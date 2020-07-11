#include <iostream>
#include <string>

using namespace std;

struct Hero
{
	string name;
	string superpower;
	string heroname;
	string weakness;
	string costume;
	bool ishuman;
};

int main()
{
	Hero Superman;

	Superman.name = "Clark Kent";
	Superman.superpower = "Lazer eyes etc";
	Superman.heroname = "Superman";
	Superman.weakness = "Krypronite";
	Superman.costume = "red, blue, cape, spandex";
	Superman.ishuman = false;

	cout << Superman.name << endl;
	cout << Superman.superpower << endl;
	cout << Superman.heroname << endl;
	cout << Superman.weakness << endl;
	cout << Superman.costume << endl;
	cout << Superman.ishuman << endl;

	Hero Batman;

	Batman.name = "Bruce Wayne";
	Batman.superpower = "I'm Rich";
	Batman.heroname = "Batman";
	Batman.weakness = "His Family";
	Batman.costume = "Black, Grey, Cape";
	Batman.ishuman = true;

	cout << Batman.name << endl;
	cout << Batman.superpower << endl;
	cout << Batman.heroname << endl;
	cout << Batman.weakness << endl;
	cout << Batman.costume << endl;
	cout << Batman.ishuman << endl;

	return 0;
}
