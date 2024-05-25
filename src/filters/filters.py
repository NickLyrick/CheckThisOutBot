"""A module that contains filters for the handlers."""

import dataclasses

from aiogram import Bot
from aiogram.enums import ChatMemberStatus
from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.utils import formatting

from src.bot.settings import settings


class CheckPermissions(BaseFilter):
    """Check if the user has permissions to change bot settings."""

    async def __call__(self, message: Message) -> bool:
        try:
            member = await message.chat.get_member(message.from_user.id)
            if (
                member.status == ChatMemberStatus.CREATOR
                or member.user.id in settings.bot.admin_ids
            ):
                return True
            else:
                await message.reply(
                    text="У вас нет прав для изменения настроек бота для данного чата"
                )
                return False
        except Exception as e:
            await message.answer(text=f"Ошибка: \n" f"{formatting.Pre(e)}.as_html()")
            return False


@dataclasses.dataclass
class Filters:
    """A class that contains filters for the handlers."""

    check_permissions: CheckPermissions


my_filters = Filters(
    check_permissions=CheckPermissions(),
)
