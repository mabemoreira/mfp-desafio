def le_nomes() -> list:
    '''
    Lê o arquivo '0022_names.txt', retira as aspas dos nomes e os coloca em uma lista, que é retornada
    '''
    try:
        with open('0022_names.txt') as arquivo:
            return arquivo.read().replace('"', '').split(',')
    except FileNotFoundError:
        print('Arquivo não encontrado! Você não está rodando do diretório names-scores.')
        return []


def merge(lista: list, indice_inicio: int, indice_meio: int, indice_fim: int) -> None:
    '''
    Junta as sublistas ordenadas do merge sort

    Não retorna, pois é in-place
    '''
    tamanho_esquerda = indice_meio - indice_inicio + 1
    tamanho_direita = indice_fim - indice_meio
    esquerda = lista[indice_inicio:indice_meio + 1] #copiando as sub listas não ordenadas pra não dar problemas na hora da comparação
    direita = lista[indice_meio + 1:indice_fim + 1]

    indice_esquerda = indice_direita = 0
    indice_lista = indice_inicio

    while indice_esquerda < tamanho_esquerda and indice_direita < tamanho_direita: #enquanto nenhuma lista acabar
        if esquerda[indice_esquerda] <= direita[indice_direita]:
            lista[indice_lista] = esquerda[indice_esquerda] #se a esquerda é menor ou igual à direita, ela vai pra lista 
            indice_esquerda += 1
        else:
            lista[indice_lista] = direita[indice_direita] #se a direita é menor, ela vai pra lista
            indice_direita += 1
        indice_lista += 1 #nos dois casos a lista continua

    while indice_esquerda < tamanho_esquerda: #se um lado acabou, mas o outro não, copiamos o que sobrou
        lista[indice_lista] = esquerda[indice_esquerda]
        indice_esquerda += 1
        indice_lista += 1

    while indice_direita < tamanho_direita:
        lista[indice_lista] = direita[indice_direita]
        indice_direita += 1
        indice_lista += 1


def merge_sort(lista: list, indice_inicio: int, indice_fim: int) -> None:
    '''
    Ordena a lista de nomes in-place usando o merge sort
    '''
    #apesar dele ser geralmente usado para números, pela tabela ASCII nada nos impede de usar com letras em palavras
    if indice_inicio < indice_fim:
        indice_meio = (indice_inicio + indice_fim) // 2
        merge_sort(lista, indice_inicio, indice_meio)
        merge_sort(lista, indice_meio + 1, indice_fim)
        merge(lista, indice_inicio, indice_meio, indice_fim)


def calcula_soma_pontuacao(nomes: list, letras_valores: dict) -> int:
    '''
    Calcula a soma total da pontuação dos nomes
    '''
    soma_total = 0
    for indice, nome in enumerate(nomes, start=1):
        pontuacao_nome = sum(letras_valores[letra] for letra in nome)
        soma_total += pontuacao_nome * indice
    return soma_total


def main():
    letras_valores = {letra: valor for valor, letra in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}
    nomes = le_nomes()
    merge_sort(nomes, 0, len(nomes) - 1)
    soma_total = calcula_soma_pontuacao(nomes, letras_valores)
    print(f'Pontuação total dos nomes = {soma_total}')


if __name__ == '__main__':
    main()