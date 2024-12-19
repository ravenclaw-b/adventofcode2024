#include <bits/stdc++.h>
#include <set>

using namespace std;

unsigned long long A, B, C;



int opcode()
{   // NOTE: This function would only work for my specific input
    if (A==0) return -1;
    B = A & 7; //2,4
    B = B ^ 3;  //1,3
    C = A >> B;  //7,5
    //B = B ^ C;   B=B^B
    B = B^5;  //1,5
    //B = B ^ 3;
    B = B ^ C;  //new 4,2
    A = A >> 3;//0,3

    return B & 7;  //5,5
}

int printvector(set <unsigned long long>& v)
{
    for(auto &item:v){
        cout<< item <<", ";
    }
    cout<<endl;
    return 0;
}
int main() {
    vector<int> p = {2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0};
                     
    unsigned long long count = 0;
    vector<unsigned long long> pow;
    unsigned long long result = 999999999999999999;
    pow.push_back(7);
    unsigned long long temp=pow[0];
    for(int i=1; i<20; i++){
        temp = temp<<1;
        temp+=1;
        temp = temp<<1;
        temp+=1;
        temp = temp<<1;
        temp+=1;
        pow.push_back(temp);
    }
    //for (int i=0; i<20; i++){
    //    cout<<pow[i]<<endl;
    //}
    int x;
    int i = 0;

    set<unsigned long long> bestlist{0,1,2,3,4,5,6,7};
    for(int k=1; k<17; k++){
        //cout<<k<<endl;
        //printvector(bestlist);
        //cin>>x;
        set<unsigned long long> templist;
        for(auto & item : bestlist){
            for(unsigned long long  j=0; j<1024;j++){
                count = item+ (j<<(k*3));
                //count = j;

                
                A = count; //count;
                B = 0;
                C = 0;

                // Print progress every 1,000,000 counts
                //if (count % 100000000 == 0) {
                //   cout << "Checking count: " << count << endl;
                //}

                // Process program
                
                i = 0;
                while (i<p.size() && p[i] == opcode()) {
                    if (i==k){
                        
                        //cout<<i<<" "<<(count & pow[i])<<" count=  "<< count <<"  pow = "<< pow[i]<<endl;
                        templist.insert(count & pow[i]);
                        //cin>>x;

                    }
                    //cout<<count<<"  "<<i<<endl;
                    i += 1;

                }
                if(i==16 && A==0){
                    //cout<<"result = "<<count<<endl;
                    if (result > count)
                       result = count;
                }
                
            }
            
        }
        bestlist = templist;
    }

    cout << "Resulting count: " << result << endl;
    return 0;
}