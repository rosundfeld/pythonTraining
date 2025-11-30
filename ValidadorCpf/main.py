from cpf_validator import cpf_check

def main():
    cpf = input("Digite o CPF para validação: ")
    resultado = cpf_check(cpf)
    print(resultado)

main()