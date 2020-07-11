#include <iostream>
using namespace std;
const int row = 5;
const int col = 4;
int main(){
    int max = 0;
    int p = 0;
    int c = 0;
    int s[row][col];
    cout << "enter elements in array" << endl;
    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            cin >> s[i][j];
        }
        
    }

    for(int i = 0; i < row; i++){
        for(int j = 0; j < col; j++){
            if(row == 0){
                p += s[i][j];
                max = p;
                c = 1;
				p = 0;
            }
            else if(row == 1){
                p += s[i][j];
                if(p >= max){
                    max = p;
                    c = 2;
					p = 0;
                }
            }
            else if(row == 2){
                p += s[i][j];
                if(p >= max){
                    max = p;
                    c = 3;
					p = 0;
                }
            }
            else if(row == 3){
                p += s[i][j];
                if(p >= max){
                    max = p;
                    c = 4;
					p = 0;
                }
            }
            else if(row == 4){
                p += s[i][j];
                if(p >= max){
                    max = p;
                    c = 5;
					p = 0;
                }
            }
        }
    }
	cout << c << " " << max << endl;
    
}

