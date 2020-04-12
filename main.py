from monitor import env_monitor

import os, sys

dir_test = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, dir_test)

if __name__ == '__main__':
    print("dir_test:" + dir_test)
    env_monitor.get_memory_info()

