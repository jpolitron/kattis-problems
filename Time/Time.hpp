#ifndef Time_hpp
#define Time_hpp
#include <iostream>

using namespace std;

class Time
{
	public:
		Time();
		Time(int hr, int min, int sec);
		friend ostream& operator << (ostream& out, const Time& t);
		//overload the insertion operator
		//postcondition: returns the time in the form: hh:mm:ss
		friend bool operator ==(const Time& tL, const Time& tR);
		//overload the equailty operator
		//is equal to the time on the right side, otherwise, it returns false
		friend Time operator +(const Time& tL, const Time& tR);
		//overload the addition operator
		//postcondition: returns an on object of type Time with
		//the sum of the time on the left side and right side
		Time& operator +=(const Time& tR);
		//overload the additon assignment operator 
		//postcondition: adds the time of the left and right object and
		//stores the result in the left operand returns a reference to the 
		//modified time object
		Time& operator ++();
		//overload the prefix increment operator
		//postcondition: the time is incremented by one second 
	private:
		int hr;
		int min;
		int sec;
};
#endif
