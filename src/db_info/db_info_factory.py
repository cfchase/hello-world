from .pg_info import PgInfo
from .my_sql_info import MySqlInfo
from .ms_sql_info import MSSqlInfo
from .db_info import DbInfo


def get_db_info(db_type, db_host, db_port, db_name, db_user, db_password, db_admin_user, db_admin_password):
    info = DbInfo()
    if db_type and db_type.find('postgres') >= 0:
        info = PgInfo(db_host, db_port, db_name, db_user, db_password)
    elif db_type and db_type.find('mysql') >= 0:
        info = MySqlInfo(db_host, db_port, db_name, db_user, db_password)
    elif db_type and db_type.find('mssql') >= 0:
        info = MSSqlInfo(db_host, db_port, db_name, db_admin_user, db_admin_password)

    info.get_info()
    return info
