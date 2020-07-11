#include <iostream>
using namespace std;

int main()
{
	int og[6];
	int n;
	og[0] = 1;
	og[1] = 1;
	og[2] = 2;
	og[3] = 2;
	og[4] = 2;
	og[5] = 8;
	for(int i = 0; i < 6; i++)
	{
		cin >> n;
		cout << og[i]  - n << " ";
	}
	cout << endl;
}
