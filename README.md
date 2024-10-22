# Instagram & TikTok Video Downloader Bot

This is a Telegram bot built with [Aiogram 2.25](https://docs.aiogram.dev/en/latest/) that allows users to download videos from Instagram and TikTok using APIs. The bot can be deployed with either webhook or non-webhook methods.

## Features
- Download videos from Instagram and TikTok via APIs.
- Supports both webhook and polling (non-webhook) setup methods.
- Written in Python using the Aiogram 2.25 framework.

## Requirements
- Python 3.8+
- Aiogram 2.25
- [Other required libraries (list them here if any)]
  
## API Documentation
- [Instagram API](https://rapidapi.com/social-api1-instagram/api/instagram-scraper-api2)
- [TikTok API](https://rapidapi.com/yi005/api/tiktok-video-no-watermark2)
  
## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/bekiake/instagram_downloader_bot.git
    cd instagram_downloader_bot
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add the following variables:

    ```bash
    BOT_TOKEN=your_bot_token
    API_KEY_INSTAGRAM=your_instagram_api_key
    API_KEY_TIKTOK=your_tiktok_api_key
    ```

## Running the Bot

### Using Polling (non-webhook method)
To run the bot using the polling method, simply run:

```bash
python bot.py
```

## Using Webhooks

To run the bot with webhook support, you need to configure a few more settings.

1. **Ensure HTTPS Server**: Make sure you have an HTTPS server set up. You can use tools like [ngrok](https://ngrok.com/) or any other server with SSL.

2. **Update the Environment Variable**: In your `.env` file, update the `WEBHOOK_URL` to your server's URL:

   ```bash
   WEBHOOK_URL=https://yourdomain.com/webhook
   ```
3. Run the webhook setup:

    ```bash
    python webhook_bot.py
    ```

## Contributing
Feel free to fork the repository, create a new branch, and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


