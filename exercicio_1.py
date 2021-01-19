def calcula_media(nota):
    # opcao 1:
    total = 0
    for i in nota:
        total += i
    # opcao 2:
    #total = sum(nota)

    # media simples:
    media = total / len(nota)
    return media

# Se media[i] >= 5 imprime "alunos[i] - Aprovado com media media[i]", a media deve ser
# impressa com 1 casas decimais
def print_aprovados(alunos, medias):
    for i in range(len(medias)):
        if(medias[i] >= 5):
            print("{} - Aprovado com media {:.1f}".format(alunos[i], medias[i]))
    return


alunos = ["Joao", "Maria", "Leonardo", "Ana"]
notas = [[4.3, 7.1, 8.2], [7.0, 2.5, 5.1], [7.6, 9.2, 9.7], [9.5, 6.7, 10.0]]

medias = [0, 0, 0, 0]
for i in range(4):
    medias[i] = calcula_media(notas[i])

print_aprovados(alunos, medias)
