#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp> // para lidar com inteiros grandes demais para caber em unsigned long long
using namespace std;
using namespace boost::multiprecision; // para não ficar escrevendo o nome da lib frequentemente, igual com std

cpp_int binpow(cpp_int base, cpp_int expoente){
    cpp_int resposta = 1;
    while(expoente > 0){
        if(expoente & 1 == 1)
            resposta *= base;
        base *= base;
        expoente >>= 1;
    }
    return resposta;
}

cpp_int soma_digitos(cpp_int potencia){ 
    // soma os dígitos de qualquer cpp_int
    cpp_int soma = 0;
    // sabemos que o último dígito de um número é o resto da divisão dele por 10
    while(potencia > 0){
        soma += potencia % 10;
        potencia /= 10;
    }
    return soma;
}

int main(){
    cpp_int potencia = binpow(2,1000);
    cpp_int resposta = soma_digitos(potencia);
    cout << resposta << endl;
    return 0;
}