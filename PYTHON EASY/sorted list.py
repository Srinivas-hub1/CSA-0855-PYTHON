class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1, list2):
    # Create a dummy node to simplify the merge process
    dummy = ListNode()
    current = dummy
    
    # Pointers for both lists
    p1 = list1
    p2 = list2
    
    # Merge the two lists
    while p1 and p2:
        if p1.val < p2.val:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    
    # If there are remaining nodes in either list, append them
    if p1:
        current.next = p1
    elif p2:
        current.next = p2
    
    # Return the merged list, which starts from the next of dummy
    return dummy.next

def print_list(head):
    """ Helper function to print the linked list """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    # Creating two sorted linked lists for demonstration
    # List 1: 1 -> 2 -> 4
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    
    # List 2: 1 -> 3 -> 4
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    # Merging the two lists
    merged_list = merge_two_sorted_lists(list1, list2)
    
    # Printing the merged list
    print("Merged List:")
    print_list(merged_list)
