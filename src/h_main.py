"""
Основной модуль бота для управления картами с кешбеком.

Модуль реализует:
- Добавление новых карт
- Просмотр карт по категориям
- Анализ карт с лучшим кешбеком
"""

import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

# Локальные модули
from database.initializer import (
    create_db
)
from database.core import (
    is_user_in_table,
    get_value_db,
    create_user,
    create_card
)
from keyboards.builders import (
    inline_category,
    add_card,
    reply_off_add_kb
)
from texts.messages import (
    INCORRECT_COMMAND,
    CARD_INPUT_TEMPLATE,
    ADDING_COMPLETED,
    HELP_MESSAGE,
    MADE_BY_TEXT,
)



# Загрузка BOT_TOKEN из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Инициализация бота с HTML-разметкой по умолчанию
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


class OrderAdd(StatesGroup):
    """Класс состояний для добавления новой карты."""
    new_card = State()


async def check_user_in_table(message: Message) -> None:
    """
    Проверяет наличие пользователя в базе данных.
    
    Если пользователя нет - создает новую запись и предлагает добавить карту.
    Если пользователь есть - показывает меню категорий.
    
    Args:
        message (Message): Объект сообщения от пользователя
    """
    user_id = message.chat.id
    name = message.chat.username

    if not is_user_in_table(user_id):
        create_user(user_id, name)
        add_card_command(message)
    else:
        await message.answer(
            text="Выберите категорию",
            reply_markup=inline_category()
        )


@dp.message(CommandStart())
async def start(message: Message) -> None:
    """Обработчик команды /start."""
    await check_user_in_table(message)


@dp.message(Command('add_card'))
async def add_card_command(message: Message) -> None:
    """Обработчик команды /add_card. Отправляет инструкцию по добавлению новой карты."""
    await message.answer(
        text="Добавление новой карты",
        reply_markup=add_card()
    )


@dp.message(Command('help'))
async def help_command(message: Message) -> None:
    """Обработчик команды /help. Отправляет инструкцию по использованию бота."""
    await message.answer(
        text=HELP_MESSAGE,
        parse_mode="HTML"
    )


@dp.message(Command('made_by'))
async def made_by_command(message: Message) -> None:
    """Обработчик команды /made_by. Отправляет информацию об авторе бота."""
    await message.answer(
        text=MADE_BY_TEXT,
        parse_mode="HTML"
    )


@dp.callback_query(F.data)
async def inline_callback(
    callback: CallbackQuery,
    state: FSMContext
) -> None:
    """
    Обработчик inline-кнопок.
    
    Args:
        callback (CallbackQuery): Объект callback от кнопки
        state (FSMContext): Контекст состояния
    """
    await state.clear()
    user_id = callback.message.chat.id
    call = str(callback.data)

    match call:
        case 'add':
            await callback.answer()
            await state.set_state(OrderAdd.new_card)
            await callback.message.answer(
                text=CARD_INPUT_TEMPLATE,
                reply_markup=reply_off_add_kb()
            )
            
        case _:
            # Получаем карты пользователя по выбранной категории
            cards = get_value_db(table="Cards", id=user_id)
            filtered_cards = [card for card in cards if card[3] == call]
            cashbacks = [card[4] for card in filtered_cards]
            
            if not filtered_cards:
                await callback.answer(f"В категории {call} нет карт")
                return
                
            best_card_index = cashbacks.index(max(cashbacks))
            best_card = filtered_cards[best_card_index]
            
            await callback.answer(f"Вы выбрали {call}")
            await callback.message.answer(
                f"Лучшая ваша карта: {best_card[2]}\n"
                f"Кешбек: {max(cashbacks)}%"
            )


@dp.message(F.text, OrderAdd.new_card)
async def folder_name_chosen(
    message: Message,
    state: FSMContext
) -> None:
    """
    Обработчик добавления новой карты.
    
    Args:
        message (Message): Сообщение с данными карты
        state (FSMContext): Контекст состояния
    """
    user_id = message.chat.id
    text = message.text

    if text == "Завершить добавление":
        await state.clear()
        await message.answer(ADDING_COMPLETED)
        return
        
    try:
        # Парсинг данных карты
        lines = text.split('\n')
        name = lines[0]
        cashbacks = {
            elem.split()[0]: float(elem.split()[1])
            for elem in lines[1:]
        }

        # Сохранение карт в БД
        for category, cashback in cashbacks.items():
            create_card(user_id, name, category, cashback)
            
    except (IndexError, ValueError):
        await message.answer("Ошибка формата. Используйте шаблон из примера.")


@dp.message(F.text)
async def other_text(message: Message) -> None:
    """
    Обработчик прочих текстовых сообщений.
    
    Args:
        message (Message): Входящее сообщение
    """
    if message.chat.type == "private":
        await message.answer(text=INCORRECT_COMMAND)


async def main() -> None:
    """Основная функция запуска бота."""
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Для первоначальной настройки БД:
    # os.remove("database_hackaton.db")
    # create_db()
    
    asyncio.run(main())