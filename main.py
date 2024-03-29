from datetime import timedelta
import os
import time
import random


def start_working():
    count = 30537
    while True:
        send_commit(count)
        count += 1
        time.sleep(timedelta(hours=random.randint(2, 10)).seconds)
        # time.sleep(timedelta(seconds=0.5).seconds)


def send_commit(count):
    with open("README.md", "w") as file:
        file.write("I already have " + str(count) + " commits!")

    os.system("git commit -a -m commit" + str(count))
    # time.sleep(1)
    os.system("git push")


if __name__ == '__main__':
    start_working()
