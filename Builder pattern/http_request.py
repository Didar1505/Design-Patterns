class HttpRequest:
    def __init__(self):
        self.url = ''
        self.method = "GET"
        self.headers = {}
        self.params = {}
        self.body = None
        self.timeout = 10

    def __str__(self):
        return (
            f"--- HTTP Request ---\n"
            f"  {self.method} {self.url}\n"
            f"  Headers: {self.headers}\n"
            f"  Params: {self.params}\n"
            f"  Body: {self.body}\n"
            f"  Timeout: {self.timeout}s"
        )
    def __repr__(self):
        return str(self.url)

class RequestBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._request = HttpRequest()

    def with_url(self, url):
        self._request.url = url
        return self
    
    def with_method(self, method):
        self._request.method = method
        return self
    
    def add_header(self, key, value):
        self._request.headers[key] = value
        return self

    def add_query_param(self, key, value):
        self._request.params[key] = value
        return self

    def set_json_body(self, data):
        import json 
        self._request.body = json.dumps(data)
        self.add_header('Content-Type', "application/json")
        return self

    def set_timeout(self, seconds):
        self._request.timeout = seconds
        return self

    def build(self):
        final = self._request
        self.reset()
        return final
    


builder = RequestBuilder()
search_request = builder \
.with_url("https://api.example/com/search") \
.with_method("POST") \
.add_query_param("q", 'design patterns') \
.add_query_param("page", 2) \
.build()

print(search_request)
