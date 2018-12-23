/**
 * URL of problem:
 * https://leetcode.com/problems/reveal-cards-in-increasing-order/
*/

public class RevealCardsIncOrder950 {
    public static void main(String[] args) {
        Solution950 sol = new Solution950();
        int[] deck = {};
        int[] ordering = sol.deckRevealedIncreasing(deck);
        for(int i = 0; i < ordering.length; i++) {
            System.out.print(ordering[i] + " ");
        }
        System.out.println();
    }
}

class Solution950 {
    public int[] deckRevealedIncreasing(int[] deck) {
        return null;
    }
}