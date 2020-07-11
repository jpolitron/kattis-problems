#include <string>
#include <iostream>
using namespace std;

int main()
{
	int cases, result, x;
	string last;
	cin >> cases;
	while(cases > 0)
	{
		cin >> x;
		result = x;
		for(int i = 1; i < x; i++)
		{
			result *= 1 * (x - i);
		}
	    last = to_string(result);
		cout << last[last.length()-1] << endl;
		result = 0;
		last = "";
		cases --;
	}
return 0;
}

