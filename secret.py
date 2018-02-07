# secret.py

from requests_oauthlib import OAuth1Session
import secrets

api_key = 'y0ixbVnDfL8A6AZsfjacURKJ2'
api_secret = '7KSlSju7SSGsUbA42N5dJVYPqxBOeTDmWxCieAPQzLQxw8hb7I'

access_token = '2936703055-oMlK3ms19xFIi4ZWQ0aEH3nKNoKwIlK3rGcEmCi'
access_token_secret = 'OeygFEAPAXHbAhGJyiVFHtnCi44JV5LVz5qdiT72Tzqo5'

client_key = secrets.client_key
client_secret = secrets.client_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
print (r.text)
