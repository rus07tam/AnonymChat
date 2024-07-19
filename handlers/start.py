from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from states import UserStates

async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(UserStates.passive.state)
    await message.answer('Привет! Я бот, который помогает находить собеседника для вас.')

def register_handlers_start(dp: Dispatcher):
    dp.message.register(cmd_start, CommandStart())
