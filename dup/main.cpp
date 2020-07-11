#include <iostream>
#include <string>
using namespace std;

bool duplicate(string s)
{
  bool flag = false;
  char target;
  if(s.length() >= 2)
  {
    for(int i = 0; i < s.length()-1; i++)
    {
      target = s[i];
      if (tolower(target == s[i+1]))
      {
        flag = true;
      }
      else{
        flag = false;
      }
    }
  }
  return flag;
}

int main()
{
   cin >> s;
  duplicate(s);
  return 0;
}
