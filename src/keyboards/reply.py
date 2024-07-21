from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Workout"),
            KeyboardButton(text="Language 🇺🇦/🇺🇸")
        ]
    ], 
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Choose action from the menu",
    selective=True
)