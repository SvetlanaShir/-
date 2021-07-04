#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
ll n;
ll t;
cin>>n;
if (n==2){cout << -1; return 0;}
vector <ll> v(101);
v[1] = 1;
v[2] = 0;
for (ll i = 3; i <= 100; i++) {
    ll sq = 12;
    for (ll j = 1; j <= 10; j++) {
        if (j*j >= i){sq = j; break;}
    }
    t = sq*sq-i;
    if (t==2){v[i] = sq+1;} else{v[i] = sq;}
    }
t = v[n];
cout << t;
vector <char> ans[t];
for (ll i = 0; i < t; i++) {
    for (ll j = 0; j < t; j++) {ans[i].push_back('.');
        }}

ans[0][0]='o';
n-=1;
ll x=0, p=1;

while (n>0){
        if (n==1){x+=1; p=1;
        ans[x][x]='o';
        n-=1;
if (ans[x-1][x] == '.'){
ans[x-1][x] = 'o';
ans[x][x-1] = 'o';
ans[x-2][t-1] = '.';
ans[t-1][x-2] = '.';

}
        }
        else{
       // cout << n<<" "<<x<<" "<<p<<endl;
        if(x+p < t){
            ans[x][p+x]='o';
            ans[p+x][x]='o';
            p+=1;
            n-=2;}
        else{x+=1; p=1;
        ans[x][x]='o';
n-=1;
        }}
}
for (ll i = t-1; i >=0; i--) {cout << endl;
    for (ll j = 0; j < t; j++) {
        cout<<ans[i][j];
        }
    }
return 0;
}
