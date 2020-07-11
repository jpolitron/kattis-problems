#include <iostream>
using namespace std;

int main()
{

int a = 2;
int inc = -1;

for(int counter = 1; counter <= 6; counter++)
{
	cout << a ;
	a = a + inc;
	inc = inc - 1;
}
}
