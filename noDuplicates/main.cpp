#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int main()
{
	set<string> str;
	int size;
	string word, s;
	string flag = "yes";
	getline(cin, word);
	size = word.length();

	if(!(size  > 80))
	{
		for(int i = 0; i < size; i++)
		{
			if(!isspace(word[i]))
			{
				s += toupper(word[i]);
			}
			else if(!str.find(s) == str.end())
			{
				str.insert(s);
			}
			else if(str.find(s) != str.end())
			{
				flag = "no";
			}
			else{
				s = "";
			}
		}
		cout << flag << endl;
	}
return 0;
}
