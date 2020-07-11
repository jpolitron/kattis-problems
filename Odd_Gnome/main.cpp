#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> king;
	int n,x,temp,size;

	cout << "Enter the size of locations " << endl;
	cin >> n;
	for(int i = 0; i < n; i++)
	{
		cout << "Enter the size of groups " << endl;
		cin >> size;
		cout << "Enter positions " << endl;
		cin >> x;
		for(int i = 0; i < size-1; i++)
		{
			temp = x;
			cin >> x;
			if(temp > x)
			{
				king.push_back(temp);
			}
		}
	}
	for(int i = 0; i < king.size(); i++)
	{
		cout << "The kings location: " << i << endl;
	}
	return 0;
}

