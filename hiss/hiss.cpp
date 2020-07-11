#include <iostream>s
#include <string>
using namespace std;
int main(){
string str;
string flag = "no hiss";
cin >> str;
if (str.length() > 1){
	for(int i = 0; i < str.length()-1; i++){
		if (str[i] == 's' && str[i+1] == 's'){
			flag = "hiss";
		}
	}
}
	cout << flag << endl;
}
