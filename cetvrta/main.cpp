/*
Puesdo:
1. take in x's and y's.
2. then pass through function
3. have it check if the first and second are the same if so return 3rd.
4. have it check 2nd and 3rd then return 1st
5. all fails return the second
*/
#include <iostream>
using namespace std;

int points(int a, int b, int c)
{
  if(a == b)
  {
    return c;
  }
  else if(b == c)
  {
    return a;
  }
  else{
    return b;
  }
}
int main()
{
  int x1,y1,x2,y2,x3,y3;
  cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
  cout << points(x1,x2,x3) << " " << points(y1,y2,y3) << endl;
}
