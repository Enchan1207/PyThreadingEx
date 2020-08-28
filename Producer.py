#
# プロデューサ キューにデータを追加する
#
from threading import Thread, Event
from queue import Queue
import random, time

class ProducerThread(Thread):
    def __init__(self, queue, endReq):
        super(ProducerThread, self).__init__()
        self.queue = queue
        self.endReq = endReq
    
    def run(self):
        lst = ["a", "b", "c", "d", "e"]
        while not self.endReq["stop"]:
            self.queue.put(random.choice(lst))
            time.sleep(random.randint(1, 3))

        print("Producer has detected endReq. funishing process now...")
