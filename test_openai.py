import os
import sys
import openai

# ----------------------------
# Variables d'entorn
# ----------------------------
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("Python:", sys.version)
print("OpenAI version:", openai.__version__)
print("TELEGRAM_TOKEN:", "✅ Set" if TELEGRAM_TOKEN else "❌ Missing")
print("OPENAI_API_KEY:", "✅ Set" if OPENAI_API_KEY else "❌ Missing")

if not OPENAI_API_KEY:
    print("❌ Falta la variable d'entorn OPENAI_API_KEY")
    exit(1)

openai.api_key = OPENAI_API_KEY

# ----------------------------
# Petita prova ChatCompletion
# ----------------------------
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ets un assistent de prova."},
            {"role": "user", "content": "Hola! Dona'm un missatge curt de 
prova."}
        ],
        max_tokens=50,
        temperature=0.7
    )
    print("✅ ChatCompletion OK!")
    print("Resposta GPT:", 
response['choices'][0]['message']['content'].strip())
except Exception as e:
    print("❌ Error ChatCompletion:", e)

