import unittest
from app.config import config, table
from app import utils


class TestMongo(unittest.TestCase):

    @staticmethod
    def test_init():
        utils.mongo.client.drop_database(config.database)

    def test_fs(self):
        message = b'lab_server_fs_test'
        _id = utils.mongo.fs.put(message)
        obj = utils.mongo.fs.get(_id)
        self.assertEquals(obj.read(), message)
