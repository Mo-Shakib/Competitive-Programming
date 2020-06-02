#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    double a, b, result;
    cin >> a >> b;

    result = ((a * 3.5) + (b * 7.5)) / 11;

    cout << fixed << setprecision(5) << "MEDIA = " << result << endl;

    return 0;
}
