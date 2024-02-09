import requests
import locale

def converter_moeda(valor, moeda_origem, moeda_destino, chave_api):
    url = f"https://v6.exchangerate-api.com/v6/{chave_api}/latest/{moeda_origem}"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        return None, None
    except requests.exceptions.RequestException as req_err:
        print(f"Erro de requisição: {req_err}")
        return None, None

    dados = resposta.json()

    if 'conversion_rates' in dados and moeda_destino in dados['conversion_rates']:
        taxa_cambio = dados['conversion_rates'][moeda_destino]
        valor_convertido = valor * taxa_cambio
        return valor_convertido, taxa_cambio
    else:
        print(f"Não foi possível encontrar a taxa de câmbio para {moeda_destino}.")
        return None, None

def main():
    chave_api = '2b48a26debc43edb2eeeab43'
    
    try:
        valor = float(input("Digite o valor que você deseja converter: "))
        if valor <= 0:
            raise ValueError("O valor deve ser um número positivo.")
        
        moeda_origem = input("Digite a moeda de origem (por exemplo, 'BRL'): ").upper()
        moeda_destino = input("Digite a moeda de destino (por exemplo, 'USD'): ").upper()
        
        if len(moeda_origem) != 3 or len(moeda_destino) != 3:
            raise ValueError("Código de moeda inválido. Use três letras, por exemplo, 'USD'.")

    except ValueError as value_err:
        print(f"Erro: {value_err}")
        return

    valor_convertido, taxa_cambio = converter_moeda(valor, moeda_origem, moeda_destino, chave_api)

    if valor_convertido is not None:
        locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
        valor_formatado = locale.currency(valor_convertido, grouping=True)
        print(f"{locale.format_string('%.2f', valor)} {moeda_origem} é igual a {valor_formatado} {moeda_destino} com uma taxa de câmbio de {taxa_cambio:.4f}.")

if __name__ == "__main__":
    main()
