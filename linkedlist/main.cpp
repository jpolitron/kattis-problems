//line 10
void print(Node* n)
{
  while(n != NULL)
  {
    cout << n->data << " ";
    n = n -> next;
  }
}

int main()
{
  Node* head = NULL;
  Node* second = NULL;
  Node* third = NULL;

  //allocate 3 nodes in the heap
  head = new Node();
  second = new Node();
  thrid = new  Node();

  head ->data = 1; //assign data in first node
  head ->next = second; //link first node with second

  second->data = 2; //assign data to node with second
  second->next third;

  third->data = 3; //assign to third node
  third->next = NULL;

  printList(head);

  return 0;
}
