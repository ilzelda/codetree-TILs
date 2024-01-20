#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    cin>>n;

    vector<int> arr(100000);
    vector<int> dp(100000, -1001);


    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    dp[0] = arr[0];

    for(int i=1; i<n; i++){
        if(dp[i-1]+arr[i] > arr[i]) dp[i] = dp[i-1]+arr[i];
        else dp[i] = arr[i];
    }

    int max = -1001;
    for(int i=0; i<n; i++){
        max = max < dp[i] ? dp[i] : max;
    }
    cout << max;
}