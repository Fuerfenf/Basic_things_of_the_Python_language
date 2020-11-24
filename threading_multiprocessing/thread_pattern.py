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
