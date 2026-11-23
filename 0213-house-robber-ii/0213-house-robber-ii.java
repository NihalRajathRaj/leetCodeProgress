class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 1) return nums[0];
        if(n == 2) return Math.max(nums[0], nums[1]);
        int rob1 = nums[0];
        int rob2 = Math.max(nums[0], nums[1]);
        for(int i=2; i<=n-2; i++){
            int curr1 = Math.max(rob2, rob1 + nums[i]);
            rob1 = rob2;
            rob2 = curr1;
        }
        int rob3 = nums[1];
        int rob4 = Math.max(nums[1], nums[2]);
        for(int j=3; j<=n-1; j++){
            int curr2 = Math.max(rob4, rob3 + nums[j]);
            rob3 = rob4;
            rob4 = curr2;
        }
        return Math.max(rob2, rob4);
    }
}