import telebot
import g4f
import asyncio

g4f.debug.logging = True
g4f.debug.check_version = False
print(g4f.Provider.Bing.params)

# Токен вашего бота в Telegram
TOKEN = '6500323231:AAF_ZDKnyG_ZaseRVZRQ54Hlr82y9-FYWig'
bot = telebot.TeleBot(TOKEN)

async def ask(prompt: str) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )
    return response['replies'][0]['content'] if 'replies' in response and len(response['replies']) > 0 else "Sorry, I couldn't understand that."

@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    asyncio.run(send_response(message))

async def send_response(message):
    response = await ask(message.text)
    bot.reply_to(message, response)

bot.polling()
