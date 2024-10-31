from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Replace "your_own_API_Token got from BotFather" with your actual bot token
TOKEN = "your_own_API_Token"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello sir, Welcome to the Bot. Please write /help to see the commands available."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Available Commands:
    /youtube - To get the YouTube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get the Gmail URL
    /geeks - To get the GeeksforGeeks URL
    """)

async def gmail_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Your Gmail link here (I am not giving mine one for security reasons)"
    )

async def youtube_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("YouTube Link => https://www.youtube.com/")

async def linkedin_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("LinkedIn URL => https://www.linkedin.com/")

async def geeks_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("GeeksforGeeks URL => https://www.geeksforgeeks.org/")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Sorry, '{update.message.text}' is not a valid command."
    )

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Sorry, I can't recognize you, you said '{update.message.text}'."
    )

if __name__ == "__main__":
    # Initialize the application
    app = ApplicationBuilder().token(TOKEN).build()

    # Registering the command handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('youtube', youtube_url))
    app.add_handler(CommandHandler('linkedin', linkedin_url))
    app.add_handler(CommandHandler('gmail', gmail_url))
    app.add_handler(CommandHandler('geeks', geeks_url))

    # Registering the message handlers
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), unknown_text))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the bot
    app.run_polling()