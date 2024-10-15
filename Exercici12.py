#Solució al problema 12 basat en una interpretació simple de l'enunciat.
#Es fa el que es demana, però la manera en la qual està plantejat fa que els
#threads s'incrementen d'un a un i amb una unitat a la vegada. És a dir, no hi ha gaire simulació
# de la concurrència
import threading
import time
from idlelib.query import Query
import random
THREADS = 3
MAX_COUNT = 100

Threads_value = [0,0,0] #P, Q, R
Threads_name = ['P', 'Q', 'R']
mutex = threading.Semaphore(1)

def thread(index):
    global Threads_value
    global  Threads_name

    print("Thread {}".format(threading.current_thread().name))

    for i in range(MAX_COUNT//THREADS):
        time.sleep(random.uniform(0.1, 0.8))
        mutex.acquire()
        sum = Threads_value[0] + Threads_value[1]
        # If R<=Q+P
        if Threads_value[2]<=sum:
            Threads_value[index]+=1
            print("-----------------------------------------------------------------------------")
            print(f"Thread P thread value = {Threads_value[0]}")
            print(f"Thread Q thread value = {Threads_value[1]}")
            print(f"Thread R thread value = {Threads_value[2]}")
        mutex.release()


def main():
    threads = []
    for i in range(THREADS):
        t = threading.Thread(target=thread, name=Threads_name[i], args=(i,) )
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
