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

int main1() {
  /*int x, p, A, B;
  int attempts = 0;
  while (1) {
    attempts++;
    p = rand() + 2;
    if (isprime(p)) break;
  }
  x = rand() % p;
  A = rand() % p;
  B = modpow(A,x,p);*/
  cout << "PROVER-private: Pick x p A" << endl;
  int x, p, A; cin >> x >> p >> A;
  int B = modpow(A,x,p);

  cout << "PROVER-public: (A,B,p) = " << A << ' '  << B << ' ' << p << endl;

  while (1) {
    cout << "PROVER-private: Pick r between 0 and " << p-1 << endl;
    int r; cin >> r;
    int h = modpow(A, r, p);
    cout << "PROVER-public: h = " << h << endl;

    cout << "VERIFIER: Pick b = 0 or 1" << endl;
    int b; cin >> b; b = bool(b);

    int s = (r+b*x) % (p-1);
    cout << "PROVER-public: s = " << s << endl;
    bool ok = modpow(A,s,p) == h * 1ll * modpow(B,b,p) % p;
    cout << "VERIFIER " << ok;
  }
}
