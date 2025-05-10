# Cashback Card Bot

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Aiogram](https://img.shields.io/badge/aiogram-3.x-green)
![SQLite](https://img.shields.io/badge/database-SQLite-yellow)
![License](https://img.shields.io/badge/license-MIT-orange)

Telegram-бот для анализа и сравнения кешбек-карт с возможностью персонализированных рекомендаций.

## Основные возможности

- **Сравнение карт** по категориям расходов
- **Автоматический подбор** карты с максимальным кешбеком
- Удобное управление через Telegram-интерфейс
- Парсинг данных о картах из сообщений

### Алгоритмы работы

1. **Анализ кешбека**:
   - Поиск максимального кешбека в каждой категории (`O(n)`)
   - Кэширование результатов для быстрого доступа

2. **Обработка данных карт**:
   ```python
   # Пример ввода:
   Название карты
   Категория1 5.5%
   Категория2 3%
   ```

## Установка  
```bash
git clone https://github.com/JakovManishek/Hacathon_T1.git```
