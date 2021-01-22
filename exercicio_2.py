### Implemente a função calcula_fibonacci aqui! ###

# Função main - Não alterar! #
if __name__ == "__main__":
    numero = int(input("Digite o numero que deseja calcular o Fibonacci: "))

    resultado = calcula_fibonacci(numero-1)

    print("O fibonacci de {} é {}".format(numero, resultado))

