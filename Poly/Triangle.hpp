#ifndef Triangle_hpp
#define Triangle_hpp
#include "Shape.hpp"
#include <iostream>
using namespace std;

class Triangle: public Shape
{
	public:
		Triangle(int a = o, int b = 0):Shape(a,b) {}
		int area()
		{
			cout << "Triangle class area: " << endl;
			return (width * height / 2);
		}
};
#endif
