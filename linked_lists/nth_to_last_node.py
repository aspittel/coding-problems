"""
Find the Nth to last node in a linked list.

From Python for Data Structures Udemy
"""
def linked_list_length(node):
    length = 1
    while node.nextnode:
        node = node.nextnode
        length += 1
    return length
        
    
def nth_to_last_node(n, head):
    length = linked_list_length(head)
    
    curr_index = 0
    needed_index = length - n
    
    while needed_index > curr_index:
        head = head.nextnode
        curr_index += 1
    
    return head


# Alternative solution (better since O(N) rather than O(2N))
def nth_to_last_node(n, head):
	fast = slow = head

	for i in range(n-1):
		fast = fast.nextnode

	while fast.nextnode:
		fast = fast.nextnode
		slow = slow.nextnode

	return slow
