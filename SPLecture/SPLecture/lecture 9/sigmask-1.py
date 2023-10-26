import signal
import time

if __name__ == "__main__":
    signal.pthread_sigmask(signal.SIG_BLOCK, [signal.SIGINT])

    # code that should not be interrupted
    print("running important code")
    time.sleep(10)
    print("finished running important code")

    signal.pthread_sigmask(signal.SIG_SETMASK, [])

    for i in range(20):
        print(f"counter {i}")
        time.sleep(1)
