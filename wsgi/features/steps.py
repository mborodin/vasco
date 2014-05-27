from vasco import app
from lettuce import step, world, before, after
from nose.tools import assert_equals, assert_true


@before.each_scenario
def setUp(scenario):
    world.app = app
    world.client = world.app.test_client()


@after.each_scenario
def tearDown(scenario):
    del world.client
    del world.app

@step('I have selected to sign up with (.*)')
def select_provider(step, provider):
    world.provider = provider


@step('I submit login (.*) and password (.*)')
def provide_credentials(step, login, password):
    world.login = login
    world.password = password


@step('I got signed up and user profile is created with name (.*) and profile picture (.*)')
def test_user_signup(step, name, userpic):
    app = world.app
    client = world.client
    rv = client.get('/signup/%s' % world.provider.lower())
    assert_equals(rv.status_code, 301)
    assert_equals(rv.headers['Location'], 'http')
    assert_true(False)
