import openai

# Substitua 'chave_api' pela sua chave de API real
chave_api = "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"
openai.api_key = chave_api

def enviar_mensagem(mensagem):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você está conversando com um assistente virtual."},
            {"role": "user", "content": mensagem}
        ],
    )
    return resposta["choices"][0]["message"]["content"]

while True:
    texto = input("Escreva sua mensagem: ")
    if texto.lower() == "sair":
        break
    resposta = enviar_mensagem(texto)
    print("Assistente: ", resposta)
    
