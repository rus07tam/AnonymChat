from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import UserStates
from handlers.search import users

async def cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == UserStates.search.state:
        await state.set_state(UserStates.passive.state)
        del users[message.from_user.id]
        await message.answer('✅ Seacrch cancelled')
    elif current_state == UserStates.talk.state:
        await message.answer('❌ You\'re not searching. Maybe you wanted to end the users - /stop')
    else:
        await message.answer('❌ You\'re not searching')

def register_handlers_cancel(dp: Dispatcher):
    dp.message.register(cancel, Command('cancel'))
