import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
from environs import Env
from instagram import instagram_download
from tik_tok import tik_tok_download
from yt import get_video_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

env = Env()
env.read_env()

API_TOKEN = env.str("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Send me Instagram, Tik Tok or YouTube Url !")



@dp.message_handler(content_types=types.ContentType.TEXT)
async def download_content(message: types.Message):
    url = message.text
    instagram_pattern = r'https?:\/\/(www\.)?instagram\.com\/(p|reel|tv)\/[A-Za-z0-9_-]+\/.*?'
    tiktok_pattern = r'https?:\/\/(www\.)?tiktok\.com\/@[\w.-]+\/video\/\d+|https?:\/\/vt\.tiktok\.com\/[\w.-]+\/'
    youtube_pattern = r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})(.*)?$'
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
        elif re.match(youtube_pattern, url):
            result = get_video_data(url)
            
            await bot.send_video(
                message.chat.id,
                video=result['videos'],
                caption=result['title'],
                thumb=result['thumbnail']
            )
            await bot.send_audio(
                message.chat.id,
                audio=result['audios'],
                caption=result['title']
            )
        else:
            await bot.send_message(message.chat.id, text="Invalid URL")
            
            
            

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
