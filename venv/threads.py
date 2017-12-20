# import thread
import threading
import time

def show():
    for i in range(1, 11):
        time.sleep(1)
        print "** Main Thread : ", i


# # print "========="
# # show()
#
#
# thread.start_new_thread(show(), ("Thread-1", ))


threadLock = threading.Lock

class MyThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name
        print self.name, "Created"

    def run(self):

        threadLock.acquire()

        for i in range(1,11):
            time.sleep(1)
            print self.name, " - @@", i

        threadLock.release()

th = MyThread("MyThread")

th.start()
show()