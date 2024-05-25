"""Initialize dispatcher"""

import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.chat_action import ChatActionMiddleware

# Middlewares
# from src.middleware.db_middleware import DBSession

# Routers
# from src.handlers.basic_handlers import basic_router
# from src.handlers.game_score_handlers import game_score_router
# from src.handlers.records_handlers import records_router
# from src.handlers.schedule_handlers import schedule_router
# from src.handlers.tables_handlers import table_router
# from src.handlers.wiki_handlers import wiki_router


# from src.database import Request


dispatcher = Dispatcher()


async def register_routers(dp: Dispatcher) -> None:
    """Register Routers"""

    # dp.include_routers(
    #     basic_router,
    #     game_score_router,
    #     table_router,
    #     schedule_router,
    #     records_router,
    #     wiki_router,
    # )


async def register_middlewares(dp: Dispatcher, bot: Bot) -> None:
    """Register Middlewares"""

    # # Create request
    # request = Request()
    # await request.create_connection()
    # logging.info("Connection created")

    # Create middlewares
    # db_middleware = DBSession(request=request)
    chat_action_middleware = ChatActionMiddleware()

    dp.message.middleware.register(chat_action_middleware)
    dp.update.middleware.register(chat_action_middleware)
    dp.error.middleware.register(chat_action_middleware)

    # dp.update.middleware.register(db_middleware)


@dispatcher.startup()
async def on_startup(dispatcher: Dispatcher, bot: Bot) -> None:
    """On startup"""

    # Register middlewares
    await register_middlewares(dp=dispatcher, bot=bot)
    logging.info("Middlewares registered")

    await register_routers(dp=dispatcher)
    logging.info("Routers registered")