#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;
    int arr[10];
    for(int i =0 ;i < 10 ; i++){
        cin >> arr[i];
    }
    cout << arr[2] + arr[4] + arr[9];
    return 0;
}