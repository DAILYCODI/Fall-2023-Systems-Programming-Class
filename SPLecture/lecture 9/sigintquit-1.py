import signal

counter = 0


def sig_handler(signum, frame):
    global counter

    if signum == signal.SIGINT:
        counter += 1
        print(f"Caught SIGINT {counter}")
        return

    print("Caught SIGQUIT - that's all folks!")
    return


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGQUIT, sig_handler)

    counter = 0
    while True:
        signal.pause()
