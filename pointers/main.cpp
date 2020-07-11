#include <iostream>

using namespace std;

int main(){
	
	// simple integer example
	// normal int declaration of variable x
	int x;
	cout << "initial value of x: " << x << endl;
	// int x rassignment to value of 24
	x = 24;
	cout << "value of x after reassignment: " << x << endl;
	// the & next to a variable name returns a reference to the address of the variable. In this case x.
	cout << "address of x: "<< &x << endl;
	
	// read from rigth to left
	// a pointer named ptr that *points to and int variable
	int *ptr;
	cout << "initial address of ptr: " << ptr << endl;
	 // assign ptr to address of x
	ptr = &x;
	cout << "address of ptr after assigment: " << ptr << endl;	
	cout << "value of ptr when we dereference: " << *ptr << endl;
	cout << endl;
	cout << "End of pointers example. LMK if you want more!" << endl;
	
	return 0;
}
