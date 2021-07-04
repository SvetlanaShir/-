#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
ll ans=0, n;
    map <ll, ll> v;
    map <pair<ll, ll>, ll> w;
    pair<ll, ll> p, r;
    cin >> n;
    ll a, b;
    for (ll i=0; i<n; i++){
        cin >> a >> b;
        if (a==b){ans += v[a];
        v[a] += 1;}
        else{
            ans += v[a] + v[b];
            v[a] += 1;
            v[b] += 1;
            p.first = a;
            p.second = b;
            r.first = b;
            r.second = a;
            ans -= w[p];
            ans -= w[r];
            w[p] += 1;
        }}
    cout << ans;
return 0;
}
