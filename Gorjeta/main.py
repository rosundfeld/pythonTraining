from calcular_gorjeta import receber
from convert_number import convert_number

def pedir_numero(prompt, default=None):
    while True:
        entrada = input(prompt)
        if entrada == "" and default is not None:
            return default
        numero = convert_number(entrada)
        if numero is not None:
            return numero
        print("Entrada inválida. Por favor, insira um número válido.")

valor = convert_number(input("Digite o valor da conta: R$ "))
gorjeta = convert_number(input("Digite a porcentagem da gorjeta (padrão 10%): ") or 10)
valores = receber(valor, gorjeta)

if valores:
    total = valores['total']
    gorjeta_valor = valores['gorjeta']
    print(f"Valor da gorjeta: R$ {gorjeta_valor:.2f}")
    print(f"Valor total com gorjeta: R$ {total:.2f}")
else:
    print("Erro: Verifique se o valor digitado está correto.")
