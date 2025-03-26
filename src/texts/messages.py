"""
Текстовые сообщения

Содержит:
- Шаблоны сообщений
- Тексты ошибок
- Форматированные подсказки
"""

# Сообщения об ошибках
INCORRECT_COMMAND = """
<b>❌ Неизвестная команда</b>
Используйте /help для просмотра доступных команд
"""

# Шаблон ввода карты
CARD_INPUT_TEMPLATE = """
<b>💳 Как добавить карту?</b>

Отправьте сообщение в формате:

<pre>
Название карты
категория1 кешбек1
категория2 кешбек2
...
</pre>

<b>🔹 Пример:</b>
<pre>
Alpha Premium
products 0.05
fuel 0.10
travels 0.15
taxi 0.20
</pre>

<b>📋 Список категорий</b> (кешбек указывается десятичной дробью):
• <code>products</code> - 🍏 Продукты (5%)
• <code>fuel</code> - ⛽ Топливо (10%)
• <code>travels</code> - ✈️ Путешествия (15%)
• <code>taxi</code> - 🚕 Такси (20%)
• <code>medic</code> - 🏥 Медицина
• <code>clothing</code> - 👕 Одежда
• <code>education</code> - 🎓 Образование
• <code>cosmetics</code> - 💄 Косметика
• <code>electronics</code> - 📱 Электроника
• <code>entertainments</code> - 🎭 Развлечения
• <code>restaurant</code> - 🍽️ Рестораны
• <code>transport</code> - 🚌 Транспорт
• <code>sport</code> - ⚽ Спорт

<i>💡 Совет: Можно добавить несколько категорий для одной карты</i>
"""

# Подтверждения действий
ADDING_COMPLETED = """
<b>✅ Добавление завершено</b>
Карты успешно сохранены!
Используйте /start для возврата в меню
"""

# Помощь
HELP_MESSAGE = """
<b>📚 Доступные команды:</b>

/start - Главное меню
/add_card - Добавить новую карту
/help - Эта справка
/made_by - Об авторе

🔄 Для изменения данных просто повторно добавьте карту
"""

MADE_BY_TEXT = """
<b>Telegram Bot, созданный в процессе решения кейса на хакатоне T1</b>

Git: <a href="https://github.com/JakovManishek/Hacathon_T1">Репозиторий GitHub</a>
Контакты: @Jakov_Manishek

<i>Версия: 1.1 | 2025</i>
"""
