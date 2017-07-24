

class DbInfo():
    db_type_label = None

    def __init__(self):
        self.host = ""
        self.database = ""
        self.port = ""
        self.user = ""
        self.password = ""
        self.connector = None
        self.connection = None
        self.cursor = None
        self.version = ""
        self.uptime = ""
        self.connection_count = ""
        self.error = None

    def get_info(self):
        if not self.connector:
            return
        self.error = None

        try:
            self.connection = self.connector.connect(host=self.host,
                                                     port=self.port,
                                                     database=self.database,
                                                     user=self.user,
                                                     password=self.password)
            self.cursor = self.connection.cursor()
            self.version = self.query_version()
            self.uptime = self.query_uptime()
            self.connection_count = self.query_connection_count()
        except Exception as err:
            self.error = err
            print(err)
        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

    def query_version(self):
        return self.query("""SELECT VERSION()""", 0, 0)

    def query_uptime(self):
        return self.query("""SHOW STATUS LIKE 'Uptime'""", 0, 1) + " seconds"

    def query_connection_count(self):
        return self.query("""SHOW STATUS LIKE 'Connections'""", 0, 1)

    def query(self, query_str, row, col):
        if not self.connection:
            return None

        self.cursor.execute(query_str)
        rows = self.cursor.fetchall()
        result = str(rows[row][col])
        return result
