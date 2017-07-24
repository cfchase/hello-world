from .db_info import DbInfo
import psycopg2


class PgInfo(DbInfo):
    db_type_label = 'PostgreSQL'

    def __init__(self, host, port, database, user, password):
        super().__init__()
        self.host = host
        self.port = port or 5432
        self.database = database
        self.user = user
        self.password = password
        self.connector = psycopg2

    def query_version(self):
        return self.query("""SELECT VERSION()""", 0, 0)

    def query_uptime(self):
        return self.query("""SELECT current_timestamp - pg_postmaster_start_time() AS uptime""", 0, 0) + "seconds"

    def query_connection_count(self):
        return self.query("""SELECT sum(numbackends) FROM pg_stat_database;""", 0, 0)
