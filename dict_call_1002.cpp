#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>

#define MAX  100 + 10
#define INF 100000000
using namespace std;

string phoneNum;
vector <string> dict(10);
int dp[MAX]={0},path[MAX] = {0};

void initDict(){
    dict[0]="oqz";  dict[1]="ij";   dict[2]="abc"; dict[3]="def";
    dict[4]="gh";   dict[5]="kl";  dict[6]="mn";   dict[7]="prs";
    dict[8]="tuv";  dict[9]="wxy";
}

bool match(string number, string word){
    for(int i = 0 ; i < number.length(); i ++){
        int len = dict[number[i]-'0'].length(),j;
        for( j = 0; j < len; j ++ ){
            if(dict[number[i]-'0'][j] == word[i]) break;
        }
        if(j >= len) return false;
    }
    return true;
}

int main(){
    initDict();
    while(cin >> phoneNum && phoneNum != "-1"){
        int n;
        cin>>n;
        vector<string> word(n);
        for(int i = 0; i < n; i ++ ) cin >>word[i];
        for(int i = 0; i < MAX; i ++ ) dp[i] = INF;
        memset(path,-1,sizeof(path));
        dp[0] = 0;
        for(int i = 1; i <= phoneNum.length(); i ++ ){
            for(int j = 0; j < n; j ++ ){
                if( (word[j].length() + i-1) <= phoneNum.length() && match( phoneNum.substr(i-1,word[j].length()) , word[j] ) ){
                    if(dp[i + word[j].length()-1] > dp[i-1] + 1){
                        dp[i + word[j].length()-1] = dp[i-1] + 1;
                        path[i + word[j].length()-1] = j;
                    }
                }
            }

        }
        if(path[phoneNum.length()] == -1) cout<<"No solution."<<endl;
        else{
            vector <string> ans;
            int k = phoneNum.length();
            while(path[k] != -1){
                ans.push_back(word[path[k]]);
                k = k - word[path[k]].length();
            }
            int ansLen = ans.size();
            cout<<ans[ansLen-1];
            for(int i = ansLen-2; i >= 0 ; i-- ) cout<<" "<<ans[i];
            cout<<endl;
        }
    }

    return 0;
}