#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    int i;
    int arr[10] = {};
    for(i=0; i<10; i++){
        int n;
        cin >> n;
        if (n == 0) break;
        else arr[i] = n; 
    }

    for (int j=i-1; j>=0; j--){
        cout << arr[j] << ' ';
    }
    return 0;
}