/*
Puesdo:
1. take in hands and trump.
2. take in # and suit while the user keeps inputing numbers.
3. check suit with trump.
4. if it checks out add it to sum using the suit function with the #.
5. else do the same but with the value function.
6. return the sum.
*/
#include <iostream>
using namespace std;

int getValue(char c)
{
  switch(c)
  {
    case 'A':
      return 11;
    case 'K':
      return 4;
    case 'Q':
      return 3;
    case 'J':
      return 20;
    case 'T':
      return 10;
    case '9':
      return 14;
    default:
      return 0;
  }
  return 0;
}

int getSuit(char c)
{
  switch(c)
  {
    case 'A':
      return 11;
    case 'K':
      return 4;
    case 'Q':
      return 3;
    case 'J':
      return 2;
    case 'T':
      return 10;
    default:
      return 0;
    }
    return 0;
}

int main()
{
  int hand;
  char trump;
  cin >> hand >> trump;
  int limit = hand*4;
  char number,suit;
  int sum = 0;
  while(limit != 0)
  {
    cin >> number >> suit;
    limit --;
    if(suit == trump)
    {
      sum += getValue(number);
    }
    else
    {
      sum += getSuit(number);
    }
  }
  cout << sum << endl;
  return 0;
}
