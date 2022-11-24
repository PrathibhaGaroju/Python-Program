import multiprocessing
import time

class Process(multiprocessing.process):
    def __init__(self, id):
        super(process, self).__init__()
        self.id = id
    def run(self):
        time.sleep(1)
    print("I'm the process with id: {}".format(self.id))
            
if __name__ == '__main___':
    p = process(0)

    p.start()
 
    p.join()
    p = Process(1)
    p.start()
    p.join()    
            