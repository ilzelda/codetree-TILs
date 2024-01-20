#include <iostream>

using namespace std;

int arr[1000] = {0};

int main(){
    int n;
    cin >> n;

    int dp[1000] = {0};
    dp[0] = 1;

    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    for(int i = 1; i<n; i++){
        for(int j=i-1; j>=0; j--){
            if((arr[j] < arr[i]) && (dp[i] < dp[j]+1)) {
                dp[i] = dp[j]+1;
            }
        }
    }

    int max = 1;
    for(int i = 1; i<n; i++){
        if (max < dp[i]) max = dp[i];
    }
    
    cout << max << '\n';
}