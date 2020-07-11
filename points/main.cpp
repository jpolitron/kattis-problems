#include <iostream>
using namespace std;

int main()
{
	//draw diagram for this part pf the code diagram 0
	double num1 = 5.23, num2 = 6.74;
	double *p1 = &num1;
	double *p2 = &num2;
	double *p3;
	//draw a seprate digaram for the rest of the code
	p3 = &num2;
	cout << "*p3 = " << *p3 << endl;

	p3 = p1; 
	cout << "*p3 = " << p3 << ", p3 = " << p3 << endl;
	
	*p1 = *p2;
	cout << "*p1 = " << *p1 << ",p1 = " << p1 << endl;
return 0;
}
