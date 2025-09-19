import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ----------------------------
# Variable d'entorn per al token del bot
# ----------------------------
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ----------------------------
# Base de dades interna de preguntes i respostes
# ----------------------------
FAQS = {
    "ribera": "El riu que passa per Ginestar és el riu Ebre.",
    "restaurants": "A Ginestar pots trobar restaurants locals amb plats típics com la clotxa i vins de la Ribera d'Ebre.",
    "historia": "Ginestar té una rica història agrícola i cultural, amb vinyes i oliveres centenàries.",
    "hotels": "Ginestar és petit i no té grans hotels, però hi ha allotjaments rurals i cases de turisme.",
    "clima": "El clima és mediterrani continental, amb estius calorosos i hiverns frescos.",
    "autobus": "🚌 Horaris d'autobús a Ginestar:\n- Dilluns a divendres: 07:00, 09:00, 12:00, 17:00\n- Dissabtes: 09:00, 12:00, 17:00\n- Diumenges: 10:00, 15:00",
    "fira raure": "✨ XVI Fira Raure de Ginestar\n📅 El pròxim diumenge 28 de setembre de 2025 celebrarem una nova edició de la nostra fira d’arts i oficis, amb l’essència de sempre i moltes activitats per a tots els públics."
}

# ----------------------------
# Funcions de resposta de comandes
# ----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Missatge de benvinguda"""
    await update.message.reply_text(
        "👋 Benvingut al Bot Turístic de Ginestar!\n\n"
        "Pots provar aquestes opcions:\n"
        "/info - Informació general del poble\n"
        "/quevisitar - Llocs d’interès\n"
        "/gastronomia - Menjar típic\n"
        "/festes - Festes i tradicions\n"
        "/horaris - Horaris d'autobús\n"
        "/fira - Informació de la Fira Raure\n"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 Ginestar és un municipi de la Ribera d’Ebre, conegut per les seves vinyes, "
        "oliveres i paisatges de la vora de l’Ebre."
    )

async def que_visitar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏞️ Llocs per visitar a Ginestar:\n"
        "- L’església parroquial de Sant Martí\n"
        "- Passeig pel riu Ebre\n"
        "- Vinyes i oliveres\n"
        "- Rutes de senderisme i ciclisme"
    )

async def gastronomia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍇 Gastronomia de Ginestar:\n"
        "- Vins de la Ribera d’Ebre\n"
        "- Oli d’oliva extra verge\n"
        "- Plats tradicionals com la clotxa"
    )

async def festes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎉 Festes de Ginestar:\n"
        "- Festa Major de Sant Martí (novembre)\n"
        "- Festes d’estiu amb activitats culturals i esportives\n"
        "- Tradicions populars i música en viu"
    )

async def horaris(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["autobus"])

async def fira(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["fira raure"])

# ----------------------------
# Funció intel·ligent per missatges lliures
# ----------------------------
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Busca paraules clau a FAQS i respon"""
    msg = update.message.text.lower()
    for keyword, answer in FAQS.items():
        if keyword in msg:
            await update.message.reply_text(answer)
            return
    # Si no troba res
    await update.message.reply_text(
        "❓ No t’entenc. Prova alguna de les comandes: /info /quevisitar /gastronomia /festes /horaris /fira"
    )

# ----------------------------
# Funció principal
# ----------------------------
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("❌ Falta la variable d'entorn TELEGRAM_BOT_TOKEN")

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Handlers de comandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("quevisitar", que_visitar))
    app.add_handler(CommandHandler("gastronomia", gastronomia))
    app.add_handler(CommandHandler("festes", festes))
    app.add_handler(CommandHandler("horaris", horaris))
    app.add_handler(CommandHandler("fira", fira))

    # Handler per preguntes lliures
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot en marxa...")
    app.run_polling()


if __name__ == "__main__":
    main()
