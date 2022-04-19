import json

from tests.utils.base import BaseTestCase
from tests.utils.common import get_token, get_all_sfa, post_sfa, update_sfa, get_by_sprint_sfa
from tests.utils.data_dicts import DataDicts


class TestNewsBlueprint(BaseTestCase):
    def test_post_sfa(self):
        """ Test post_news Endpoint """
        # Add user and get access_token
        token = get_token(self)

        # Test post_sfa
        post_response = post_sfa(self, DataDicts.post_sfa, token)
        self.assertEquals(post_response.status_code, 200)

    def test_get_all(self):
        """ Test get_all Endpoint """
        # Add user and get access_token
        token = get_token(self)

        # Add data
        post_sfa(self, DataDicts.post_sfa, token)

        # Test get_all
        get_response = get_all_sfa(self, token)
        self.assertEquals(get_response.status_code, 200)

    def test_update_sfa(self):
        """ Test update_news Endpoint """
        # Add user and get access_token
        token = get_token(self)

        # Add news_post
        post_sfa(self, DataDicts.post_sfa, token)

        response = update_sfa(self, DataDicts.update_sfa, token)
        self.assertEquals(response.status_code, 200)

    def test_get_by_sprint_sfa(self):
        """ Test update_news Endpoint """
        # Add user and get access_token
        token = get_token(self)

        # Add news_post
        post_sfa(self, DataDicts.post_sfa, token)

        response = get_by_sprint_sfa(self, token)
        self.assertEquals(response.status_code, 200)
