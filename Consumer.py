#
# コンシューマ キューのデータを処理する
#
from threading import Thread, Event
import queue

class ConsumerThread(Thread):
    def __init__(self, queue, endReq):
        super(ConsumerThread, self).__init__()
        self.queue = queue
        self.endReq = endReq
    
    def run(self):
        while not self.endReq["stop"]:
            try:
                data = self.queue.get(timeout = 5)
            except queue.Empty:
                data = None
            
            if data is not None:
                print("Received! {0}".format(data))
                self.queue.task_done()
            else:
                print("data has not produced.")

        print("Consumer has detected endReq. funishing process now...")
