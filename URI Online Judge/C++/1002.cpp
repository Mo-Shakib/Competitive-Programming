#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double r, pi, result;
    pi = 3.14159;
    cin >> r;
    result = pi * (r * r);
    std:: cout << "A=" << fixed << setprecision(4) << result << endl;

    return 0;
}