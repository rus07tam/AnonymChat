from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states import UserStates

async def on_message(message: Message, state: FSMContext):
    me = (await state.get_data())['talk']
    another = (await me[1].get_data())['talk']

    if (message.reply_to_message) and (message.reply_to_message.message_id in me[2]):
        msg = await message.copy_to(me[0], reply_to_message_id=me[2][message.reply_to_message.message_id])
    else:
        msg = await message.copy_to(me[0])

    another[2][msg.message_id] = message.message_id
    me[2][message.message_id] = msg.message_id
    await state.update_data(talk=me)
    await me[1].update_data(talk=another)

def register_handlers_message(dp: Dispatcher):
    dp.message.register(on_message, UserStates.talk)