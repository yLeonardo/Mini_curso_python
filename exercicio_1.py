# Implemente a funcao calcula_media para retornar a media de um aluno:

### defina aqui a funcao calcula_media ###
    
    return media

# Implemente a funcao print_aprovados para imprimir os alunos com media maior ou igual
# a 5, formato de impressao: "alunos[i] - Aprovado com media media[i]", a media deve ser
# impressa com 1 casas decimal:

def print_aprovados(alunos, medias):

    return


alunos = ["Joao", "Maria", "Leonardo", "Ana"]
notas = [[4.3, 7.1, 8.2], [7.0, 2.5, 5.1], [7.6, 9.2, 9.7], [9.5, 6.7, 10.0]]

medias = [0, 0, 0, 0]
for i in range(4):
    medias[i] = calcula_media(notas[i])

print_aprovados(alunos, medias)
