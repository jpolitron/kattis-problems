#include "Family.hpp"
#include <iostream>
#include <string>
using namespace std;
int main()
{
	Family f1;
	Family f2;
	Family f3;
	Family f4;
	Family f5;
	Family f6;
	f1.set_name("Humberto Politron");
	f1.set_age(48);
	f1.set_weight(210.00);
	f1.set_height(6.0);

	f1.print(f1);

	f2.set_name("Chava Politron");
	f2.set_age(26);
	f2.set_weight(230.00);
	f2.set_height(6.1);

	f2.print(f2);

	f3.set_name("Jessie Politron");
	f3.set_age(19);
	f3.set_weight(190);
	f3.set_height(5.1);

	f3.print(f3);

	f4.set_name("Angel Politron");
	f4.set_age(12);
	f4.set_weight(130.00);
	f4.set_height(5.7);

	f4.print(f4);

	f5.set_age(21);
	f5.set_weight(125.00);
	f5.set_height(4.11);

	f5.print(f5);

	f6.set_name("Sally");
	f6.set_age(8);
	f6.set_weight(11);
	f5.set_height(2.0);

	f6.print(f6);
	
	return 0;
}
