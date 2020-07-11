#ifndef Bus_hpp
#define Bus_hpp
#include "Route.hpp"
#include <string>
#include <iostream>
using namespace std;
class Bus
{
	public:
		Bus();
		Bus(string driver, int capacity, int current_stop);
		string current_stop();
		string next_stop();
		
	private:
		Route r1;
		string driver;
		int capacity;
		int current_stop;
		int passanger;
};
#endif
