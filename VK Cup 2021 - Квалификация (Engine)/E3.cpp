#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n=16;
string g1;
vector <ll> g;
vector <ll> ans;
ll t;
vector <ll> vec;
void vec_full(ll n){
    if (n==1){}else{
    ll a, b;
    a = n / 2;
    b = n - a;
    vec_full(a);
    vec_full(b);
    vec.push_back(n);
    }}

void antisort (vector <ll> v, ll n) {
    if (v.size()==1){
            ans.push_back(v[0]);
    }
    else{
	vector <ll> w;
	ll s = 0;
	while (s <  n){
    if (g[t] == 0){w.push_back(0); s += 1;}
    else{w.push_back(1); s += 1;}
    t-=1;
	}
	reverse(w.begin(), w.end());
    vector <ll> w_left, w_right;

	for (ll i = 0; i < n; i++) {
            if (w[i] == 0){w_left.push_back(v[i]);}
            else{w_right.push_back(v[i]);}
	}
	antisort (w_right, n - n/2);
	antisort (w_left, n/2);
}
}


int main() {
ll k = 1;
ll bad = 1;
vector <ll> v;
cin >> g1;
ll left = 1;
ll right = 100001;
while (bad!=0){
        //cout << k<< bad;
        k=(left + right) / 2;
        v.clear();
        vec.clear();
        g.clear();
vec_full(k);
for (ll i = 0; i <k; i++) {v.push_back(i+1);};
ll temp = 0;
        bad=0;
for (ll i = 0; i <vec.size(); i++) {
    ll n0=0, n1=0;
    while ((n0<vec[i]/2) && (n1<vec[i] - vec[i]/2)){
            if (temp >= g1.size()){bad = 1; break;}
           if (g1[temp] == '0'){g.push_back(0); n0 += 1; temp+=1;}
    else{g.push_back(1); n1 += 1; temp+=1;}}
    if (bad == 1){break;}
    while (n0<vec[i]/2){g.push_back(0); n0 += 1;}
    while (n1<vec[i] - vec[i]/2){g.push_back(1); n1 += 1;}}
if (temp != g1.size()){bad = 2;}
if (bad == 1){right = k-1;}
if (bad == 2){left = k+1;}
}


//for (ll i = 0; i <vec.size(); i++) {cout << vec[i];}
//cout <<endl;
//for (ll i = 0; i <g.size(); i++) {cout << g[i];}
t = g.size()-1;
antisort(v, k);
cout << k<<endl;
for (ll i = ans.size()-1; i >=0; i--) {cout << ans[i]<<" ";}
return 0;
}
