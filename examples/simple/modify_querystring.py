from mitmproxy import http
import re
import json
import sys
sys.path.append('../')
from connect import sendDataToFire

def request(flow: http.HTTPFlow) -> None:
    data = {}
    #data['time'] = flow.request.timestamp_start
    ######################################################################
    if flow.request.url[:32] == "https://www.google.co.in/search?" and flow.request.method == 'GET' :
        
        #data['From'] = "Google search"
        s = flow.request.path
        s = s[s.find('q=')+2:]
        s = s[:s.find('&')]
        data['QueryG'] = s.replace('+', ' ')
        json_dg = json.dumps(data)
        sendDataToFire(json_dg, 'Google')#[data.find('&q=')+1: data.find('&')])
    ########################################################################
    elif (flow.request.url[:50] == "https://suggestqueries.google.com/complete/search?" and flow.request.method == 'GET'):
        ys = flow.request.path
        ys = ys[ys.find('q=')+2:]
        ys = ys[:ys.find('&')]
        data['QueryY'] = ys.replace('+', ' ')
        json_dy = json.dumps(data)
        sendDataToFire(json_dy, 'YouTube')#[data.find('&q=')+1: data.find('&')])
    ######################################################################

    else:
        if flow.request.method == 'GET':            
            data['Website'] = flow.request.host
            json_dw = json.dumps(data)
            sendDataToFire(json_dw, 'Visited-websites')



    # data['url'] = flow.request.url 
    # json_data = json.dumps(data)
    # sendDataToFire(json_data, 'Visited-websites')