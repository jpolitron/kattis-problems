#ifndef Family_hpp
#define Family_hpp
#include <iostream>
#include <string>
using namespace std;

class Family
{
        public:
                //Consturctors 
		Family();
                Family(string name, int age, double weight, double height);

                //Accessors 
                void set_name(string name);
                void set_age(int age);
                void set_weight(double weight);
                void set_height(double height);

                //Mutators
                string get_name();
                int get_age();
                double get_weight();
                double get_height();

                void print(Family object);

        private:
                string name;
                int age;
                double weight, height;

};
#endif
                            
