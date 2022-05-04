#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int modpow(ll x, ll p, ll mod) {
  ll y = 1;
  do {
    if (p & 1) y = y * x % mod;
    x = x * x % mod;
  } while (p/=2);
  return y;
}

bool isprime(int p) {
  for (int i=2; i*i<=p; i++) {
    if (p % i == 0) return 0;
  }
  return 1;
}

int main() {
  int x, p, A, B;
  int attempts = 0;
  while (1) {
    attempts++;
    p = rand() + 2;
    if (isprime(p)) break;
  }
  x = rand() % p;
  A = rand() % p;
  B = modpow(A,x,p);

  printf("Ppriv: x=%d\n", x);
  printf("Ppub: A=%d, B=%d, p=%d\n",A,B,p);

  for (int i=0; i < 100; i++) {
    int r = rand() % p;
    printf("Ppriv: r=%d\n", r);
    int h = modpow(A, r, p);
    printf("Ppub: h=%d\n", h);

    int b = rand() % 2;
    printf("V: b=%d\n", b);

    int s = (r+b*x) % (p-1);
    printf("Ppub: s=%d\n", s);
    int ok = modpow(A,s,p) == h * 1ll * modpow(B,b,p) % p;
    printf("V: ok=%d\n", ok);
    if (!ok) {
      printf("FAIL\n");
      break;
    }
  }
  printf("x was %d\n", x);
  printf("%d attempts\n", attempts);
}