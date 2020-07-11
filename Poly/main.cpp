#include <iostream>
using namespace std; 

int main()
{
	Shape *Shape;
	Rectangle rec(10,7);
	Triangle tri(10,5);

	//store address of the rectangle and call area
	
	shape = &rec;
	shape-> area();

	//store the address of Triangle and call area
	shape = &tri;
	shape->area();

	return 0;
}
