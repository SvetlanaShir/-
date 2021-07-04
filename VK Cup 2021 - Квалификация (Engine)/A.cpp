#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll n, q = 0;
    cin >> n;
    string a, ans = "blue";
    for (ll i=0; i<n; ++i){
        cin >> a;
        if (a == "lock"){q = 1;}else{
            if (a == "unlock"){q = 0;}else{
                if (q ==0){ans = a;
    }}}}
    cout << ans;
return 0;}
