import random
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import UserStates
import random
import asyncio

users: dict[int, list[int, FSMContext]] = {}

async def search(message: Message, state: FSMContext):
    await asyncio.sleep(random.randint(0, 3))
    current_state = await state.get_state()
    if current_state == UserStates.search.state:
        await message.answer('❌ You\'re already searching.')
    elif current_state == UserStates.talk.state:
        await message.answer('❌ You\'re already chatting.')
    else:
        await state.set_state(UserStates.search.state)
        if not users or (len(users) == 1 and message.from_user.id in users):
            await message.answer('🔎 Searching...')
            users[message.from_user.id] = [message.chat.id, state]
        else:
            user = random.choice(list(users.keys()))
            chat, context = users[user]
            del users[user]
            await context.set_state(UserStates.talk.state)
            await context.update_data(talk=[message.chat.id, state, {}])
            await state.set_state(UserStates.talk.state)
            await state.update_data(talk=[chat, context, {}])
            await message.bot.send_message(chat, '👤 Interlocutor founded!')
            await message.answer('👤 Interlocutor founded!')

def register_handlers_search(dp: Dispatcher):
    dp.message.register(search, Command('search'))
