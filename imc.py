peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

imc = peso / (altura ** 2)

print(f"\nSeu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc < 25:
    print("Seu peso está na faixa ideal (normal).")
elif imc >= 25 and imc < 30:
    print("Você está com sobrepeso.")
elif imc >= 30 and imc < 35:
    print("Você está com obesidade grau I.")
elif imc >= 35 and imc < 40:
    print("Você está com obesidade grau II (severa).")
else:
    print("Você está com obesidade grau III (mórbida).")