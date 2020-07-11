#include<iostream>
using namespace std;
void bubble(int arr[], int size){
	for(int i = 0; i < size-1;i++){
		for(int j = 0; j < size-1-i; j++){
			if(arr[j] > arr[j+1])
				swap(arr[j],arr[j+1]);
		}
	
	}
}
int main(){
	int arr[] = {4,2,8,10,3,5};
	int size = 6;
	bubble(arr,size);
	for(int j = 0; j < size; j++){
		cout << arr[j] << " " ;
	}
}
