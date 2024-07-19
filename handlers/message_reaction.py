from aiogram import Dispatcher
from aiogram.types import MessageReactionUpdated
from aiogram.fsm.context import FSMContext
from states import UserStates

async def on_message_reaction(reaction: MessageReactionUpdated, state: FSMContext):
    user, _, messages = (await state.get_data())['talk']
    if reaction.message_id in messages:
        await reaction.bot.set_message_reaction(
            chat_id=user,
            message_id=messages[reaction.message_id],
            reaction=reaction.new_reaction
        )

def register_handlers_message_reaction(dp: Dispatcher):
    dp.message_reaction.register(on_message_reaction, UserStates.talk)