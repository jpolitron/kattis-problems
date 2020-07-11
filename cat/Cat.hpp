#ifndef Cat_hpp
#define Cat_hpp
#include <string>
using namespace std;

class Cat
{
	public:
		//CONSTRUCTORS
		Cat();
		Cat(string name, string color, int age, char gender);

		//MUTATORS
		void setname(string name);
		void setcolor(string color);
		void setage(int age);
		void setgender(char gender);

		//ACCESSORS
		string getname();
		string getcolor();
	       	int getage();
		char getgender();
		void print();
	private:
		string name,color;
		int age;
		char gender;

};
#endif
