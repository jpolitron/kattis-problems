#include <iostream>
#include <math.h>
using namespace std;

int main()
{
int r,c;
cin >> r;
cin >> c;
cout.precision(9);
float  total =  ((pow((r-c), 2.0)* 3.14)/((pow(r,2.0)*3.14)))*100;
cout << fixed << total << endl;
return 0;
}
