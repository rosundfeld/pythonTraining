def cpf_check(cpf):
    valid_cpf = convert_number(cpf)
    if valid_cpf is None:
        return "CPF deve ser apenas números."
    if len(str(cpf)) != 11:
        return "CPF deve ter 11 dígitos."
    if (check_sum(valid_cpf) == False or check_last_digits(valid_cpf) == False):
        return "CPF inválido."
    return "CPF válido."


def check_sum(cpf):
    total = sum(int(digit) for digit in str(cpf))
    digits = ''.join(char for char in str(total) if char.isdigit())
    if (digits[0] == digits[1]):
        return True
    else:
        return False


def check_last_digits(cpf):
    str_cpf = str(cpf)
    first_nine_digits = str_cpf[:9]
    first_check_digit = calculate_check_digit(first_nine_digits)
    second_check_digit = calculate_check_digit(
        first_nine_digits + str(first_check_digit))
    return str_cpf[-2:] == f"{first_check_digit}{second_check_digit}"


def calculate_check_digit(digits):
    sum_total = 0
    for index, digit in enumerate(digits):
        sum_total += int(digit) * (len(digits) + 1 - index)
    remainder = sum_total % 11
    if remainder < 2:
        return 0
    else:
        return 11 - remainder


def convert_number(valor):
    try:
        numero = int(valor)
        return numero
    except (ValueError, TypeError):
        return None
