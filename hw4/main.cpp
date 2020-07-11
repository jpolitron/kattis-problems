#include "Bus.hpp"
#include <iostream>
#include <string>
using namespace std;

int main()
{
	int choice;
	Bus b1();
	do{
		cout << b1.current_stop() << endl;
		cout << b1.next_stop() << endl;
		cout << "Enter new people" << endl;
		int new_people;
		cin >> new_people;
		b1.passangers_on(new_people);
		cout << "Enter people who got off" << endl;
		int old_people;
		cin >> old_people;
		b1.passangers_off(old_people);
		b1.drive_forward();
		cout << "Would you like to continue yes or no " << endl;
		cin >> choice;
	
	}	
	while(choice != n);
return 0;
}
