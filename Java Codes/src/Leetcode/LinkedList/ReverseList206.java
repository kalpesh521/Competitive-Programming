package Leetcode.LinkedList;
//Reverse List
public class ReverseList206 {

    public void reverse(ListNode head) {
        if (head == null) {
            return;
        }
        ListNode prev = null;
        ListNode present = head;
        ListNode next = present.next;

        while (present != null) {
            present.next = prev;
            prev = present;
            present = next;
            if (next != null) {
                next = next.next;
            }
        }
        head = prev;
    }

    public static void main(String[] args) {

    }
}
