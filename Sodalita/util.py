import psutil
import datetime

def main():
    print("___________________________SYSTEM INFORMATION___________________________\n")
    print("############ CPU ############")
    cpu_percent()
    cpu_count()
    cpu_freq()
    print("\n############ MEMORY ############")
    memory()
    print("\n############ DISK ############")
    disk()
    print("\n############ USERS ############")
    users()
    boot()

def cpu_percent():
    cp = psutil.cpu_percent(interval=1)
    p = cp*10
    print("CPU IN USE: {} %".format(p))

def cpu_count():
    l  = psutil.cpu_count()
    nl = psutil.cpu_count(logical=False)
    print("CPU Physical: {}\nCPU Logic: {}\nCPU TOTAL: {}".format(nl, (l-nl), l))

def cpu_freq():
    f = psutil.cpu_freq()
    print("CORRENT CPU FREQUENCY: {}Mhz\nMAX CPU FREQUENCY: {}Mhz\nMIN CPU FREQUENCY: {}Mhz".format(f.current, f.max, f.min))

def memory():
    vm = psutil.virtual_memory()
    print("USED MEMORY: {:.4f}GB\nMEMORY USED PERCENT: {}%\nPHYSICAL MEMORY: {:.4f}GB".format((vm.used/1000000000), vm.percent, (vm.total/1000000000)))
def disk():
    dsk = psutil.disk_usage('/')
    print("DISK USED PERCENT: {}%\nDISK USED: {:.4f}GB\nDISK FREE: {:.4f}GB\nDISK TOTAL: {:.4f}GB".format(dsk.percent, (dsk.used/1000000000), (dsk.free/1000000000), (dsk.total/1000000000)))
def users():
    u = psutil.users()
    for i in u:
        aj = datetime.datetime.fromtimestamp(i.started).strftime("%Y-%m-%d %H:%M")
        us = i.name
        print("USER: {}, LOGGED LAST TIME IN: {}".format(us, aj))

def boot():
    print("\nBOOTED COMPUTER IN: {}".format(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M")))

if __name__ == '__main__':
    main()