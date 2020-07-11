#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
    unordered_set<int> days;
    int N,A,B;
    cin >> N;
    for(int i = 0; i < N; i++){
	    cin >> A;
	    cin >> B;
        for(int n = A; n <= B; n++){
            days.insert(n);
        }
    }
    cout << days.size() << endl;
    return 0;
}
