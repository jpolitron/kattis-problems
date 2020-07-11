//
//  main.cpp
//  template
//
//  Created by Jessie Politron on 10/23/19.
//  Copyright © 2019 Jessie Politron. All rights reserved.
//

#include <cstdlib> //provides exit_success
#include <iostream> //provides cout
#include <string> //string class
using namespace std;

template <class Item>
Item maximal(Item a, Item b)
{
    if(a > b)
        return a;
    else
        return b;
}
int main()
{
    string s1("frijoles");
    string s2("beans");
    
    cout << "Larger  of frijoles and beans: " << maximal(s1, s2) << endl;
    cout << "Larger of 10 and 20: " << maximal(10, 22) << endl;
    cout << "It's a large world." << endl;
    
    return EXIT_SUCCESS;
}
