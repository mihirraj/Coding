public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        int carry = 0;
        while(l1 != null || l2!= null || carry!= 0){
            ListNode tempNode = new ListNode(0);
            int sum = carry;
            if(l1!= null){
                sum = sum + l1.val;
                tempNode = l1; //If l1 exists, make tempNode point to it.
                l1 = l1.next;
            }
            if(l2 != null){
                sum = sum + l2.val;
                tempNode = l2; //If l2 exists, make tempNode point to it.
                l2 = l2.next;
            }
            carry = sum / 10;
            tempNode.val = sum % 10; //Modify tempNode
            curr.next = tempNode;
            curr = curr.next;
        }
        return dummy.next;
    }