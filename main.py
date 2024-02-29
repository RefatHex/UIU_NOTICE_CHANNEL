import time
from TOKEN import TOKEN, BOT_USERNAME
from scraper import get_notices
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'auto_update_executed' not in context.chat_data:
        await update.message.reply_text("Hello! Thanks for using our BOT.")
        await handle_auto_update(update, context)
        context.chat_data['auto_update_executed'] = True
    else:
        await update.message.reply_text("Hello again!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("contact admin")


async def get_updates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await handle_auto_update(update, context)


async def handle_auto_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    last_processed_news: str = ""
    await update.message.reply_text("From now on, you'll be receiving updates")

    async def job_callback(context):
        nonlocal last_processed_news
        post_text = get_notices()
        if post_text is not None and post_text != last_processed_news:
            await context.bot.send_message(chat_id='@uiu_notice_bot', text=post_text)
            print(post_text)
            last_processed_news = post_text
        print(post_text)

    context.job_queue.run_repeating(job_callback, interval=10, first=0)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

if __name__ == '__main__':
    print('Starting bot')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler(
        'get_updates', get_updates))

    # error
    app.add_error_handler(error)

    # polling
    print("Polling")
    app.run_polling(poll_interval=3)
