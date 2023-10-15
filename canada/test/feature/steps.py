# from lettuce import step, world, before
# from nose.tools import assert_equals
# from canada import app
#
# @before.all
# def before_all():
#     world.app = app.test_client()
#
# #from app.views import USERS
#
#
# @step(u'Given some users are in the system')
# def given_some_users_are_in_the_system(step):
#     USERS.update({'david01': {'name': 'David Sale'}})
#
# @step(u'And the following user details are returned:')
# def and_the_following_user_details(step):
# assert_equals(step.hashes, [json.loads(world.response.data)])