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
    print("⚠️ Falta la variable d'entorn TELEGRAM_BOT_TOKEN")
    exit(0)

if not OPENAI_API_KEY:
    print("⚠️ Falta la variable d'entorn OPENAI_API_KEY")
    exit(0)

openai.api_key = OPENAI_API_KEY

# ----------------------------
# Base de dades interna (keywords)
# ----------------------------
FAQS = {
    "info": "📍 Ginestar és un municipi de la Ribera d’Ebre, conegut per vinyes, oliveres i paisatges del riu Ebre.",
    "quevisitar": "🏞️ Llocs per visitar:\n- Església parroquial de Sant Martí\n- Ermita de Sant Isidre\n- Església Vella\n- Passeig pel riu Ebre\n- Vinyes i oliveres\n- Rutes de senderisme i ciclisme",
    "gastronomia": "🍇 Gastronomia:\n- Vins de la Ribera d’Ebre\n- Oli d’oliva extra verge\n- Plats tradicionals com la clotxa",
    "festes": "🎉 Festes:\n- Festa Major de Sant Martí (novembre)\n- Festa del Pa amb Tomaca (27 de juliol)\n- Diada de l'Ermita de Sant Isidre (segon diumenge de maig)",
    "horaris": "🚌 Horaris d'autobús Ginestar ↔ Móra d'Ebre:\n🟢 Ginestar → Móra d'Ebre: 08:30, 17:53\n🔁 Móra d'Ebre → Ginestar: 08:45, 18:02\nOperador: ALSA, Dilluns a dissabte",
    "fira": "✨ XVI Fira Raure de Ginestar\n📅 Diumenge 28 de setembre de 2025: Fira d’arts i oficis amb activitats per a tots els públics.",
    "entitats": "🏛️ Entitats i Associacions:\n- Lo Margalló, Motoceballots, GinRiders, Lo Corral, La Ginesta, Lo Local\n- Associació de Dones, Lliga contra el Càncer\n- Cooperativa Agrícola, Sindicat, Molí Escoda, Molí Sunyer, Ferreria, Refugis Guerra Civil, Brixa Montserrada Bru (1615)",
    "espais": "⛪ Patrimoni i espais culturals:\n- Església parroquial de Sant Martí\n- Ermita de Sant Isidre\n- Església Vella",
    "kayaks": "🛶 Kayaks al riu Ebre: activitats d'aventura i rutes en kayak per Ginestar.",
    "parxis": "🏅 Ginestar va ser nomenada Capital Olímpica del Parxis durant els Jocs Olímpics de Barcelona 1992."
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
# Funció intel·ligent amb GPT (ChatCompletion)
# ----------------------------
def chat_with_gpt(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ets un guia turístic expert de Ginestar, Ribera d’Ebre. Dona respostes concretes, clares i útils sobre festes, gastronomia, activitats, patrimoni, entitats i horaris."},
                {"role": "user", "content": message}
            ],
            max_tokens=250,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"❌ Error en generar la resposta: {e}"

# ----------------------------
# Handler per missatges lliures
# ----------------------------
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    # Primer revisem si hi ha coincidència amb keywords
    for keyword, answer in FAQS.items():
        if keyword in msg:
            await update.message.reply_text(answer)
            return
    # Si no, enviem a GPT
    reply = chat_with_gpt(update.message.text)
    await update.message.reply_text(reply)

# ----------------------------
# Main
# ----------------------------
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Comandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", lambda u,c: send_faq(u,c,"info")))
    app.add_handler(CommandHandler("quevisitar", lambda u,c: send_faq(u,c,"quevisitar")))
    app.add_handler(CommandHandler("gastronomia", lambda u,c: send_faq(u,c,"gastronomia")))
    app.add_handler(CommandHandler("festes", lambda u,c: send_faq(u,c,"festes")))
    app.add_handler(CommandHandler("horaris", lambda u,c: send_faq(u,c,"horaris")))
    app.add_handler(CommandHandler("fira", lambda u,c: send_faq(u,c,"fira")))
    app.add_handler(CommandHandler("entitats", lambda u,c: send_faq(u,c,"entitats")))
    app.add_handler(CommandHandler("espais", lambda u,c: send_faq(u,c,"espais")))
    app.add_handler(CommandHandler("kayaks", lambda u,c: send_faq(u,c,"kayaks")))
    app.add_handler(CommandHandler("parxis", lambda u,c: send_faq(u,c,"parxis")))

    # Missatges lliures
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot en marxa amb GPT (ChatCompletion)...")
    app.run_polling()

if __name__ == "__main__":
    main()
