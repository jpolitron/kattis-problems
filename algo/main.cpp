#include <iostream>
#include <algorithm>

using namespace std;

int gcd(int a, int b)
{
	if(a == 0)
		return b;
	return gcd(b%a, a);
	}
int main()
{
	int a;
	int b;
	cout << "Enter your first number" << endl;
	cin >> a;
	cout << "Enter your second number" << endl;
	cin >> b;
	cout << "Your greatest common divisor" << endl;
       cout <<	gcd(a, b) << endl;
	return 0;
}

