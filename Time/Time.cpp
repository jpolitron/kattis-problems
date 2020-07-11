#include "Time.hpp"
Time::Time()
{
	hr = 0;
	min = 0;
	sec = 0;
}
Time::Time(int hr, int min, int sec)
{
	this->hr = hr;
	this->min = min;
	this->sec = sec;
}
ostream& operator << (ostream& out, const Time& t)
{
	if(hr < 10)
	{
		out << "0";
		out << hr << ":";
	}
	if(min < 10)
	{
		out << "0";
		out << min << ":";
	}
	if(sec < 10)
	{
		out << "0";
		out << sec;
	}
	return out;
}
bool operator ==(const Time& tL, const Time& tR)
{
	return tL.hr == tR.hr && tL.min == tR.min && tL.sec == tR.sec;
}
Time operator +(const Time& tL, const Time& tR)
{
	int new_hour = tL.hr + tR.hr;
	int new_min = tL.min + tR.min;
	int new_sec + tL.sec + tR.sec;

	if(new_hour >= 60)
	{
		new_sec = new_sec % 60;
		min ++;
	}
	if(new_min >= 60)
	{
		new_min = new_min % 60;
		hr ++;
	}
	if(new_hour >= 24)
	{
		new_hour = new_hour % 12;
	}
}

