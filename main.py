from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        original_text = update.message.text
        translated = GoogleTranslator(source='ar', target='fa').translate(original_text)
        await update.message.reply_text(f"📤 ترجمه:\n{translated}")
    except Exception as e:
        await update.message.reply_text("❌ خطا در ترجمه.")

app = ApplicationBuilder().token("7816288854:AAEQ3eT4UaYxt_XiYmP5mK0H63ZpLlrtfaE").build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_message))
app.run_polling()
