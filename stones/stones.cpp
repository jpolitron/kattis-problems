#include <iostream>
using namespace std;
int main(){
int p;
cin >> p;
if (p % 2 == 0){
	cout << "Bob" << endl;
}
	else if (p % 2 == 1){
		cout << "Alice" << endl;
	}
	else{
		cout << "error" << endl;
	}
	return 0;
}
