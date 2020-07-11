import argparse,sys,subprocess,time,os
from multiprocessing import Pool,Queue,Process
from ipaddress import ip_address
import socket

def help_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--number',
                            required = True,
                            default = 1,
                            type = int,
                            dest = 'number',
                            help = '并发数')
    parser.add_argument('-f','--func',
                            required = True,
                            type = str,
                            choices = ['ping','tcp'],
                            dest = 'func',
                            help = '方式')
    parser.add_argument('-ip','--ipaddr',
                            required = True,
                            type = str,
                            dest = 'ipaddr',
                            help = 'ip范围,只考虑C类子网')
    parser.add_argument('-v','--verbose',
                            action="store_true",
                            dest = 'verbose',
                            help = '详细信息')
    return parser

def splitip(iprange):
    if len(iprange.split('-')) == 2:
        if iprange.split('-')[0].split('.')[2] != iprange.split('-')[1].split('.')[2]:
            print('只考虑C类子网')
            sys.exit()
        startip = ip_address(iprange.split('-')[0])
        endip = ip_address(iprange.split('-')[1])
    else:
        startip = endip = ip_address(iprange)
    return startip,endip

def ipcheck(ip):
    #centos为-w，mac为-W
    #starttime = time.time()
    try:
        result = subprocess.call(f'ping -c 1 -W 1 {ip}',shell=True,stdout=subprocess.PIPE)
        print(os.getpid(),ip)
        if result == 0:
            print(ip)
    except Exception as e:
        pass

def portcheck(ipaddr,port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((ipaddr,port)) 
        #print(os.getpid(),port)
        if(result == 0):  
            print (ipaddr,port)
        s.close()
    except Exception as e:
        pass

'''
    result = subprocess.Popen(f'nc -z -n {ipaddr} 11100-11200',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    for port in result.stdout.readlines():
        infolist = port.decode('utf-8').split(' ')
        print(infolist[2],infolist[4])
'''
if __name__=="__main__":
    parser = help_parse().parse_args()
    pool = Pool(parser.number)
    list = []
    starttime = time.time()
    if parser.func == 'ping':
        start = splitip(parser.ipaddr)[0]
        end = splitip(parser.ipaddr)[1]
        while start != end+1:
            list.append(start)
            start +=1
        for ip in list:
            pool.apply_async(ipcheck,(ip,))
        pool.close()
        pool.join()
    else:
        for port in range(1,65536):
            pool.apply_async(portcheck,(parser.ipaddr,port,))
        pool.close()
        pool.join()
    if parser.verbose:
        print(time.time()-starttime)