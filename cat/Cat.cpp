#include "Cat.hpp"
#include <iostream>
#include <string>
using namespace std;
Cat::Cat()
{
	name = "Kelly";
	color = "Black";
	age = 12;
	gender = 'F';
}
Cat::Cat(string name, string color, int age, char gender)
{
	this -> name = name; 
	this -> color = color;
	this -> age = age;
	this -> gender = gender;
}
void Cat::setname(string name)
{
	this-> name = name;
}
string Cat::getname()
{
	return name;
}
void Cat::setcolor(string color)
{
	this-> color = color;
}
string Cat::getcolor()
{
	return color;
}
void Cat::setage(int age)
{
	this-> age = age;
}
int Cat::getage()
{
	return age;
}
void Cat::setgender(char gender)
{
	this-> gender = gender;
}
char Cat::getgender()
{
	return gender;
}
void Cat::print()
{
	cout << "Your pets are: " << name << "/n" << color << "/n" << age << "/n" << gender << endl;
}
