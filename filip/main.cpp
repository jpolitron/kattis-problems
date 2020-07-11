#include <iostream>
#include <string>

using namespace std;
int main()
{
	string n, n2;
	cin >> n;
	cin >> n2;

	swap(n[0], n[n.length()-1]);
	swap(n2[0], n2[n2.length()-1]);

	int finaln = stoi(n);
	int finaln2 = stoi(n2);

	if(finaln < finaln2)
	{
		cout << finaln2 << endl;
	}
	else{
		cout << finaln << endl;
	}
	return 0;
}
