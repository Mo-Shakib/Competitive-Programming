#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
    double a, b, c, result;
    cin >> a >> b >> c;

    result = ((a * 2) + (b * 3) + (c * 5)) / 10;

    cout << fixed << setprecision(1) << "MEDIA = " << result << endl;

    return 0;
}
