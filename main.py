import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ✅ El token s'agafa d'una variable d'entorn
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# ──────────────────────────────────────────────
# Funcions de resposta
# ──────────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Missatge de benvinguda quan l'usuari escriu /start"""
    await update.message.reply_text(
        "👋 Benvingut al Bot Turístic de Ginestar!\n\n"
        "Pots provar aquestes opcions:\n"
        "/info - Informació general del poble\n"
        "/quevisitar - Llocs d’interès\n"
        "/gastronomia - Menjar típic\n"
        "/festes - Festes i tradicions\n"
    )


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Informació general del poble"""
    await update.message.reply_text("📍 *Ginestar* és un municipi de la Ribera d’Ebre, conegut per les seves vinyes, "
        "oliveres i paisatges de la vora de l’Ebre.\n\n"
        "És un lloc tranquil per gaudir de la natura i la cultura rural catalana."
    )


async def que_visitar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Llocs d’interès turístic"""
    await update.message.reply_text(
        "🏞️ *Llocs per visitar a Ginestar:*\n"
        "- L’església parroquial de Sant Martí.\n"
        "- El passeig pel riu Ebre.\n"
        "- Les vinyes i oliveres de l’entorn.\n"
        "- Rutes de senderisme i ciclisme pels voltants."
    )


async def gastronomia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menjar típic"""
    await update.message.reply_text(
        "🍇 *Gastronomia de Ginestar:*\n"
        "- Vins de la Ribera d’Ebre.\n"
        "- Oli d’oliva extra verge.\n"
        "- Plats tradicionals catalans com la clotxa."
    )


async def festes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Festes locals"""
    await update.message.reply_text(
        "🎉 *Festes de Ginestar:*\n"
        "- Festa Major al voltant de Sant Martí (novembre).\n"
        "- Festes d’estiu amb activitats culturals i esportives.\n"
        "- Tradicions populars i música en viu."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Resposta per defecte quan l’usuari escriu quelcom desconegut"""
    await update.message.reply_text(
        "❓ No t’entenc. Prova alguna de les comandes: /info /quevisitar /gastronomia /festes"
    )


# ──────────────────────────────────────────────
# Funció principal
# ──────────────────────────────────────────────
def main():
    """Arrenca el bot"""
    if not TELEGRAM_TOKEN:
        raise ValueError("❌ Falta la variable d'entorn TELEGRAM_BOT_TOKEN")

    # Creem l’aplicació
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Assignem els handlers (ordres)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("quevisitar", que_visitar))
    app.add_handler(CommandHandler("gastronomia", gastronomia))
    app.add_handler(CommandHandler("festes", festes))

    # Handler per missatges normals
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot en marxa...")
    app.run_polling()


if __name__ == "__main__":
    main()

