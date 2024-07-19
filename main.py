import asyncio
from aiogram import Dispatcher
from bot_init import bot, dp
from handlers.start import register_handlers_start
from handlers.search import register_handlers_search
from handlers.cancel import register_handlers_cancel
from handlers.stop import register_handlers_stop
from handlers.message import register_handlers_message
from handlers.message_reaction import register_handlers_message_reaction

def register_all_handlers(dp: Dispatcher):
    register_handlers_start(dp)
    register_handlers_search(dp)
    register_handlers_cancel(dp)
    register_handlers_stop(dp)
    register_handlers_message(dp)
    register_handlers_message_reaction(dp)

if __name__ == '__main__':
    register_all_handlers(dp)
    asyncio.run(dp.start_polling(bot))
