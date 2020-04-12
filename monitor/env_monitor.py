import os
from collections import OrderedDict


def get_memory_info():
    mem_info = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            print(line)
