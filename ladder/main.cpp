#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double length, angle;
	cin >> length;
	cin >> angle;
	int result =  (length/ sin(angle * M_PI/ 180)) + 1;
	cout << result << endl;
return 0;
}
