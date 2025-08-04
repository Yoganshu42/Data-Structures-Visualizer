from stack import StackOperations
from queue_ds import QueueOperations
from inputs import Inputs
from circular_queue import CircularQueueOperations
from singly_linked_list import ListOperations

print("\t\t\t--- WELCOME TO DATA STRUCTURE VISUALIZER ---")

def main():
    while True:
        ds = Inputs.inputs_main()

        if ds == 1:
            s = StackOperations()
            s.run()
        if ds == 2:
            q = QueueOperations()
            q.run()
        if ds == 3:
            cq = CircularQueueOperations()
            cq.run()
        if ds == 4:
            sll = ListOperations()
            sll.run()
        if ds == 5:
            pass
        if ds == 6:
            pass
        if ds == 7:
            print("Thanks for using The DATA STRUCTURE VISUALIZER")
            exit()


if __name__  == "__main__":
    main()
