#include <iostream>
using namespace std;
int i = 20;
int j = 7;
void trade(int& i, int& j){
	cout << "i is: " << i << endl;
	cout << "j is: " << j << endl;
	swap(i,j);
}
int main(){
trade(i,j);
cout << "i is now: " << i << endl;
cout << "j is now: " << j << endl;
return 0;
}

