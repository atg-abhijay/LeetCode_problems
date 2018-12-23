import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

/**
 * URL of problem:
 * https://leetcode.com/problems/reveal-cards-in-increasing-order/
*/

public class RevealCardsIncOrder950 {
    public static void main(String[] args) {
        Solution950 sol = new Solution950();
        int[] deck = {17, 13, 11, 2, 3, 5, 7};
        int[] ordering = sol.deckRevealedIncreasing(deck);
        for(int i = 0; i < ordering.length; i++) {
            System.out.print(ordering[i] + " ");
        }
        System.out.println();
    }
}

class Solution950 {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        int deckSize = deck.length;
        Deque<Integer> dq = new ArrayDeque<Integer>();
        dq.add(deck[deckSize-1]);
        int count = 1;
        while(count != deckSize) {
            Integer lastCard = dq.removeLast();
            dq.addFirst(lastCard);
            dq.addFirst(deck[deckSize-1-count]);
            count++;
        }

        int[] ordering = new int[deckSize];
        int index = 0;
        while(!dq.isEmpty()) {
            ordering[index] = dq.removeFirst();
            index++;
        }

        return ordering;
    }
}