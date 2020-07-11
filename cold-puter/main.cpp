#include <iostream>
using namespace std;
int main()
{
	int size, x;
	int counter = 0;
	cin >> size;
	while(size > 0)
	{
		cin >> x;
		if(x < 0)
		{
			counter ++;
		}
		size --;
	}
	cout << counter << endl;
return 0;
}
