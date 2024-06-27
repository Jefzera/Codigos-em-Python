import random

nove_digitos = ""

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_com_digito = f'{nove_digitos}{digito_1}{digito_2}'

cpf_formato = f'{cpf_com_digito[:3]}.{cpf_com_digito[3:6]}.{cpf_com_digito[6:9]}-{cpf_com_digito[9:]}'

print(f"O CPF Gerado é: {cpf_formato}")