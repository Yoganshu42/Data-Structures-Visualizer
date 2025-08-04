from inputs import Inputs

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def list_traversal(self):
        if self.head is None:
            print("List is empty!")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def insert_at_head(self,data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node 

    def insert_at_tail(self,data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                n = self.head
                while n.ref:
                    n = n.ref
                n.ref = new_node
            print(f"Element {data} inserted at the end of the list.")

    def insert_at_mid(self,data):
        try:
             position = int(input("Enter the position of the element you want to insert after: "))
        except Exception:
             print("Error! Position can only be a positive integer.")

        if position < 0:
             print("Position can't be negative!")
             return
        new_node = Node(data)
        if position == 0:
             new_node.ref = self.head
             self.head = new_node
             print(f"Element {data} is inserted at beginning of the list.")
             return
        temp = self.head
        current_pos = 0

        while temp is not None and current_pos < position -1:
             temp = temp.ref
             current_pos += 1
            
        if temp is None:
             print("Position out of bond!")
             return
        new_node.ref = temp.ref
        temp.ref = new_node
        print(f"Element {data} inserted at {position}")
             
    def delete_at_head(self):
         if self.head is None:
              print("List is empty! Nothing to delete.")         
              return
         deleted_data = self.head.data
         self.head = self.head.ref
         print(f"Element {deleted_data} is deleted")

    def delete_at_tail(self):
         if self.head is None:
              print("List is empty! Nothing to delete.")
              return
         if self.head.ref is None:
              deleted_data = self.head.data
              self.head = None
              print(f"Element {deleted_data}.\n List Empty!")
              return
         n = self.head
         while n.ref.ref:
              n = n.ref
         deleted_data = n.ref.data
         n.ref = None    
         print(f"Element {deleted_data} is deleted from the list! ")
         return
    
    def delete_at_mid(self):
        try:
             position = int(input("Enter the position of the element you want to delete from: "))
        except Exception:
             print("Error! Position can only be a positive integer.")

        if position < 0:
             print("Position can't be negative!")
             return
        
        if position == 0:
             self.delete_at_head()
             return
        temp = self.head
        current_pos = 0

        while temp is not None and current_pos < position -1:
             temp = temp.ref
             current_pos += 1
            
        if temp is None:
             print("Position out of bond!")
             return
        deleted_data = temp.ref.data
        temp.ref = temp.ref.ref
        print(f"Element {deleted_data} deleted from {position}")

     

class ListOperations:
    def run(self):
        sll = SinglyLinkedList() 

        while True:
            choice = Inputs.choice_LinkedList()
            if len(choice) == 1:
                if choice in ['1']:
                    try:    
                        data = input("Enter the content you want to insert to head: ")
                        sll.insert_at_head(data)
                        print(f"Element {data} successfully added in List")
                    except ValueError:
                        print("Enter a valid item to insert!")
                    except Exception as e:
                        print(f"Error: {e}")
                elif choice in ['2']:
                    try:    
                        data = input("Enter the content you want to insert to head: ")
                        sll.insert_at_head(data)
                        print(f"Element {data} successfully added in List")
                    except ValueError:
                        print("Enter a valid item to insert!")
                    except Exception as e:
                        print(f"Error: {e}")
                elif choice in ['2']:
                    try:    
                        data = input("Enter the content you want to insert to head: ")
                        sll.insert_at_head(data)
                        print(f"Element {data} successfully added in List")
                    except ValueError:
                        print("Enter a valid item to insert!")
                    except Exception as e:
                        print(f"Error: {e}")
                elif choice in ['3']:
                    try:    
                        data = input("Enter the content you want to insert to head: ")
                        sll.insert_at_mid(data)
                        print(f"Element {data} successfully added in List")
                    except ValueError:
                        print("Enter a valid item to insert!")
                    except Exception as e:
                        print(f"Error: {e}")

                elif choice in ['4']:
                    sll.delete_at_head()

                elif choice in ['5']:
                    sll.delete_at_tail()

                elif choice in ['6']:
                    sll.delete_at_mid()

                elif choice in ['7']:
                    print(f"List content:")    
                    sll.list_traversal()

                elif choice in ['8']:
                    print("Exiting...\n\n")
                    break
     
# l1 = SinglyLinkedList()
# l1.insert_at_head(10)
# l1.insert_at_tail(20)
# l1.insert_at_mid(15)
# l1.insert_at_mid(35)
# l1.insert_at_mid(59)
# l1.list_traversal()
# l1.delete_at_head()
# l1.list_traversal()
# l1.delete_at_tail()
# l1.list_traversal()
# l1.delete_at_mid()
# l1.list_traversal()
