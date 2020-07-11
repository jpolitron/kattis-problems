#include <iostream>
#include <string>

using namespace std;
string s;
string compress(string s)
{
	string result;
	int counter = 1;
	if(s.length() <= 1)
	{
		return s;
	}
	for(int i = 0; i < s.length()-1; i++)
	{
		if(s[i] == s[i+1])
		{
			counter ++;
		}
		else if(s[i] != s[i+1])
		{
			result += s[i] + to_string(counter);
			counter = 1;
		}
	}
	result += s[s.length()-1] + to_string(counter);
	return result;
}
int main()
{
	cout << "Enter a string" << endl;
	cin >> s;
	cout << compress(s) << endl;
}
