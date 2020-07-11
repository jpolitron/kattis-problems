#include "Complex.hpp"

int main()
{
	Complex x(8,9);
	Complex y(1,3);

	x.print();
	y.print();

	x.add(y);

	x.print();

	return 0;
}
