#ifndef Route_hpp
#define Route_hpp
#include <string>
#include <iostream>
using namespace std;
class Route
{
	public:
		string getStop(int index);
		Route();
		Route(int current_position);
	private:
		string stops[5];
		int current_position;

};
#endif
