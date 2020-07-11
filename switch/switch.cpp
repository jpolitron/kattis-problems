#include <iostream>
using namespace std;
int main(){
char choice;
int num;
do{
	cout << "enter a num" << endl;
	cin >> num;
	switch(num)
	{
		case 1:
		cout << "ok" << endl;
		break;
		case 2:
		cout << "yee" << endl;
		break;
		default:
		cout << "out of range" << endl;
	}
		cout << "want to try again y - yes" << endl;
		cin >> choice;
}

while(choice == 'y');
	return 0;
}
