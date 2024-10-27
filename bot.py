# bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sqlite3
from config import TOKEN

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot.')


# Подключение к базе данных SQLite
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        username TEXT
    )
    ''')
    conn.commit()
    conn.close()


# Основная функция для запуска бота
def main():
    init_db()  # Инициализация базы данных

    app = ApplicationBuilder().token(TOKEN).build()

    # Добавление обработчика команды /start
    app.add_handler(CommandHandler('start', start))

    # Запуск бота
    app.run_polling()

#comment to test commit



#comment to test commit 2

if __name__ == '__main__':
    main()
