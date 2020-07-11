#include <iostream>
#include <fstream>
using namespace std;
int main(){
ofstream file;
file.open("example.txt");
string s;
file << "Politron";
cout << s;
file.close();
return 0;
}
