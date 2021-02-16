from datetime import datetime
from math import floor
from .config import *

class Clock():

    def __init__(self):
        self.time = TIME
        self.start = int()
        self.end = int()

    def start_count(self):
        self.start = datetime.now()

    def update(self):
        difference = datetime.now() - self.start
        self.time = TIME - floor(difference.seconds)



