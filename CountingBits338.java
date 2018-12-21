public class CountingBits338 {
    public static void main(String[] args) {
        Solution338 sol = new Solution338();
        int[] numBits = sol.countBits(Integer.parseInt(args[0]));
        for(int i = 0; i < numBits.length; i++) {
            System.out.print(numBits[i] + " ");
        }
        System.out.println();
    }
}

class Solution338 {
    public int[] countBits(int num) {
        int[] numBits = new int[num+1];
        boolean odd = true;
        for(int i = 1; i <= num; i++) {
            if(odd) {
                numBits[i] = numBits[i-1] + 1;
                odd = false;
            }
            else {
                numBits[i] = numBits[i/2];
                odd = true;
            }
        }
        return numBits;
    }
}