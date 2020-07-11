#include <iostream>
using namespace std;
int main()
{
	int cases,mph,time,s;
	int change = 0;
	cin >> cases;
	while(cases != -1)
	{
		for(int i = 0; i < cases; i++)
		{
			cin >> mph >> time;
			change = abs(change - time);
			s = mph * change;
			cout << s << " miles" << endl;
		}
		cin >> cases;
		cout << s << " miles" << endl;
	}
	return 0;
}
