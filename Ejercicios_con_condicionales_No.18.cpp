//18. Escribir un programa que determine si un número leído desde el teclado es par o impar
#include <iostream>
using namespace std;

int main (){
    char userChoice;
    
    do{

        int num;
        cout << "\nDigite el numero a continuacion: ";
        cin >> num;

        if((num%2) == 0)
        cout <<"El numero " << num << " es par" << endl;
        else
        cout<<"El numero " << num << " es impar" << endl;

        cout << "\nDesea continuar? (s/n): " << endl;
        cin >> userChoice;

    }while (userChoice == 's' || userChoice == 'S');

    return 0;
}