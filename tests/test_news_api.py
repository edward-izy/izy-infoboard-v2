import json

from tests.utils.base import BaseTestCase
from tests.utils.common import register_user, login_user, get_all_news, post_news, update_news, get_token
from tests.utils.data_dicts import DataDicts


class TestNewsBlueprint(BaseTestCase):
    # def test_post_news(self):
    #     """ Test post_news Endpoint """
    #     # Add user and get access_token
    #     token = get_token(self)
    #
    #     # Test post_news
    #     post_response = post_news(self, DataDicts.news, token)
    #     self.assertEquals(post_response.status_code, 200)
    #
    # def test_get_all(self):
    #     """ Test get_all Endpoint """
    #     # Add user and get access_token
    #     token = get_token(self)
    #
    #     # Add data
    #     post_news(self, DataDicts.news, token)
    #
    #     # Test get_all
    #     get_response = get_all_news(self, token)
    #     self.assertEquals(get_response.status_code, 200)

    def test_update_news(self):
        """ Test update_news Endpoint """
        # Add user and get access_token
        token = get_token(self)
        # print(token)
        print(json.dumps(DataDicts.news))
        # Add news_post
        response = post_news(self, DataDicts.news, token)

        print("*********************")
        print(json.loads(response.data))
        print("*********************")
        #
        # self.assertEquals(response.status_code, 200)
        # response = update_news(self, DataDicts.update_news, token)
        # print("*********************")
        # print(response.data)
        # print("*********************")
        # self.assertEquals(response.status_code, 200)
