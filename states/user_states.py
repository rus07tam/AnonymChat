from aiogram.fsm.state import State, StatesGroup

class UserStates(StatesGroup):
    lang = State()
    passive = State()
    search = State()
    talk = State()
