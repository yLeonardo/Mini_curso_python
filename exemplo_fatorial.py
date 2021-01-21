def fatorial(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return n * fatorial(n - 1)


numero = int(input("Digite o numero que deseja obter o fatorial: "))

resultado = fatorial(numero)

print("O fatorial de {}! é {}".format(numero, resultado))

