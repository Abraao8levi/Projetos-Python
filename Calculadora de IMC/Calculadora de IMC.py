
def calculate_imc(weight: float, height: float) -> float:
    return weight / (height ** 2)

weight = float(input("Digite o seu peso em kg: "))
height = float(input("Digite a sua altura em metros: "))

imc = calculate_imc(weight, height)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}, o que indica que você está abaixo do peso.")
elif imc < 25:
    print(f"Seu IMC é {imc:.2f}, o que indica que você está com um peso saudável.")
elif imc < 30:
    print(f"Seu IMC é {imc:.2f}, o que indica que você está com sobrepeso.")
else:
    print(f"Seu IMC é {imc:.2f}, o que indica que você está obeso.")
