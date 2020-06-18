#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
    string name;
    double fixed_salary, seles, bonus, final_salary;
    getline(cin, name);
    cin >> fixed_salary >> seles;
    bonus = (seles * 15)/ 100;
    final_salary = fixed_salary + bonus;
    std:: cout << "TOTAL = R$ " << fixed << setprecision(2) << final_salary << endl;
    return 0;
}
