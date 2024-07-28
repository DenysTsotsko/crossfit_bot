import logging

from aiogram import Router, F
from aiogram.types import Message 
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

from utils.states import WorkOutForm


from keyboards.reply import *
from generators import generating_promt

router = Router()


async def process_form_step(
    message: Message, state: FSMContext, next_state: State, prompt: str, keyboard: ReplyKeyboardMarkup, data_key: str
):
    await state.update_data({data_key: message.text})
    await state.set_state(next_state)
    await message.answer(prompt, reply_markup=keyboard)


# start of the FSM 
@router.message(F.text.lower() == "workout")
async def fill_workout_requirements(message: Message, state: FSMContext) -> None:
    await state.set_state(WorkOutForm.kind)
    await message.answer("Choose type of your workout 💀", reply_markup=kind_kb)


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action in FSM
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Okay... Cancelled",
        reply_markup=main_kb,
    )


@router.message(WorkOutForm.kind)
async def form_kind(message: Message, state: FSMContext) -> None:
    # we update our state in state, works like dictionary
    await process_form_step(message, state, WorkOutForm.time, "Nice! Choose time cap ⏱️", time_kb, "kind")


@router.message(WorkOutForm.time)
async def form_time(message: Message, state: FSMContext) -> None: 
    await process_form_step(message, state, WorkOutForm.muscles, "Choose part of your body", muscles_kb,"time")

@router.message(WorkOutForm.muscles)
async def form_muscles(message: Message, state: FSMContext) -> None:
    await process_form_step(message, state, WorkOutForm.equipment, "Time to choose your equipment", equipment_kb, "muscles")


@router.message(WorkOutForm.equipment)
async def form_equipment(message: Message, state: FSMContext) -> None: 
    await process_form_step(message, state, WorkOutForm.level, "Choose the level", lvl_kb, "equipment")


@router.message(WorkOutForm.level)
async def form_level(message: Message, state: FSMContext) -> None: 
    await process_form_step(message, state, WorkOutForm.gender, "Choose the gender", gender_kb,"level")


@router.message(WorkOutForm.gender)
async def form_gender(message: Message, state: FSMContext) -> None: 
     await state.update_data(gender=message.text)
     data = await state.get_data()
     await state.clear()

     formatted_text = []
     [
         formatted_text.append(f"{key}: {value}")
         for key, value in data.items()
     ]
     response = await generating_promt(formatted_text)
     await message.answer(response, reply_markup=main_kb)