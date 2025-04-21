from properties import serv_dir,index
from response import *
import os.path
from datetime import datetime

def handle_req(req,ip,nlog):
    req = parse_request(req)
    itarget = req['start-line']['target']
    target,status_code,status_msg = check_target(itarget)
    write_log(nlog,ip,status_code,itarget,req['headers']['User-Agent'])
    data = extract_data(target)
    resp = create_response(target,data,status_code,status_msg)
    return resp

def check_target(target):
    if target == '/': target += index
    target = serv_dir + target
    error = 'errors/err.html'
    if os.path.isfile(target):
        return (target,'200','File Found')
    else:
        return (error,'404','File Not Found')

def extract_data(file):
    file = open(file,'rb')
    data = file.read()
    file.close()
    return data

def open_log(log_file):
    file = log_file
    if os.path.isfile(file):
        file = open(file,'a')
    else:
        file = open(file,'w')
    return file

def write_log(file,ip,status,target,useragent):
    file.write(f'{datetime.now().isoformat()} {status} {ip[0]}:{ip[1]} {target} {useragent}\n')

def close_log(log_file):
    log_file.close()
