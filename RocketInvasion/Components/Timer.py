"""
Default timer
"""

import time

class Timer:

    def __init__(self, functions=[], frequency=1000):

        self.functions = functions
        self.frequency = frequency

        self.last = time.perf_counter()
        self.now = time.perf_counter()

    def tick(self):

        self.now = time.perf_counter()

        if self.now-self.last >= self.frequency:

            self.now = self.last
            
            for el in self.functions:

                el()
