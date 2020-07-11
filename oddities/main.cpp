#include <iostream>

using namespace std;

int main()
{
	int size;
	int x;
	cin >> size;

	for(int i = 0; i < size; i++)
	{
		cin >> x;
		if(x % 2 == 0)
		{
			cout << x << " is even" << endl;
		}
		else{
			cout << x << " is odd" << endl;
		}
	}
	return 0;
}


