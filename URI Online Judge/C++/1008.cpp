#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    int number, hour;
    double amount, salary;
    cin >> number >> hour >> amount;
    salary = hour * amount;
    cout << "NUMBER = " << number << endl;
    std:: cout << "SALARY = U$ " << fixed << setprecision(2) << salary << endl;
    return 0;
}
