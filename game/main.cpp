// One parent class and two child classes in polymorphism where in this case 
// the children will inherit from the parent and whatever it inherits will be 
// used in a different way each time.
#include <iostream>
using namespace std;

class Enemy
{
	protected:
		int attackPower;
	public:
		void setAttackPower(int a )
		{
			attackPower = a;
		}
};
//ninja class inherits from enemy 
class Ninja: public Enemy
{
	//something specifc only to ninja
	public:
		void attack()
		{cout << "I am a ninja, ninja chop! -" << attackPower << endl;}
};
//child inherits from parent 
class Monster: public Enemy{
	public:
		void attack()
		{cout << "Monster must eat you!!!!!! -" << attackPower << endl;}
};

int main()
{
	Ninja n;
	Monster m;
	//anything an enemy can do a ninja can do 
	Enemy *enemy1 = &n;
	//anything an enemy can do a monster can do 
	Enemy *enemy2 = &m;
	enemy1-> setAttackPower(29);
	enemy2-> setAttackPower(89);
	n.attack();
	m.attack();
	return 0;
}
