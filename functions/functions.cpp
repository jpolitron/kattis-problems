#include <iostream>
using namespace std;
int i = 6;
int j = 7;
void print(int i, int& j){
	i+=1;
	cout <<"i is now "<< i + 11 << endl;
	cout <<" j is now "<< j << endl;
	j += 15;
}
int main(){
print(i,j);
cout << "j:  "<< j << endl;
cout << "i: "<< i << endl;
return 0;
}
