#ifndef Rectangle_hpp
#define Rectangle_hpp
#include "Shape.hpp"
#include <iostream>
using namespace std;

class Rectangle : public Shape
{
	public:
		Rectangle(int a = 0, int b = 0):Shape(a,b) {}
		int area()
		{
			cout << "Rectangle class area: " << endl;
			return (width * height);
		}
};
#endif
