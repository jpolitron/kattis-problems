#include <iostream>
using namespace std;
void display(int arr[5]){
for(int i =0; i < 5; i++){
	cout << arr[i] << " \t";
}
}
int main()
{
	int arr[5] = {4,1,10,7,9};
	display(arr);
	return 0;
	}

