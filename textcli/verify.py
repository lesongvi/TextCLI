
from urllib.request import Request
from urllib import request
import json
import random

class Verify:
    def __init__(self, token: str):
        self.token = token
        self.verify = 'https://api.rqn9.com/data/1.0/vtoken/'
        self.user_agents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
        ]

    def dev_info(self):

        request_obj = Request(self.verify + self.token + '&vtoken=' + self.token, headers = {'User-Agent': self.user_agents[random.randint(0,7)]})
        response_obj = request.urlopen(request_obj)

        try:
            check = json.loads(response_obj.read().decode('utf-8'))
            
            if check is None:
                return False
            elif 'status' in check:
                if check['status'] == 'success':
                    return True
                else:
                    return False
        except Exception as e:
            return False

        return