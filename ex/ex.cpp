#include <iostream>
using namespace std;
int i = 50;
int j = 60;
void trade(int& i, int& j){
	cout << "i is: " << i << endl;
	cout << "j is: " << j << endl;
	i = j + i;
	j = i -j;
	i = i - j;
}
int main(){
trade(i,j);
cout << "i is now: " << i << endl;
cout << "j is now: " << j << endl;
return 0;
}


