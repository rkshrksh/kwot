import json
import random
import pkg_resources

resource_package = __name__
resource_path = 'quotes.json'
qfile = pkg_resources.resource_stream(resource_package, resource_path)

def get_quote(n=1):
    data = json.load(qfile)
    return random.choices(list(data), k=n)