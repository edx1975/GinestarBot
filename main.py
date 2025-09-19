import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ----------------------------
# Variable d'entorn per al token del bot
# ----------------------------
TELEGRAM_TOKEN = os.getenv("7901264524:AAG2ekYzZYooZrsYmOH5gGYOOTgqz6fCZnw")

# ----------------------------
# Base de dades interna de preguntes i respostes
# ----------------------------
FAQS = {
    # Informació general
    "riviere": "El riu que passa per Ginestar és el riu Ebre.",
    "historia": "Ginestar té una rica història agrícola i cultural, amb vinyes i oliveres centenàries.",
    "clima": "El clima és mediterrani continental, amb estius calorosos i hiverns frescos.",
    
    # Gastronomia
    "restaurants": "A Ginestar pots trobar restaurants locals amb plats típics com la clotxa i vins de la Ribera d'Ebre.",
    
    # Festes
    "pa amb tomaca": "🎉 Festa del Pa amb Tomaca: Se celebra el 27 de juliol amb tiquets per a ració i taula, al Passeig del Riu.",
    "festa de l'ermita": "🎉 Diada de l'Ermita de Sant Isidre: Segon diumenge de maig, amb dinar de germanor a l'ermita de Sant Isidre.",
    
    # Horaris d'autobús
    "autobus": "🚌 Horaris d'autobús Ginestar ↔ Móra d'Ebre:\n\n"
               "🟢 **Ginestar → Móra d'Ebre**:\n"
               "- Sortides: 08:30, 17:53\n"
               "- Durada: ~10 minuts\n"
               "- Preu: 1–2 €\n"
               "- Operador: ALSA\n"
               "- Dies: Dilluns a dissabte\n\n"
               "🔁 **Móra d'Ebre → Ginestar**:\n"
               "- Sortides: 08:45, 18:02\n"
               "- Durada: ~10 minuts\n"
               "- Preu: 1–2 €\n"
               "- Operador: ALSA\n"
               "- Dies: Dilluns a dissabte\n\n"
               "ℹ️ Per més informació, visita: alsa.es",
    
    # Fira
    "fira raure": "✨ XVI Fira Raure de Ginestar\n📅 Diumenge 28 de setembre de 2025: Fira d’arts i oficis amb activitats per a tots els públics.",
    
    # Entitats i associacions
    "entitats": "🏛️ Entitats i Associacions de Ginestar:\n"
                "- Lo Margalló: Grup de Natura, activitats mediambientals\n"
                "- Motoceballots: Col·lectiu de motoristes\n"
                "- GinRiders: Club de MTB\n"
                "- Lo Corral: Associació Cultural\n"
                "- La Ginesta: Associació Cultural i Banda de Música\n"
                "- Lo Local: Espai cultural comunitari\n"
                "- Associació de Dones: Suport i activitats per a dones\n"
                "- Lliga contra el Càncer: Activitats de conscienciació\n"
                "- Cooperativa Agrícola: Fundada 1918\n"
                "- Sindicat: Bar i restaurant local\n"
                "- Molí Escoda: Producció d’oli d’oliva\n"
                "- Molí Sunyer: Històric molí\n"
                "- Ferreria: Patrimoni industrial\n"
                "- Refugis Guerra Civil: Patrimoni històric\n"
                "- Brixa Montserrada Bru (1615): Document històric\n",
    
    # Patrimoni i espais culturals
    "espais culturals": "⛪ Patrimoni i espais culturals:\n"
                        "- Església parroquial de Sant Martí: Celebracions i activitats religioses\n"
                        "- Ermita de Sant Isidre: Diada de l'Ermita i altres activitats\n"
                        "- Església Vella: Activitats culturals, exposicions i esdeveniments comunitaris\n",
    
    # Curiositats
    "kayaks": "🛶 Kayaks al riu Ebre: Activitats d'aventura i rutes en kayak per la zona de Ginestar.",
    "parxis": "🏅 Ginestar va ser nomenada Capital Olímpica del Parxis durant els Jocs Olímpics de Barcelona 1992."
}

# ----------------------------
# Funcions de resposta de comandes
# ----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Benvingut al Bot Turístic de Ginestar!\n\n"
        "Pots provar aquestes opcions:\n"
        "/info - Informació general del poble\n"
        "/quevisitar - Llocs d’interès i patrimoni\n"
        "/gastronomia - Menjar típic\n"
        "/festes - Festes i tradicions\n"
        "/horaris - Horaris d'autobús\n"
        "/fira - Informació de la Fira Raure\n"
        "/entitats - Entitats i associacions\n"
        "/espais - Patrimoni i espais culturals\n"
        "/kayaks - Activitats al riu Ebre\n"
        "/parxis - Curiositats"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 Ginestar és un municipi de la Ribera d’Ebre, conegut per les seves vinyes, "
        "oliveres i paisatges de la vora del riu Ebre."
    )

async def que_visitar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏞️ Llocs per visitar a Ginestar:\n"
        "- Església parroquial de Sant Martí\n"
        "- Ermita de Sant Isidre\n"
        "- Església Vella\n"
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
        "- Festa del Pa amb Tomaca (27 de juliol)\n"
        "- Diada de l'Ermita de Sant Isidre (segon diumenge de maig)"
    )

async def horaris(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["autobus"])

async def fira(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["fira raure"])

async def entitats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["entitats"])

async def espais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["espais culturals"])

async def kayaks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["kayaks"])

async def parxis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(FAQS["parxis"])

# ----------------------------
# Funció intel·ligent per missatges lliures
# ----------------------------
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    for keyword, answer in FAQS.items():
        if keyword in msg:
            await update.message.reply_text(answer)
            return
    await update.message.reply_text(
        "❓ No t’entenc. Prova alguna de les comandes: /info /quevisitar /gastronomia /festes /horaris /fira /entitats /espais /kayaks /parxis"
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
    app.add_handler(CommandHandler("entitats", entitats))
    app.add_handler(CommandHandler("espais", espais))
    app.add_handler(CommandHandler("kayaks", kayaks))
    app.add_handler(CommandHandler("parxis", parxis))

    # Handler per preguntes lliures
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot en marxa...")
    app.run_polling()

if __name__ == "__main__":
    main()
