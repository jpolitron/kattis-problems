#include <iostream>
#include <string> 
#include <unordered_set> 
using namespace std; 

int main() {
  unordered_set<string> used;
  int x; 
  cin >> x; 
  string temp;
  string previous; 
  cin >> previous; 
  used.insert(previous); 
  for(int i = 2; i <= x; i++){
    cin >> temp; 
    if(temp[0] != previous[previous.length()-1] || used.count(temp) == 1){
      if(i % 2 == 0){
         cout << "Player 2 lost" << endl; 
         return 0; 
      }
      else if(i % 2 == 1){
        cout << "Player 1 lost" << endl;
        return 0;
      }
    }
      used.insert(temp);
      previous = temp;
    }
      cout << "Fair Game" << endl;

  return 0; 
}
