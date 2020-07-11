//
//  main.cpp
//  linked
//
//  Created by Jessie Politron on 3/25/20.
//  Copyright © 2020 Jessie Politron. All rights reserved.
//

#include <iostream>
#include <cstdlib>
using namespace std;

struct Node
{
    int data;
    Node *next;
};
class LinkedList
{
public:
    LinkedList()
    {
        head = NULL;
        tail = NULL;
    }
    void add_node(int n)
    {
        Node *temp = new Node;
        temp->data = n;
        temp->next = NULL;
        
        if(head == NULL)
        {
            head = temp;
            tail = temp;
        }
        else
        {
            tail->next = temp;
            tail = tail->next;
        }
    }
private:
    Node *head, *tail;
};

int main()
{
    LinkedList l;
    l.add_node(2);
    l.add_node(3);
    
    const Node *cursor = head;
    while(cursor != NULL)
    {
        cout << cursor->data << endl;
    }
    return EXIT_SUCCESS;
}
