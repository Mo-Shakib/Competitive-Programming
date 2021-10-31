#include <iostream>
using namespace std;
int
main ()
{
  int i, rangenumber, num = 1, c = 0, letest = 0;
  cout<<"Enter the Nth value:";
  cin>>rangenumber;

  while (c != rangenumber)
    {
      int num1=num;
      int num2=0;
      //reverse of number
    while(num1!=0)
    {
        int rem=num1%10;
        num1/=10;
        num2=num2*10+rem;
    }
    if(num==num2)
      {
          c++;
          letest=num;
      }
      num = num + 1;
    }
  cout<<rangenumber<<"th palindrome number is "<<letest;
  return 0;
}