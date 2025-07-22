from stack import StackOperations
from queue_ds import QueueOperations
from inputs import Inputs

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
            pass
        if ds == 4:
            pass
        if ds == 5:
            pass
        if ds == 6:
            print("Thanks for using The DATA STRUCTURE VISUALIZER")
            exit()


if __name__  == "__main__":
    main()
