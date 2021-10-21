
from datetime import datetime, timedelta
import os
import time
import random


def start_working():
    count = 1

    send_commit(count)

    # while True:
    #     sendCommit()
    #     time.sleep(timedelta(hours=random.randint(1, 10)).seconds)


def send_commit(count):
    with open("README.md", "w") as file:
        file.write("I already have " + str(count) + " commits!")

    os.system("git commit -a -m commit" + str(count))
    time.sleep(5)

    os.system("git push")


if __name__ == '__main__':
    start_working()
