#include <iostream>
using namespace std;

int excel(string letter)
{
	int result = 0;
	for(int i = 0; i < letter.length(); i++)
	{
		result *= 26;
		result += letter[i] - 'A' + 1;
	}
	return result;
}
int main()
{
	cout << excel("A") << endl;
	cout << excel("BB") << endl;
}
