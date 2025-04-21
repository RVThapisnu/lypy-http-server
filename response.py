import mimetypes

mimetypes.init()

def parse_request(req):
    splitted = req.split('\r\n')
    request = {
            "start-line" : get_startline(splitted[0]),
            "headers" : get_headers(splitted[1:-2]),
            "data" : splitted[-1]
            }
    return request

def get_startline(req):
    startline = {
        "method" : get_method(req),
        "target" : get_target(req),
        "protocol" : get_protocol(req)
            }
    return startline

def get_headers(req):
    headers = {}
    for s in req:
        data = s.split(':',1)
        headers[data[0].strip()] = data[1].strip()
    return headers

def get_method(req):
    method = req.split()[0]
    return method

def get_target(req):
    target = req.split()[1]
    return target

def get_protocol(req):
    protocol = req.split()[2]
    return protocol

def create_response(target,data,status_code,status_msg):
    startline = create_startline('HTTP/1.1',status_code,status_msg)
    headers = create_headers(target,data)
    response = startline + headers + data 
    return response

def create_startline(proto,status_code,status_msg):
    startline = f'{proto} {status_code} {status_msg}\r\n'
    startline = startline.encode()
    return startline

def create_headers(target,data):
    headers = (
            f"Server: Lightning\r\n"
            f"Content-Type: {mimetypes.guess_type(target)[0]}\r\n"
            f"Content-Length: {find_contentLength(data)}\r\n"
            "\r\n"
        )
    headers = headers.encode()
    return headers

def find_contentLength(data):
    length = len(data)
    return length
