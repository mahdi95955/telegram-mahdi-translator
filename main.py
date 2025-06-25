from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from googletrans import Translator

translator = Translator()

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        try:
            translated = translator.translate(update.message.text, src='ar', dest='fa')
            await update.message.reply_text(f"📤 ترجمه:
{translated.text}")
        except Exception as e:
            await update.message.reply_text("❌ خطا در ترجمه.")
    else:
        await update.message.reply_text("❗ فقط پیام متنی قابل ترجمه است.")

app = ApplicationBuilder().token("7731294839:AAHv7Rt78_Jbxs6wlqv_SPGhFgmIL5mLJxA").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
app.run_polling()