//uku
//========================================================
class Solution {
    public String convert(String s, int numRows) {

        if(numRows == 1 || numRows >= s.length())
            return s;

        StringBuilder[] result = new StringBuilder[numRows];

        for(int i = 0; i < numRows; i++) {
            result[i] = new StringBuilder();
        }

        int j = 0;
        int direction = 1;

        for(int i = 0; i < s.length(); i++) {

            result[j].append(s.charAt(i));

            if(j == 0)
                direction = 1;
            else if(j == numRows - 1)
                direction = -1;

            j += direction;
        }

        StringBuilder ans = new StringBuilder();

        for(int i = 0; i < numRows; i++) {
            ans.append(result[i]);
        }

        return ans.toString();
    }
}