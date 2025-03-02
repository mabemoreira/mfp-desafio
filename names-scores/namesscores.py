def le_nomes():
    '''
    Lê o arquivo, retira as aspas dos nomes e os coloca na lista nomes
    '''
    with open('0022_names.txt') as arquivo:
        nomes = arquivo.read().replace('"', '').split(',')
    return nomes


def merge(lista, indice_inicio, indice_meio, indice_fim):
    '''
    Junta as sub listas ordenadas do merge sort
    '''
    tamanho_esquerda = indice_meio - indice_inicio + 1 
    tamanho_direita = indice_fim - indice_meio
    esquerda = [lista[indice_inicio + i] for i in range(tamanho_esquerda)] #copiando a sub lista esquerda não ordenada pra não dar problemas na hora da comparação
    direita = [lista[indice_meio + 1 + i] for i in range(tamanho_direita)] #mesma coisa para a sub lista direita
    i = 0 #indice da sub lista esquerda
    j = 0 #indice da sub lista direita
    k = indice_inicio #indice da lista original
    while i < tamanho_esquerda and j < tamanho_direita: #enquanto nenhuma lista acabar
        if esquerda[i] <= direita[j]:
            lista[k] = esquerda[i] #se a esquerda é menor ou igual à direita, ela vai pra lista 
            i += 1 #vamos pra frente na esquerda
        else:
            lista[k] = direita[j] #se a direita é menor, ela vai pra lista
            j += 1 #vamos pra frente na direita
        k += 1 #nos dois casos a lista continua
    while i < tamanho_esquerda: #se a direita acabou, mas a esquerda não, copiamos o resto
        lista[k] = esquerda[i]
        i += 1
        k += 1
    while j < tamanho_direita: #caso igual ao anterior, mas com a direita
        lista[k] = direita[j]
        j += 1
        k += 1


def merge_sort(lista, indice_inicio, indice_fim): 
    '''
    Ordena a lista de nomes in place 
    '''
    #apesar dele ser geralmente usado para números, pela tabela ASCII nada nos impede de usar com letras em palavras
    if indice_inicio < indice_fim:
        indice_meio = (indice_inicio + indice_fim) // 2
        merge_sort(lista, indice_inicio, indice_meio)
        merge_sort(lista, indice_meio + 1, indice_fim)
        merge(lista, indice_inicio, indice_meio, indice_fim)

    
def calcula_soma_pontuacao(nomes, letras_valores):
    '''
    Calcula a soma total da pontuação dos nomes
    '''
    soma_total = 0
    for indice in range(len(nomes)):
        soma_local = sum(letras_valores[letra] for letra in nomes[indice]) #calcula a soma de cada nome
        soma_total += soma_local * (indice + 1) #a lista é 0 indexada, mas as positções começam em 1
    return soma_total

def main():
    letras_valores = {letra: valor for valor, letra in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)} #cria um dicionário com as letras e seus valores
    nomes = le_nomes()
    merge_sort(nomes, 0, len(nomes)-1) 
    soma_total = calcula_soma_pontuacao(nomes, letras_valores)
    print(soma_total)



if __name__ == '__main__':
    main()