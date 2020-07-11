#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int n;
	cin >> n;
	string flag = "False";
	if(n > 0)
	{
		if(pow(n,(1/3)))
		{
			flag = "True";
		}
		cout << flag << endl;
	}
return 0;
}
