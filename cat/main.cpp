#include <iostream>
#include "Cat.hpp"

using namespace std;

int main()
{
	Cat c1;

	c1.getname();
	c1.getcolor();
	c1.getage();
	c1.getgender();

	c1.setname(name);
	c1.setcolor(color);
	c1.setage(age);
	c1.setgender(gender);

	c1.print();

return 0;
}
