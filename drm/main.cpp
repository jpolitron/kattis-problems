#include <iostream>
#include <string>
using namespace std;
int main() {
  string str1, str2, str3;
  int total1 = 0;
  int total2 = 0;
  cin >> str1; // Taking in the string that is to be put through the three steps
  int counter = 0;
  string alphabet = "ABCDEGHIJKLMNOPQRSTUVWXYZ";
  // 1. Seperating the string into two
  int size = str1.length();
  str2 = str1.substr(0, str1.length()/2);
  str3 = str1.substr(str1.length()/2, str1.length());
  cout << str2 << endl << str3 << endl;
  
  // 2. Moving the letters around 
  for(int i = 0; i < size/2; i++){ // to iterate through string 
  counter = 0;
    for(char A = 'A'; A <= 'Z'; A++){ // to check if string is a certain letter
      if(str2[i] == A)
        total1 = total1 + counter;
      else if(str3[i] == A)
        total2 = total2 + counter;
      counter++; 
    }
  }
  cout << total1;
  cout << endl << total2 << endl;
  total1 = total1 % 26; 
  total2 = total2 % 26;
  cout << total1;
  cout << endl << total2;

  for(int idx = 0; idx < str2.length(); idx++){
    for(int i = 0; i < 26; i++){
      if(str2[idx] == alphabet[i]){
        if(total1 + i > 26)
          str2[idx] = alphabet[i - (26 - total1)]; 
        else
          str2[idx] = alphabet[i + total2];
      }
      else if(str3[idx] == alphabet[i]){
        if(total2 + i > 26)
          str3[idx] = alphabet[i - (26 - total2)]; 
        else
          str3[idx] = alphabet[i + total2];
      }
    }
  }
  cout << str2 << endl << str3 << endl;


  // 3. Merging 
  

  return 0;
}
