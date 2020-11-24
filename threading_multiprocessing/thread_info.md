## Base info:
* for create threads use python modul: [threading](https://docs.python.org/3/library/threading.html)
* for create process use python modul: [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
###  How and when use threading or process:
> Threads run on a single processor and are good for speeding up some tasks, but not all. Tasks that require significant CPU computations and spend little time waiting for external events will obviously not run faster using multithreading, instead, you should use multiprocessing (multiprocessing).

## Threads:
* Чтобы запустить отдельный поток, нужно создать экземпляр потока Thread и затем запустить его с помощью метода .start():
* more info about [threads](https://webdevblog.ru/vvedenie-v-potoki-v-python/)
> code example:
``` 
import logging
import threading
import time
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")
  x = threading.Thread(target=thread_function, args=(1,))
    x.start()
 ```
* for stop thread use: join()
> code example:
```
import logging
import threading
import time
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
>```
> example on class:
```
import threading
from collections import defaultdict
import random

FISH = (None, 'plotva', 'okun', 'lesh')


class Fisher(threading.Thread):

    def __init__(self, name, worms, *args, **kwargs):
        super(Fisher, self).__init__(*args, **kwargs)
        self.name = name
        self.worms = worms

    def run(self):
        catch = defaultdict(int)
        for worm in range(self.worms):
            print(f'{self.name}: Worm № {worm} - fishing...', flush=True)
            _ = 3 ** (random.randint(50, 70) * 10000)
            fish = random.choice(FISH)
            if fish is None:
                print(f'{self.name}: Worm was eat', flush=True)
            else:
                print(f'{self.name}: Caught fish :{fish}.', flush=True)
                catch[fish] += 1
        print(f'Fisher {self.name} caught:')
        for fish, count in catch.items():
            print(f' {fish} - {count}')
vasya = Fisher(name= "Vasya", worms=12)
kolya = Fisher(name= "Kolya", worms=12)
print('=====> Go fishing ...\n')
vasya.start()
kolya.start()
print('=====> Waiting ...\n')
vasya.join()
kolya.join()
print('=====> Fishing is over.\n')
```
## Exceptions:
* to catch an error, its necessary to cah the error in thread, not in the adjacent thread 