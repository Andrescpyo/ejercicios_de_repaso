//12. Escribir un programa que calcule el número de horas, minutos y segundos que hay en un valor x de segundos indicados por el usuario

#include <iostream>
using namespace std;

int main() {
    char userChoice;

    do {
        int num;
        cout << "\nDigite el numero de segundos: ";
        cin >> num;

        int hours = num / 3600;
        int minutes = (num % 3600) / 60;
        int seconds = num % 60;

        cout << hours << " houras, " << minutes << " minutos, y " << seconds << " segundos." << endl;

        cout << "Desea continuar? (s/n): " << endl;
        cin >> userChoice;
    } while (userChoice == 's' || userChoice == 'S');

    return 0;
}