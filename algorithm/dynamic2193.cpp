// 이친수

// !-------- 1 ---------! //
// 2차원 다이나믹으로 푸는 방법
// 이진수 중 0으로 시작하지 않거나, 1이 두번 연속으로 나타나지 않는다.
// **연속으로 나타나지 않기** 위해, **마지막 숫자를 기록**한다.

// 점화식
// D[N][L] = N자리 이친수, 마지막수 L
// D[N][0] = D[N-1][0] + D[N-1][1] -- 0일때,
// D[N][1] = D[N-1][0] -- 1일때

// 초기값
// D[1][0] = 0
// D[1][1] = 1

// !-------- 2 ---------! //
// 1차원으로 푸는 방법: 1, 0인 경우
// D[N]: N자리 이친수
// 마지막 수 0: N-1[0,1] --> D[N-1]
// 마지막 수 1: N-2[0, 1] // N-1[0] // N-1[1] --> D[N-2]

#include <iostream>
using namespace std;
long long d[91];
int main()
{
  int n;
  cin >> n;
  d[1] = 1;
  d[2] = 1;
  for (int i = 3; i <= n; i++)
  {
    d[i] = d[i - 1] + d[i - 2];
  }
  cout << d[n] << '\n';
  return 0;
}