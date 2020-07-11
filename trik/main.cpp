#include <iostream>
#include <vector>
using namespace std;

int main()
{

	string cups = "DOO";
	string s;
	cin >> s;
	for(int i = 0; i < s.length(); i++)
	{
		if(toupper(s[i] == 'A'))
		{
			swap(cups[0], cups[1]);
		}
		else if(toupper(s[i] == 'B'))
		{
			swap(cups[1],cups[2]);
		}
		else{
			swap(cups[0], cups[2]);
		}
	}
	cout << cups.find('D')+1  << endl;
	return 0;
}

