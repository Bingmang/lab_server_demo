from .. import utils
from ..config import table

class Paper():

    def __init__(self):
        self.collection = table.paper
        self.conn = utils.mongo.db.get_collection(self.collection)

    def list(self):
        pass


paper = Paper()
