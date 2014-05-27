config = {
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
        }
    }
}
