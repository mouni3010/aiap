class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        """Insert a node at the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning")
        self.display()
    
    def insert_at_end(self, data):
        """Insert a node at the end of the linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted {data} at the end")
            self.display()
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Inserted {data} at the end")
        self.display()
    
    def delete_by_value(self, value):
        """Delete a node by its value"""
        if not self.head:
            print("List is empty, nothing to delete")
            return
        
        # If head needs to be deleted
        if self.head.data == value:
            self.head = self.head.next
            print(f"Deleted {value} from the list")
            self.display()
            return
        
        # Search for the node to delete
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                print(f"Deleted {value} from the list")
                self.display()
                return
            current = current.next
        
        print(f"Value {value} not found in the list")
    
    def display(self):
        """Display the linked list"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        if elements:
            print("Linked List: " + " -> ".join(elements) + " -> None")
        else:
            print("Linked List: Empty")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    print("=== Linked List Operations ===\n")
    
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    
    print()
    ll.insert_at_beginning(5)
    
    print()
    ll.insert_at_end(40)
    
    print()
    ll.delete_by_value(20)
    
    print()
    ll.delete_by_value(5)
    
    print()
    ll.delete_by_value(100)