from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Diccionario con preguntas clave y respuestas
faq = {
    "raven quest": "Raven Quest es un juego de minería en línea donde los jugadores extraen recursos valiosos y compiten en eventos.",
    "registrarme": "Para registrarte, visita el sitio oficial de Raven Quest https://bit.ly/money_ravenquest y sigue las instrucciones.",
    "recursos": "Los recursos disponibles para minar incluyen oro, esmeraldas, rubíes y diamantes.",
    "mejorar mineros": "Puedes mejorar a tus mineros utilizando los recursos obtenidos para aumentar su eficiencia.",
    "tokens": "Los tokens $QUEST son la moneda del juego que se obtiene al intercambiar recursos y se usan en el juego.",
    "jugar con amigos": "Sí, puedes colaborar con amigos para mejorar tu experiencia en el juego.",
    "eventos": "Sí, Raven Quest organiza eventos semanales con recompensas especiales.",
    "batalla de guild": "Es un evento competitivo donde los jugadores luchan para demostrar su supremacía.",
    "intercambiar recursos": "Puedes usar el mercado del juego para intercambiar recursos por tokens u otros beneficios.",
    "clan": "Puedes colaborar con otros jugadores, participar en batallas y ganar recompensas adicionales.",
    "batallas de clanes": "Debes ser parte de un clan y unirte a las batallas programadas.",
    "impulsos": "Son herramientas que aumentan tus posibilidades de ganar.",
    "hechizos": "Son herramientas que aumentan tus posibilidades de ganar.",
    "vip gold": "Alcanzando ciertos logros en el juego puedes obtener este estatus y crear un clan.",
    "liga de principiantes": "Sí, puedes entrar a la Liga Pro creando un minero en cualquier momento.",
    "mercado": "Es una plataforma donde puedes intercambiar tus recursos por tokens.",
    "ganar": "Utilizando impulsos y hechizos estratégicamente.",
    "recompensas extra": "Son beneficios adicionales por alcanzar ciertos estatus o participar en eventos.",
    "crear clan": "Necesitas alcanzar el estatus VIP Gold I para poder crearlo.",
    "batallas individuales": "Son duelos en los que puedes ganar tokens al vencer a tu oponente.",
    "más información": "Puedes visitar el sitio oficial de Raven Quest: https://bit.ly/money_ravenquest"
}

# Función para responder al comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = (
        "¡Hola! Soy la IA de Raven Quest. Pregúntame sobre el juego y te ayudaré.\n\n"
        "🪙 Regístrate y únete a esta aventura épica:\n"
        "👉 https://bit.ly/money_ravenquest\n\n"
        "💰 Intercambia tu dinero del juego por dinero real (hasta 20 $ por día)\n\n"
        "🎥 Mira este video para más detalles comoganar dinero:\n"
        "https://www.facebook.com/bazardeltiempo0/videos/1012406104184550"
    )
    await update.message.reply_text(mensaje)

# Función para manejar preguntas
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip().lower()

    for keyword, answer in faq.items():
        if keyword in user_message:
            await update.message.reply_text(answer)
            return

    await update.message.reply_text(
        "Lo siento, no tengo información exacta sobre eso. Te recomiendo visitar el sitio oficial de Raven Quest para más detalles: https://bit.ly/money_ravenquest"
    )

# Función principal
def main():
    bot_token = "7197850507:AAE-a7iS8Ls_zWphjNUisKZooH1vyFNFKr0"

    app = Application.builder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot de Raven Quest Iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()

   

   

    