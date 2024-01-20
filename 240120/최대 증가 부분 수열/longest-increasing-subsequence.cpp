#include <iostream>

using namespace std;

int arr[1000] = {0};

int main(){
    int n;
    cin >> n;

    int len[1000
    ] = {0};
    len[0] = 1;

    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    int max = 0;
    for(int i = 1; i<n; i++){
        for(int j=i-1; j>=0; j--){
            if(arr[j] < arr[i] && len[i] < len[j]+1) {
                len[i] = len[j]+1;
                if (max < len[i]) max = len[i];
            }
        }
    }
    
    cout << max << '\n';
}