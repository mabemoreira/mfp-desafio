def le_nomes():
    with open('0022_names.txt') as arquivo:
        nomes = arquivo.read().replace('"', '').split(',')
    return nomes


def merge(lista, indice_inicio, indice_meio, indice_fim):
    tamanho_esquerda = indice_meio - indice_inicio + 1
    tamanho_direita = indice_fim - indice_meio
    esquerda = [lista[indice_inicio + i] for i in range(tamanho_esquerda)]
    direita = [lista[indice_meio + 1 + i] for i in range(tamanho_direita)]
    i = 0
    j = 0
    k = indice_inicio
    while i < tamanho_esquerda and j < tamanho_direita:
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1
    while i < tamanho_esquerda:
        lista[k] = esquerda[i]
        i += 1
        k += 1
    while j < tamanho_direita:
        lista[k] = direita[j]
        j += 1
        k += 1


def merge_sort(lista, indice_inicio, indice_fim):
    if indice_inicio < indice_fim:
        indice_meio = (indice_inicio + indice_fim) // 2
        merge_sort(lista, indice_inicio, indice_meio)
        merge_sort(lista, indice_meio + 1, indice_fim)
        merge(lista, indice_inicio, indice_meio, indice_fim)

    


def calcula_soma_pontuacao(nomes, letras_valores):
    soma_total = 0
    for indice in range(len(nomes)):
        soma_local = sum(letras_valores[letra] for letra in nomes[indice])
        soma_total += soma_local * (indice + 1)
    return soma_total

def main():
    letras_valores = {letra: valor for valor, letra in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}
    nomes = le_nomes()
    merge_sort(nomes, 0, len(nomes)-1)
    soma_total = calcula_soma_pontuacao(nomes, letras_valores)
    print(soma_total)



if __name__ == '__main__':
    main()