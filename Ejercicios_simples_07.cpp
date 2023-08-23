/* Escribir un programa que calcule el volumen de una esfera de radio = r
volumen de la esfera = 4/3 * PI * radio3 */
#include <iostream>
#include <cmath>
using namespace std;

int main(){

    float radio, volumen_esfera=0;
    const double pi= 3.14159265358979323846;

    cout << "Ingrese el valor del Radio: "; cin >> radio ;
    
    //Calcular el volumen de la Esfera
    volumen_esfera = ((4*pi)/3)*(pow(radio,3));

    //Imprimir los resultados
    cout << "El volumen de la esfera es: "<< volumen_esfera;

    return 0;
}

