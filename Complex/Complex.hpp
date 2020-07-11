#ifndef Complex_hpp
#define Complex_hpp

class Complex
{
	public:
		//Default constructor
		Complex();
		//Overloaded constructor
		Complex(int real, int imag);
		//member functions
		void add(Complex other);
		void subtract(Complex other);
		//print function
		void print();
		//accessors
		int getReal();
		int getImag();
	private:
		int real,
		    imag;
};
#endif
