#include "Complex.hpp"
#include <iostream>
using namespace std;

Complex::Complex()
{
	this-> real = 0;
	this-> imag = 0;
}
Complex::Complex(int real ,int imag)
{
	this-> real = real;
	this-> imag = imag;
}
void Complex::add(Complex other)
{
	this-> real += other.real;
	this-> imag += other.imag;
}
void Complex::subtract(Complex other)
{
	this-> real -= other.real;
	this-> imag -= other.imag;
}
void Complex::print()
{
	if(imag < 0)
	{
		cout << real << imag << "i" << endl;
	}
	else{
		cout << real << " + " << imag << "i" << endl;
	}
}
