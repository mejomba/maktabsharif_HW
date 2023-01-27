import configparser
from project_exceptions import InsertDoctorException
import psycopg2


confFile = configparser.ConfigParser()
confFile.read('db.conf')
database = confFile['DB']['main_db']
host = confFile['DB']['host']
port = confFile['DB']['port']
user = confFile['DB']['user']
password = confFile['DB']['pass']




def get_connection():
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as connect:
        connect.autocommit = True
        return connect


def insert_doctor(doctor_name):
    # query = "INSERT INTO {0} (doctor_name) VALUES('{1}') RETURNING doctor_id".format('doctor', doctor_name)
    query = "INSERT INTO doctor (doctor_name) VALUES(%s) RETURNING doctor_id, doctor_name"
    param = doctor_name,
    with get_connection().cursor() as cur:
        try:
            cur.execute(query, param)
            res = cur.fetchone()
            print(f'insert {res}')
        except(InsertDoctorException, psycopg2.Error) as err:
            print(err)



insert_doctor('zahra')



# conn = psycopg2.connect(host=host, port=db_port, dbname=db_name, user=uname, password=dbpasswd)
# cur = conn.cursor()
#
#
# cur.close()
# conn.close()


# try:
#     conn = psycopg2.connect(host=host, port=db_port, dbname=db_name, user=uname, password=PASSWORD)
#
#     cur = conn.cursor()
#     print('try')
# except (Exception, psycopg2.Error) as err:
#     print(f'ERROR: ', err)
#     records = 0
# finally:
#     if (conn):
#         cur.close()
#         conn.close()