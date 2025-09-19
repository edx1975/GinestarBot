import os
import openai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# ----------------------------
# Variables d'entorn
# ----------------------------
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_TOKEN:
    print("❌ Falta la variable d'entorn TELEGRAM_TOKEN")
    exit(1)

if not OPENAI_API_KEY:
    print("❌ Falta la variable d'entorn OPENAI_API_KEY")
    exit(1)

openai.api_key = OPENAI_API_KEY

print("✅ OpenAI i Telegram tokens carregats")
print("OpenAI version:", openai.__version__)

# ----------------------------
# Base de dades interna (keywords)
# ----------------------------
FAQS = {
    "info": "📍 Ginestar és un municipi de la Ribera d’Ebre...",
    "quevisitar": "🏞️ Llocs per visitar: Església parroquial, Ermita de Sant Isidre...",
    "gastronomia": "🍇 Gastronomia: Vins, Oli, Clotxa...",
    "festes": "🎉 Festes: Festa Major, Pa amb Tomaca, Diada de l'Ermita...",
    "horaris": "🚌 Horaris d'autobús Ginestar ↔ Móra d'Ebre: 08:30, 17:53...",
    "fira": "✨ XVI Fira Raure de Ginestar, 28 de setembre de 2025...",
    "entitats": "🏛️ Entitats i associacions locals...",
    "espais": "⛪ Patrimoni i espais culturals: Església parroquial, Ermita, Església Vella",
    "kayaks": "🛶 Kayaks al riu Ebre: activitats i rutes...",
    "parxis": "🏅 Ginestar: Capital Olímpica del Parxis 1992"
}

# ----------------------------
# Comandes
# ----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Benvingut al Bot Turístic de Ginestar!\n\n"
        "Comandes disponibles:\n"
        "/info /quevisitar /gastronomia /festes /horaris /fira /entitats /espais /kayaks /parxis\n\n"
        "També pots fer preguntes lliures sobre el poble!"
    )

async def send_faq(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str):
    await update.message.reply_text(FAQS[key])

# ----------------------------
# Funció intel·ligent amb GPT (ChatCompletion 1.31)
# ----------------------------
def chat_with_gpt(message: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ets un guia turístic expert de Ginestar, Ribera d’Ebre."},
                {"role": "user", "content": message}
            ],
            max_tokens=250,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error en generar la resposta: {e}"

# ----------------------------
# Handler per missatges lliures
# ----------------------------
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    for keyword, answer in FAQS.items():
        if keyword in msg:
            await update.message.reply_text(answer)
            return
    reply = chat_with_gpt(update.message.text)
    await update.message.reply_text(reply)

# ----------------------------
# Main
# ----------------------------
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Comandes
    for cmd, key in [("info","info"),("quevisitar","quevisitar"),("gastronomia","gastronomia"),
                     ("festes","festes"),("horaris","horaris"),("fira","fira"),
                     ("entitats","entitats"),("espais","espais"),("kayaks","kayaks"),
                     ("parxis","parxis")]:
        app.add_handler(CommandHandler(cmd, lambda u,c,k=key: send_faq(u,c,k)))

    # Missatges lliures
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot en marxa amb GPT (OpenAI 1.31)...")
    app.run_polling()

if __name__ == "__main__":
    main()
