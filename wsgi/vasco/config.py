import os

try:
    environ = os.environ['VASCO_ENV']
except:
    environ = 'dev'

configs = {
    'production': {
        'providers': {
            'facebook': {
                'appId': '',
                'secret': ''
            }
        }
    },
    'dev': {
        'providers': {
            'facebook': {
                'appId': '499586600168548',
                'secret': '4d2685de6954f66399c0728e9258a104',
                'request': {
                    'scope': 'public_profile,email,user_friends'
                },
                'url': 'https://graph.facebook.com',
                'token_url': '/oauth/access_token',
                'authorize_url': 'https://www.facebook.com/dialog/oauth'
            }
        },
        'secret_key': '8XIGB0t+D27gYyBYVv3/hQD9P8RFPYMxrF7o0Vy5iYmEEgS6LILppg',
        'server_name': 'vasco.local'
    }
}

config = configs[environ]
