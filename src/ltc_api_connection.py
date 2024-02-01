import urllib.request as urlRequest
import urllib.request
import urllib.parse as urlParse
import urllib.error as urlError


def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class RemoteAPIConnection:
    def __init__(self, url):
        self.url = url
        self.connect()

    def connect(self):
        # Connect to the remote API
        pass

    def disconnect(self):
        # Disconnect from the remote API
        pass

    def send_request(self, request):
        with urllib.request.urlopen(request) as response:
            body = response.read()
        return body