import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook
import re
from environs import Env
from instagram import instagram_download
from tik_tok import tik_tok_download

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
env = Env()
env.read_env()

API_TOKEN = env.str("BOT_TOKEN")
WEBHOOK_HOST = env.str("WEBHOOK_HOST")  # Your public domain or ngrok URL
WEBHOOK_PATH = f"/{API_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Webhook settings
WEBAPP_HOST = '0.0.0.0'  # Or your local IP address
WEBAPP_PORT = 3000        # Port for webhook to listen

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Handlers
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Send me Instagram or TikTok URL!")

@dp.message_handler()
async def download_content(message: types.Message):
    url = message.text
    instagram_pattern = r'https?:\/\/(www\.)?instagram\.com\/(p|reel|tv)\/[A-Za-z0-9_-]+\/.*?'
    tiktok_pattern = r'https?:\/\/(www\.)?tiktok\.com\/@[\w.-]+\/video\/\d+|https?:\/\/vt\.tiktok\.com\/[\w.-]+\/'
    
    if not url.startswith("https://"):
        await bot.send_message(message.chat.id, text=url)
    else:
        if re.match(instagram_pattern, url):
            insta_video = instagram_download(url)
            await bot.send_video(message.chat.id, video=insta_video)
        
        elif re.match(tiktok_pattern, url):
            media = tik_tok_download(url)
            tt_video = media[0]
            tt_music = media[1]
            await bot.send_video(message.chat.id, video=tt_video)
            await bot.send_audio(message.chat.id, audio=tt_music)
            
        else:
            await message.answer("Not a valid Instagram or TikTok URL.")

# Webhook startup and shutdown handlers
async def on_startup(dp):
    # Set webhook
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    # Remove webhook
    await bot.delete_webhook()

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
