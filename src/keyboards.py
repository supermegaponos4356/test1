from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_confirm_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подтвердить", callback_data="confirm_reg"),
                InlineKeyboardButton(text="Начать заново", callback_data="restart_reg")
            ]
        ]
    )


