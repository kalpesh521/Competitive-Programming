package Leetcode.LinkedList;

import java.util.List;

public class ReverseLinkedList92 {

    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (left == right) {
            return head;
        }
    //skip node upto left-1 nodes
        ListNode current = head;
        ListNode prev = null;

        for (int i = 0; current != null && i < left - 1; i++) {
            prev = current;
            current = current.next;
        }


        // reverse  left and right (right - left +1 )
        ListNode last = prev;
        ListNode newEnd = current;
        ListNode next = current.next;
        for (int i = 0; current != null && i < right - left + 1; i++) {

            current.next = prev;
            prev = current;
            current = next;
            if (next != null) {
                next = next.next;
            }

        }

        if (last != null) {
            last.next = prev;

        } else {
            head = prev;
        }

        newEnd.next = current;
        return head;
    }
}
