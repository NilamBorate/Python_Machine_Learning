import time
import threading    

def DisplyEven(No):
    for i in range(1,No,1):
        if (i%2==0):
            print("Even number : ",i)

def DisplyOdd(No): 
    for i in range(1,No,1):
        if (i%2!=0):
            print("Odd number : ",i)
   
def main():

    print("Demonstration of parallel programming using multiple threads")
    Number=2000

    p1=threading.Thread(target=DisplyEven,args=(Number,))
    p2=threading.Thread(target=DisplyOdd,args=(Number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")

if __name__=="__main__":
    start_time=time.process_time()
    main() 
    end_time=time.process_time() 
    print("Execution time is : ",end_time-start_time)  