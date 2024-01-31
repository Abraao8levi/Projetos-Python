# Automação de tarefas e organização de dados

# Desafio:

# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a
# quantidade de produtos compradas e o preço médio dos produtos.
# E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
# Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema

# para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado


import pandas as pd
import pyautogui
import pyperclip

def open_chrome():
    pyautogui.hotkey("win")
    pyautogui.write("Chrome")
    pyautogui.hotkey("enter")

def go_to_website(website):
    pyautogui.write(website)
    pyautogui.press("enter")

def login(username, password):
    pyautogui.click(796,380)
    pyautogui.write(username)
    pyautogui.hotkey("tab")
    pyautogui.write(password)
    pyautogui.hotkey("tab")
    pyautogui.hotkey("enter")

def download_data():
    pyautogui.click(492,358)
    pyautogui.click(534,777)

def calculate_indicators(file_path):
    tabela = pd.read_csv(file_path, sep=";")
    total_gasto = tabela["ValorFinal"].sum()
    quantidade = tabela["Quantidade"].sum()
    preco_medio = total_gasto / quantidade
    return total_gasto, quantidade, preco_medio

def send_email(email, subject, message):
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
    pyautogui.press("enter")
    pyautogui.click(95, 204)
    pyautogui.write(email)
    pyautogui.hotkey("enter")
    pyautogui.hotkey("tab")
    pyperclip.copy(subject)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("ctrl", "enter")

if __name__ == "__main__":
    open_chrome()
    go_to_website("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
    login("usuário", "senha123")
    download_data()
    total_gasto, quantidade, preco_medio = calculate_indicators(r"C:\Users\Abraao\Downloads\Compras.csv")
    texto = f"""
    Prezados,
    Segue o relatório de compras

    Total Gasto: R${total_gasto:,.2f}
    Quantidade de Produtos: {quantidade:,}
    Preço Médio: R${preco_medio:,.2f}

    Qualquer dúvida, é só falar.
    Att.,Abraão Levi
    """
    send_email("pythonimpressionador@gmail.com", "Relatório de Vendas", texto)
