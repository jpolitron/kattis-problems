#include <iostream>
#include <string>
using namespace std;

int main()
{
	string Month;
	int Day;
	cin >> Month;
	cin >> Day;

	if(Month.length() == 3)
	{
		if((Month == "OCT" && Day == 31) || (Month == "DEC"  && Day == 25))
		{
			cout << "yup" << endl;
		}
		else{
			cout << "nope" << endl;
		}
	}
return 0;
}
