#
# もしかしてpythonのthreadってこういうことできたりする?
#
from queue import Queue

from Consumer import ConsumerThread
from Producer import ProducerThread

def main():
    # スレッドとキューを作る
    maxQueue = 100
    queue = Queue(maxQueue)
    endReq = {"stop": False}
    thrConsumer = ProducerThread(queue, endReq)
    thrProducer = ConsumerThread(queue, endReq)

    # 開始
    thrConsumer.start()
    thrProducer.start()

    # 待機
    try:
        print("Thread has started. Type Ctrl+C to end.")
        while True:
            pass
    except KeyboardInterrupt:
        print("Detect SIGINT(were you type Ctrl+C?). start finishing process...")
        endReq["stop"] = True
        thrConsumer.join()
        thrProducer.join()
        print("All finishing process has completed. Program will soon end.")

if __name__ == '__main__':
    main()