import pymongo


class InfostudPipeline:

    def __init__(self):
        self.connection = pymongo.MongoClient(
            'localhost',
             27017
        )
        db = self.connection['Infostud']
        self.collection = db['ads_tb']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
