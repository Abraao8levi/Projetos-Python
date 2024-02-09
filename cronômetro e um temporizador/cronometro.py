import time

def formatar_tempo(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f"{horas} horas, {minutos} minutos e {segundos} segundos"

def converter_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

def iniciar_cronometro():
    print("Cronômetro iniciado")
    start_time = time.time()

    # Faça algo aqui
    input("Pressione Enter para parar o cronômetro...")

    elapsed_time = time.time() - start_time
    print(f"Tempo decorrido: {formatar_tempo(int(elapsed_time))}")

def iniciar_temporizador():
    horas = int(input("Digite as horas do temporizador: "))
    minutos = int(input("Digite os minutos do temporizador: "))
    segundos = int(input("Digite os segundos do temporizador: "))
    countdown = converter_para_segundos(horas, minutos, segundos)

    print(f"Temporizador iniciado para {formatar_tempo(countdown)}")
    for i in range(countdown, 0, -1):
        print(f"Restam {formatar_tempo(i)}")
        time.sleep(1)
    print("Tempo esgotado!")

while True:
    print("\n1. Iniciar Cronômetro")
    print("2. Iniciar Temporizador")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        iniciar_cronometro()
    elif opcao == 2:
        iniciar_temporizador()
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")
