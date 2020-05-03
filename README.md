# SentinelOnePy
A class that provides methods for easily interacting with the SentinelOne API.

## Getting Started

These instructions will guide you through installing dependencies and importing the class into your project.

### Dependencies

* [Python3](https://www.python.org/download/releases/3.0/)
* [requests](https://requests.readthedocs.io/en/master/)

### Installing

Install `Python3`

```
sudo apt-get install python3
```

Install Pip3

```
sudo apt-get install python3-pip
```

Install `requests`

```
sudo pip3 install requests
```

Clone the repository into your project

```
git clone https://github.com/rbcummings/sentinelone-py.git
```

Import the module into your script

```
import sentinelone-py.sentinelone as sentinelOne
```

### Authenticating with the SentinelOne API

Authenticate with the SentinelOne API using an API key

```
api = sentinelOne(
    'your-subdomain',
    {'apiKey':'your-apikey'},
    ['your-siteid-1', 'your-siteid-2]
)
```

Authenticate with the SentinelOne API using your username and password

```
api = sentinelOne(
    'your-subdomain',
    {'username':'your-username', 'password':'your-password'},
    ['your-siteid-1', 'your-siteid-2]
)
```

### Performing a request to the SentinelOne API

This example will return data for up to 1000 threats created from `February 1st, 2020` through `February 29th, 2020`, sorted by field `createdAt`, order `asc`.

Define the endpoint to which your requests should be made

```
endpoint = '/web/api/v2.0/threats'
```

Set the parameters for your request

```
parameters = {
    'createdAt__gte': '2020-02-01T00:00:00.000000Z',
    'createdAt__lte': '2020-02-29T23:59:59.999999Z',
    'sortBy': 'createdAt',
    'sortOrder': 'asc',
    'countOnly': 'false',
    'limit': 1000,
}
```

Perform the request

```
response = api.get(endpoint, parameters)
```

Do something with the response data

```
print(response)
```

There are also methods for `POST` and `PUT` requests; `api.post()` and `api.put()`. Both of these methods allow an optional third parameter, `body`, to be included with your request which should also be type `dict`.

See docstring comments in `sentinelone.py` for detailed information on parameters for these methods.
