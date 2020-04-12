import os
from collections import OrderedDict
from collections import namedtuple

# 磁盘使用信息
usage_tuple = namedtuple('usage', 'free,total,used,percent')

disk_tuple = namedtuple('partition', 'device mount_point fstype')

GB = 1024 * 1024 * 1024


# 读取内存信息
def get_memory_info():
    mem_info = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            array = line.split(":")
            mem_info[array[0]] = array[1].strip()
        return mem_info


# 获取磁盘使用状态
def disk_state(path):
    # 返回具有文件描述符fd的文件的文件系统信息
    state = os.statvfs(path)
    # f_avail 非超级用户可获取的块数
    # f_frsize 分栈大小
    free = state.f_bavail * state.f_frsize
    total = state.f_blocks * state.f_frsize
    used = total - free
    try:
        percent = (float(used) / total) * 100
    except ZeroDivisionError:
        percent = 0
    return usage_tuple(round(free / GB, 3), round(total / GB, 3), round(used / GB, 3), percent)


# 获取分区详情
def disk_partitions(all=False):
    physical_devices = []
    f = open("/proc/filesystem", "r")
    for line in f:
        if not line.startswith("none"):
            continue
        physical_devices.append(line.strip())

    result = []
    f = open("/etc/mtab", "r")
    for line in f:
        if not line.startswith("none"):
            continue
        fields = line.split()
        device = fields[0]
        mount_point = fields[1]
        fstype = fields[1]
        if not all and fstype not in physical_devices:
            continue
        if device == "none":
            device = ""
        d_tuple = disk_tuple(device, mount_point, fstype)
        result.append(disk_tuple)
    return result
