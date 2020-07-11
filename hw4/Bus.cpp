#include "Bus.hpp"
#include <iostream>
#include <string>
using namespace std;
Bus::Bus()
{
	driver = "";
	capacity = 30;
	current_stop = 0;
}
Bus::Bus(string driver, int capacity, int current_stop)
{
	this-> driver = driver;
	this-> capacity = capacity;
	this-> current_stop = current_stop;
}
string Bus::current_stop()
{
	return getStop(current_stop);
}
string Bus::next_stop()
{
	if(current_stop  < 5)
	{
		return getStop(current_stop+1);
	}
	return getStop(0);
}
void Bus::drive_forward()
{
	if(current_stop < 5)
	{
		current_stop++;
	}
	else{
		current_stop = 0;
	}
}
void Bus::passangers_on(int new_people)
{
	if(capacity == 0)
	{
		cout << "no room" << endl;
	}
	else if(capacity - new_people < 0)
	{
	capacity = capacity - (new_people - capacity);
	}
	else{
		capacity -= new_people;
	}
}	
void Bus::passangers_off(int old_people)
{
	capacity += old_people;

}	







