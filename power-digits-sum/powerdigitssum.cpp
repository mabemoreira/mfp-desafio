#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp> // para lidar com inteiros grandes demais para caber em unsigned long long
using namespace std;
using namespace boost::multiprecision; // para não ficar escrevendo o nome da lib frequentemente, igual com std

cpp_int binpow(cpp_int base, cpp_int expoente){ 
    //calcula base^expoente de maneira mais rápida, já que é baseado na representação binária do expoente
    cpp_int resposta = 1; // qualquer número elevado a 0 é 1, então sabemos que nossa resposta é no mínimo isso
    while(expoente > 0){
        if(expoente & 1) // se o último bit do expoente é 1, o expoente é ímpar
            resposta *= base; 
        base *= base; // base ^2 nos leva aos expoentes pares
        expoente >>= 1; // divide por 2 para verificar o próximo bit
    }
    return resposta;
}

cpp_int soma_digitos(cpp_int potencia){ 
    // soma os dígitos de qualquer cpp_int
    cpp_int soma = 0;
    // sabemos que o último dígito de um número é o resto da divisão dele por 10
    while(potencia > 0){
        soma += potencia % 10; //somo o último dígito
        potencia /= 10; // faço a divisão inteira, substituindo o último dígito pelo penúltimo até chegar em 0
    }
    return soma;
}

int main(){
    cpp_int potencia = binpow(2,1000);
    cpp_int resposta = soma_digitos(potencia);
    cout<<"soma dos dígitos de 2^1000 = "<<resposta<<endl;
    return 0;
}