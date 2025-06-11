# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):

    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro == "sim"
    afinidade_animais = afinidade_animais == "sim"

    # Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
      return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    if intensidade >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and not afinidade_animais:
      return "A afinidade elemental do feiticeiro é com o elemento Água!"
    if intensidade >= 7 and fase_lunar == "cheia" and idade_feiticeiro <= 100 and componente_raro and afinidade_animais:
      return "A afinidade elemental do feiticeiro é com o elemento Terra!"
  
    return "A afinidade elemental do feiticeiro é com o elemento Ar!"

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input().lower()
fase_lunar_feitico = input().lower()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input().lower()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)