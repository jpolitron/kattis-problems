//
//  main.cpp
//  inherantinceEx
//
//  Created by Jessie Politron on 1/31/20.
//  Copyright © 2020 Jessie Politron. All rights reserved.
//

#include "Mother.hpp"
#include "Daughter.hpp"
#include <iostream>

using namespace std;

int main()
{
    Mother mom;
    mom.sayName();
    
    Daughter tina;
    tina.sayName();
    
    return EXIT_SUCCESS;
}
