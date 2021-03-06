from monitor import env_monitor

import os, sys

# 获取当前目录的绝对路径
dir_test = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, dir_test)

if __name__ == '__main__':
    # env_monitor.get_memory_info()
    result = env_monitor.disk_partitions(True)
    for r in result:
        print("device:" + r.device)
        print("mount_point:" + r.mount_point)
        print("fstype:" + r.fstype)
