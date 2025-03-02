# Problema 22 - Names Scores 🧑‍🤝‍🧑

O [enunciado do problema](https://projecteuler.net/problem=22) é o que segue: 

__Using names.txt (_fique tranquila, ele já está nessa pasta como '0022_names.txt'!_), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.__

__For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 5 + 12 + 9 + 14 + 53, is the 
938th name in the list. So, COLIN would obtain a score of 938 X 53 = 49714.__

__What is the total of all the name scores in the file?__
🤔

Para resolver isso, após ler o arquivo, criei um dicionário que relacionava cada letra com seu respectivo valor. Depois disso, ordenei os nomes utilizando o Merge Sort (já que é o sort com menor tempo possível). Por fim, fiz a conta como indicado no enunciado

Ah! Uma última coisa, o código assume que você está rodando diretamente da pasta names-scores. Caso você não faça isso, ocorrerá um erro na hora de ler o arquivo! 🙃

## Fontes 📖

Para a implementação do Merge Sort, me baseei no pseudocódigo capítulo 2.3.1 do CLRS além do [Geeks for Geeks](https://www.geeksforgeeks.org/merge-sort/)


