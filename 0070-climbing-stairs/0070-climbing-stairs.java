class Solution {
    public int climbStairs(int n) {
        int result=n;
        int a=2;
        int b=3;
        if(n<=3){
            return n;
        }
        for(int i=4; i<n+1; i++){
            result=a+b;
            a=b;
            b=result;
        }
        return result;
    }
}