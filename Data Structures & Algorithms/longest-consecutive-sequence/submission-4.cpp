class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int>res;
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int ans=0;
        for(int i=0;i<n;i++){
           if(res.count(nums[i]-1)){
            res[nums[i]]=1+res[nums[i]-1];
           }else{
            res[nums[i]]=1;
           }
           ans=max(ans,res[nums[i]]);
        }
        return ans;
    }
};
