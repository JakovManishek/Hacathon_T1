"""
Модуль для работы с клавиатурами в aiogram.

Содержит функции для создания:
- Inline-клавиатур с категориями
- Кнопки добавления карты
- Reply-клавиатуры для завершения ввода
"""

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup
)


def inline_category() -> InlineKeyboardMarkup:
    """
    Создает inline-клавиатуру с категориями для выбора.
    
    Returns:
        InlineKeyboardMarkup: Клавиатура с 13 категориями в один столбец
    """
    categories = [
        ("Продукты", "products"),
        ("Медицина", "medic"),
        ("Топливо", "fuel"),
        ("Вещи", "clothing"),
        ("Образование", "education"),
        ("Косметика", "cosmetics"),
        ("Электроника", "electronics"),
        ("Развлечения", "entertaiments"),
        ("Рестораны", "restaraunt"),
        ("Транспорт", "transport"),
        ("Спорт", "sport"),
        ("Такси", "taxi"),
        ("Путешествия", "travels")
    ]
    
    keyboard = [
        [InlineKeyboardButton(text=text, callback_data=data)]
        for text, data in categories
    ]
    
    return InlineKeyboardMarkup(
        inline_keyboard=keyboard,
        resize_keyboard=True,
        row_width=1
    )


def add_card() -> InlineKeyboardMarkup:
    """
    Создает inline-кнопку для добавления новой карты.
    
    Returns:
        InlineKeyboardMarkup: Клавиатура с одной кнопкой
    """
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Добавить карту", 
                callback_data="add"
            )]
        ],
        resize_keyboard=True,
        row_width=1
    )


def reply_off_add_kb() -> ReplyKeyboardMarkup:
    """
    Создает reply-клавиатуру с кнопкой завершения ввода.
    
    Returns:
        ReplyKeyboardMarkup: Клавиатура с одной кнопкой
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Завершить добавление")]
        ],
        resize_keyboard=True,
        row_width=1
    )