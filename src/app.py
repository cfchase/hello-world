from bottle import route, run, get, static_file, template, view, debug
import os
from db_info.db_info_factory import get_db_info


@route('/')
@view('index')
def index():
    db_type = os.environ.get('DB_TYPE')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    db_info = get_db_info(db_type, db_host, db_port, db_name, db_user, db_password)

    return dict(db_type=db_info.db_type_label,
                host=db_info.host,
                port=db_info.port,
                database=db_info.database,
                user=db_info.user,
                db_version=db_info.version,
                uptime=db_info.uptime,
                conn_count=db_info.connection_count,
                error=db_info.error)


# For Static files
@get("/static/css/<filename:re:.*\.css>")
def css(filename):
    return static_file(filename, root="static/css")


@get("/static/font/<filename:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filename):
    return static_file(filename, root="static/font")


@get("/static/img/<filename:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filename):
    return static_file(filename, root="static/img")


@get("/static/js/<filename:re:.*\.js>")
def js(filename):
    return static_file(filename, root="static/js")


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
