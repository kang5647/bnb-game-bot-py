from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, CallbackGame
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
from dotenv import load_dotenv
import os 
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    game_name = "counter"  # Set this to your game's short name

    keyboard = [
        [InlineKeyboardButton("Play This Game", callback_game= CallbackGame())],
        [InlineKeyboardButton("Help", callback_data='help')],
        ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_game(chat_id, game_short_name=game_name, reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    
    if query.data == 'help':
        await context.bot.answer_callback_query(query.id, text="Help message: How to play the game...")
    elif query.game_short_name == 'counter':
        await context.bot.answer_callback_query(query.id, url="https://t.me/BNBMiniGame_bot/bnbminiapp")
    # if query.data == 'help':
    #     await context.bot.answer_callback_query(query.id, text='help')
    # await context.bot.answer_callback_query(query.id, url="https://t.me/BNBMiniGame_bot/bnbminiapp")

async def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_error_handler(error)
    application.run_polling()



if __name__ == '__main__':
    main()
