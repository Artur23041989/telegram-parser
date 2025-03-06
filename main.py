from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from handlers import router as client_router


load_dotenv()

# создаем объект бота и диспетчера (маршрутизатора)
bot = Bot(token=getenv('bot_token'))
dp = Dispatcher()
dp.include_router(client_router)



dp.run_polling(bot)


