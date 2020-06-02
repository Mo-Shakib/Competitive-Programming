#include <iostream>

using namespace std;

int main()
{
int steps;
int ctr;
int flag=1;
int output=0;
cin>>steps;
if(steps<5){
    cout<<1;
}
else {
    if(steps%5==0)
        {
output=steps/5;
cout<<output;
}
else if(steps>5&&steps%5!=0){
output=(steps/5)+1;
cout<<output;
    }

    }
}