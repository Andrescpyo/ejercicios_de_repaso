/*Escribir un programa que dado un número del 1 a 7 escriba el correspondiente nombre del
día de la semana.*/
#include <iostream>
using namespace std;

int main(){
    int dia;
    cout << "Dia: "; cin >> dia;

    switch (dia){
        case 1: cout << "Lunes"<< endl; break;
        case 2: cout << "Martes"<<endl; break;
        case 3: cout << "Miercoles"<<endl; break;
        case 4: cout << "Jueves"<<endl; break;
        case 5: cout << "Viernes"<<endl; break;
        case 6: cout << "Sabado"<<endl; break;
        case 7: cout << "Domingo"<<endl; break;
        default: cout <<"El número digitado es inválido"; break;
        }

        return 0;
}


    

