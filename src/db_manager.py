import couchdb

class DBManager:
    def __init__(self, db_config):
        self.server = couchdb.Server(f"http://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/")
        self.db = self.server[db_config['dbname']]

    def read_from_db(self, doc_id):
        doc = self.db.get(doc_id)
        return doc

    def write_to_db(self, doc):
        self.db.save(doc)
