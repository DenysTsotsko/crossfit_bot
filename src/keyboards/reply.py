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


kind_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="EMOM"), 
            KeyboardButton(text="AMRAP"), 
            KeyboardButton(text="WOD"), 
            KeyboardButton(text="TABATA")
         ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose type of your workout",
    selective=True
)


time_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-5min."), 
            KeyboardButton(text="5-10min.") 
        ],
        [
            KeyboardButton(text="10-20min."), 
            KeyboardButton(text=">30min")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose time cap",
    selective=True
)


muscles_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Upper body"), 
            KeyboardButton(text="Lower body"), 
            KeyboardButton(text="Full body"), 
            KeyboardButton(text="ABS")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose body part",
    selective=True
)


equipment_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="No equipment"), 
         KeyboardButton(text="Gym"), 
         KeyboardButton(text="Outdoor")
        ]
    ], 
    resize_keyboard=True,
    input_field_placeholder="Choose body part",
    selective=True
)


lvl_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Easy"), 
         KeyboardButton(text="Medium"), 
         KeyboardButton(text="Hard")
        ]
    ], 
    resize_keyboard=True,
    input_field_placeholder="Choose body part",
    selective=True
)


gender_kb = ReplyKeyboardMarkup(
    [ 
        [
            KeyboardButton(text="M"), 
            KeyboardButton(text="W"), 
            KeyboardButton(text="Both")
        ]
    ]
)