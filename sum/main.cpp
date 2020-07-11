#include <iostream>
#include <math.h>
using namespace std;

int sum_of_squares(k,b,n,i)
{
  int sum = 0;
  int remainder = 0;
  while(n != 0)
  {
    remainder = n % b;
    n = n/b
    sum += pow(remainder,2);
  }
  cout << i+1 << " " << sum << endl;
}
int main()
{
  int lines, line,k,b,n;
  cin >> lines;
  for i in range(lines)
  {
    cin >> line;
    cin >> k >> b >> n;
  }
  sum_of_squares(k,b,n,i);
  return 0;
}
