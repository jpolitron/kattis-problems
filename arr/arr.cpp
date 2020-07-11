#include <iostream>
using namespace std;
int main(){
int r; 
int n[2][5] = {{5,4,3,2,1},
               {1,2,3,4,5}};

for(int j = 0; j < 2; j++){
	for(int i = 0; i < 4; i++){
		r += n[i]; 
}
cout << "This is the first row " << r << endl;
}
for(int j = 1; j < 2; j++){
	for(int i = 0; i < 4; i++){
		r += n[j];
	}
	cout << "This is the second row " << r << endl;
}
return 0;
}
