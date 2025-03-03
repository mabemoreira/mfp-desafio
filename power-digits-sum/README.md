# Problema 16 - Power Digits Sum *️⃣ *️⃣ ➕

O [enunciado do problema](https://projecteuler.net/problem=16) é o que segue:

__" \(2^{15} = 32768\) and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.__

__What is the sum of the digits of the number \(2^{1000}\)"?__

Fica claro que a real dificuldade do problema é computar um número tão grande. Graças à ICPC Summer School, eu fui introduzida a um algoritmo que consegue fazer isso relativamente rápido: o binpow. Ele funciona interpretando o expoente como um número binário para diminuir o número de multiplicações

Contudo, o número em questão é tão grande que mesmo um unsigned long long não é grande o suficiente para guardá-lo. Sendo assim, pesquisei e encontrei uma biblioteca para CPP que resolve esse problema: __boost multiprecision__, que tem o cpp_int, que consegue guardar um número grande assim.

## Baixando a biblioteca e configurando o VScode 🖥️

Esse tutorial supõe uma máquina Linux com bash, contudo, é possível adaptá-lo para Windows ou MacOs, mudando apenas como baixar e extrair o arquivo. 

Primeiro, baixe o arquivo .tar.gz [aqui](https://www.boost.org/users/download/)

Para extrair o arquivo, rode isso na pasta em que você baixou o arquivo(no momento a versão atual é 1_87_0):
```console 
sudo tar -xzf boost_1_87_0.tar.gz -C /usr/local/boost --strip-components=1
```
Isso irá extraí-lo em /usr/local/boost. _Se você não quer debugar o programa e apenas quer rodá-lo, vá para a seção **Rodando o programa**_

Agora, vá para o VScode na pasta mfp-desafio (ou power-digits-sum) e aperte ```CTRL + Shift + p```. Procure por ```C/C++: Edit Configurations (UI)``` Vá para __Include path__ e adicione o caminho __/usr/local/boost__

Após isso, ele deve estar conectado. Se quiser ter certeza, vá até o seu ```c_cpp_properties.json``` na pasta .vscode e veja se ele está assim: 

```json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [
                "${workspaceFolder}/**",
                "/usr/local/boost"
            ],
            ...
```
Se o JSON estiver assim, não tem problema se o VScode reclamar sobre não encontrar o import, você só precisa rodar direto do terminal (incluindo o terminal interno do VScode!)

## Rodando o programa 💻

Note que este diretório possui um arquivo Makefile, logo, para compilar o programa faça simplesmente, **dentro do diretório power-digits-sum**

```bash
make
```
Agora, para rodá-lo, faça:

```bash
make run
```
Pronto! O programa deve imprimir a soma de todos os algarismos de \(2^{1000}\), ou seja, 1366

## Fontes 📖
[CP algorithms](https://cp-algorithms.com/algebra/binary-exp.html) para a implementação do Binpow. [Documentação do Boost Multiprecision](https://www.boost.org/doc/libs/1_86_0/libs/multiprecision/doc/html/index.html). Também utilizei o Deep Seek __SOMENTE__ para me auxiliar com o processo de baixar a biblioteca 
