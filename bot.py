from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("¡Hola! Soy un bot sencillo desplegado en Koyeb 🎉.")

# Comando /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Estos son los comandos disponibles:\n/start - Saludo inicial\n/help - Ayuda")

def main():
    # Token del Bot (obtenlo desde @BotFather en Telegram)
    BOT_TOKEN = "7725269349:AAFIIvoGEb872FExb6Lhq6GW_dftbCM2XMg"

    # Inicializar el bot
    updater = Updater(BOT_TOKEN)

    # Añadir manejadores de comandos
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
