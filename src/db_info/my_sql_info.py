from .db_info import DbInfo
import mysql.connector


class MySqlInfo(DbInfo):
    db_type_label = 'MySql'

    def __init__(self, host, port, database, user, password):
        super().__init__()
        self.host = host
        self.port = port or 3306
        self.database = database
        self.user = user
        self.password = password
        self.connector = mysql.connector

    def query_version(self):
        return self.query("""SELECT VERSION()""", 0, 0)

    def query_uptime(self):
        return self.query("""SHOW STATUS LIKE 'Uptime'""", 0, 1) + " seconds"

    def query_connection_count(self):
        return self.query("""SHOW STATUS LIKE 'Connections'""", 0, 1)
