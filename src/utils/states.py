from aiogram.fsm.state import StatesGroup, State


class WorkOutForm(StatesGroup): 
    kind = State()
    time = State()
    muscles = State()
    equipment = State()
    level = State()
    gender = State()
