from pip._vendor import requests

class Client:
    def __init__(self, host):
        self._session=requests.Session()
        self._host=host
        payload = {'key1': 'value1', 'key2': 'value2'}
        answ=requests.get(host, params=payload)
        print(answ.url)
        print(answ.headers)
        print(answ.request.headers)
    def __del__(self):
        self._session.close()

Client('https://httpbin.org/get')