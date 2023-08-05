#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstring>
#include <climits>
#include <cassert>
#include <algorithm>
using namespace std;

#define speedup ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
#define ll long long


int main(){
    speedup
    int n, m; cin >> n >> m;
    assert(n > 0);
    vector<vector<int>> graph(n), rev_graph(n);
    for (int i = 0; i < m; i++){
        int u, v; cin >> u >> v;
        graph[u].push_back(v);
        rev_graph[v].push_back(u);
    }
    queue<int> q;
    vector<bool> vis(n, false);
    q.push(0);
    vector<int> out_deg(n);
    while (!q.empty()){
        int u = q.front(); q.pop(); vis[u] = true;
        for (int v: graph[u]){
            if (!vis[v]){
                q.push(v);
            }
        }
        out_deg[u] = graph[u].size();
    }
    int cnt = 0;
    while (cnt < n){
        for (int i = 0; i < n; i++){
            if (out_deg[i] == 0){
                cout << "Vehicle " << i << " is instructed to move" << endl;
                for (int j: rev_graph[i]){
                    out_deg[j]--;
                }
                out_deg[i] = INT_MAX;
                cnt++;
            }
        }
    }
    cout << "Traffic Cleared" << endl;
    return 0;
}