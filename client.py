import google.generativeai as genai

api_key = ('SECRET_KEY')
genai.configure(api_key=api_key)

configuracoes = {
    "candidate_count": 1,
    "temperature": 0.5,
}

seguranca = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=configuracoes,
                              safety_settings=seguranca)

chat = model.start_chat(history=[])

prompt = input("\n• Comando: \n")

while prompt != "fim":
    response = chat.send_message(prompt)
    print("\n• Resposta: ", response.text, "\n")
    prompt = input("\n• Comando: \n")