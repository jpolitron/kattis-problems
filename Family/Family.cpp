#include "Family.hpp"

Family::Family()
{
	name = "";
	age = 0;
	weight = 0.00;
	height = 0.00;
}
Family::Family(string name, int age, double weight, double height)
{
	this-> name = name;
	this-> age = age;
	this-> weight = weight;
	this-> height = height;
}
//Mutators 
void Family::set_name(string name)
{
	this-> name = name;
}
void Family::set_age(int age)
{
	this-> age = age;
}
void Family::set_weight(double weight)
{
	this-> weight = weight;
}
void Family::set_height(double height)
{
	this-> height = height;
}
//Accessors 
string Family::get_name()
{
	return name;
}
int Family::get_age()
{
	return age;
}
double Family::get_weight()
{
	return weight;
}
double Family::get_height()
{
	return height;
}
void Family::print(Family object)
{
	cout << "Name : " << object.get_name() << endl;
	cout << "Age : " << object.get_age() << endl;
	cout << "Weight: " << object.get_weight() << endl;
	cout << "Height: " << object.get_height() << endl;
}
