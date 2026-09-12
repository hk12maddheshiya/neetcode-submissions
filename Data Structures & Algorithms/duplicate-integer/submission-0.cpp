class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> un;
        for(int i = 0; i < n; i++){
            un.insert(nums[i]);
            if (un.size() != i + 1 ) return true;
        }
        return false;
            
    }
};