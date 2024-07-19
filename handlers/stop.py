from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import UserStates

async def stop(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == UserStates.talk.state:
        user, context, _ = (await state.get_data())['talk']
        await context.set_state(UserStates.passive.state)
        await state.set_state(UserStates.passive.state)
        await message.bot.send_message(user, '🏁 Interlocutor ended users')
        await message.answer('🏁 You ended users')
    elif current_state == UserStates.search.state:
        await message.answer('❌ You\'re not chatting. Maybe you wanted to end the search - /cancel')
    else:
        await message.answer('❌ You\'re not chatting.')

def register_handlers_stop(dp: Dispatcher):
    dp.message.register(stop, Command('stop'))
