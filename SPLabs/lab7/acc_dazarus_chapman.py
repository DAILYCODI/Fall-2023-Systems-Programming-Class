import threading

# must include a global list that is initalized from 0 to 499
# using glist

glist = list(range(500))

#Initialize the global accumulate list with zeros
# this makes the acc value visible to rest of program
alist = [0] * 5

tid = threading.get_native_id()

# accumulate function where i depicts a starting index
def accumulate(i: int):
    acc = sum(glist[i * 100: (i + 1) * 100])
    alist[i] = acc
    print(f"Accumulated value in thread [{tid} -> {i}] is {acc}")


def main():
    threads = []
    max_threads = 5

    # create thread objects
    for i in range(max_threads):
        # identify our argument and pass in our function
        thread = threading.Thread(target=accumulate, args=(i,))
        # creates an list of threads so will keep track of each thread
        threads.append(thread)

    # start threads
    for thread in threads:
        thread.start()
    
    #wait for threads to finish
    for thread in threads:
        thread.join()

        
    # total = alist[0] + alist[1] + alist[2] + alist[3] +alist[4]
    #print(f"Total is: {total}")
    total_acc = sum(alist)
    print(f"Total acc is: {total_acc}")

if __name__ == "__main__":
    main()
