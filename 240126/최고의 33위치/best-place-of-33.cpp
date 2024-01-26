#include <iostream>

int main() {
    // 여기에 코드를 작성해주세요.
    using namespace std;

    int N;
    cin >> N;

    int arr[N][N] = {0};

    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cin >> arr[i][j];
        }
    }

    int max = 0;
    for(int i=0; i<=N-3; i++){
        for(int j=0; j<=N-3; j++){
            int count = 0;

            for(int l=i; l<i+3; l++){
                for(int m=j; m<j+3; m++){
                    count += arr[l][m];
                }
            }

            if(max < count) max = count;
        }
    }

    cout << max;
    return 0;
}