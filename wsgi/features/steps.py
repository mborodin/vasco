from vasco import app, login, localization
from lettuce import step, world, before, after
from nose.tools import assert_equals, assert_true
try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse
import requests
import json


@before.each_scenario
def setUp(scenario):
    world.app = app
    world.client = app.test_client()


@after.each_scenario
def tearDown(scenario):
    del world.app
    del world.client


@step('I have selected to sign up with (.*)')
def select_provider(step, provider):
    world.provider = provider


@step('I have received provider credentials by submitting login (.*) and password (.*) to (.*)')
def provide_credentials(step, login, password, url):
    session = requests.Session()
    response = session.post(url, data={'email': login, 'pass': password})
    for cookie in response.cookies:
        params = {'server_name': urlparse(url).hostname,
                  'key': cookie.name,
                  'value': cookie.value,
                  'expires': cookie.expires
                  }
        if cookie.domain_specified:
            params['domain'] = cookie.domain
        if cookie.path_specified:
            params['path'] = cookie.path
        if cookie.secure:
            params['secure'] = True
        if cookie.has_nonstandard_attr('httponly'):
            params['httponly'] = True

        world.client.set_cookie(**params)


@step('I try to login')
def try_login(step):
    client = world.client
    rv = client.get('/login/%s' % world.provider.lower())
    world.response = rv
    #assert_equals(rv.status_code, 200)


@step('Follow location redirect')
def follow_redirect(step):
    rv = world.response
    client = world.client
    cookies = {}
    for cookie in client.cookie_jar:
        cookies[cookie.name] = cookie.value
    rv = requests.get(rv.headers['Location'], cookies=cookies)
    print(rv.content)
    assert_true(False)


@step('I got signed in')
def check_signed_in(step):
    client = world.client
    rv = client.get('/profile')
    assert_equals(rv.status_code, 200)


@step('My profile has name (.*) and avatar (.*)')
def test_user_signup(step, name, userpic):
    client = world.client
    rv = client.get('/api/profile')
    assert_equals(rv.status_code, 200)
    profile = json.loads(rv.get_data(True))
    assert_equals(profile['name'], name)
    assert_equals(profile['userpic'], userpic)


@step('I got response code (.*)')
def test_response_code(step, _code):
    code = int(_code)
    rv = world.response
    assert_equals(rv.status_code, code)


# TODO: This is hack. app should reside in own package, which should be loaded
# with vasco
make_pep8_happy = login
make_pep8_happy = localization
