class Solution {
    public boolean canAliceWin(int n) {
        // if(n < 10)  return false;
        // if(n < 19)  return true;
        int i=10;
        while (n >= 0){
            n = n-i;
            i -= 1;
        }
        if(i % 2 == 0)  return true;
        return false;
    }
}