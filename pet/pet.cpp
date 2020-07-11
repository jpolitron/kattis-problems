#include <iostream>
using namespace std;
CONST int row = 5;
CONST int col = 4;
int main(){
int c,p;
 int s[row][col];
  cout << "enter elements in array" << endl;
   for(int i = 0; i < row; i++){
	   for(int j = 0; j < col; j++){
		   cin >> s[row][col];
	   }
 }
				
cin >> c;

switch(c){
	case 1:
	for(int j = 0; j < 1; j++){
		for(int i = 0; i < 4;i++){
			p += s[j][i];
		}
	}
	cout << c << " " << p << endl;
	break;
	case 2:
	for(int j = 1; j < 2; j++){
		for(int i = 0; i < 4; i++){
		p += s[j][i];
			}
	}
	cout << c << " " << p << endl;
	break;
	case 3:
	for(int j = 2; j < 3; j++){
		for(int i = 0; i < 4; i++){
		p += s[j][i];
		}
	}
	cout << c << " " << p << endl;
	break;
	case 4:
	for(int j = 3; j < 4; j++){
		for(int i = 0; i < 4; i++){
		p += s[j][i];
			}
	}
	cout << c << " " << p << endl;
	break;
	case 5:
	for(int j = 4; j < 5;j++){
		for(int i = 0; i < 4;i++){
			p += s[j][i];
		
			}
	}
	cout << c << " " << p << endl;
	break;
	default:
	cout << " not a vaild # please try again " << endl;
}
return 0;
}
