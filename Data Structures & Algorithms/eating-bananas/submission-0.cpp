class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int i1 =0, i2 = 0;
        for(int i: piles) if(i > i2) i2 = i;
        int i3 = (i1+i2+1)/2;

        while(i1<i2-1){
            int k = 0;
            for(int i: piles) k += (i+i3-1)/i3;
            if(k > h) i1 = i3;
            else i2 = i3;

            i3 = (i1+i2+1)/2;
        }
        return i2;
    }
};
