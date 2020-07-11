#include <iostream>
using namespace std;
int main()
{
	int n,t;
	cin >> n >> t;
	int sum = 0;
	int j;
	for(j = 0; j < n; j++)
	{
		int i;
		cin >> i;
		sum += i;
		if(sum > t)
		{
			break;
		}
	}
	cout << j << endl;

return 0;
}

