#include <iostream>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    
    int coins[N];
    for(int i=0; i<N; i++){
        cin >> coins[i];    
    }

    int ans = 0;

    for(int i=N-1; i>=0; i--){
        if(K!=0){
            int num = K / coins[i];
            ans += num;
            K -= num * coins[i];
        }
    }
    
    cout << ans;

    return 0;
}