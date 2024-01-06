#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;

    int n_pass = 0;
    for(int i = 0; i<n; i++){
        int scores[4] = {};
        float sum = 0;

        for(int j=0; j<4; j++){
            int s;
            cin >> s;
            sum +=s;
        }
        if (sum/4 >= 60){
            cout << "pass" << endl;
            n_pass++;
        } 
        else cout << "fail" << endl;
    }
    cout << n_pass;
    return 0;
}