/*
Puesdo:
1. take in the number of cases with a for loop
2. take both numbers wit split
3. multiply the two numbers and add them to the total
*/
#include <iomanip>
#include <iostream>
using namespace std;
int main()
{
  int num;
  double x,y,total;
  cin >> num;
  for(int i = 0; i < num; i++)
  {
    cin >> x >> y;
    total += (x * y);
  }
  cout << fixed << showpoint;
  cout << setprecision(3);
  cout << total << endl;
  return 0;
}
