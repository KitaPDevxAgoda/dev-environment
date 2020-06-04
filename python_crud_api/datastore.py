import pyodbc
from mail import Mail

def make_connection():
    return pyodbc.connect('Driver={SQL Server};'
                    'Server=master;'
                    'Database=tempdb;'
                    'Trusted_Connection=yes;')

def create_mail(subject: str):
    conn = make_connection()
    cursor = conn.cursor()

    sql = ('INSERT INTO tempdb.dbo.MAIL (mai_subject) VALUES (%s);' % (subject))

    cursor.execute(sql)
    cursor.close()

def read_all():
    conn = make_connection()

    cursor = conn.cursor()
    cursor.execute('SELECT mai_id, mai_subject FROM tempdb.dbo.MAIL')

    mails = []

    for row in cursor.fetchall():
        mail = Mail(0, '')

        mail.id = row.mai_id
        mail.subject = row.mai_subject

        if mail.id != 0:
            mails.append(mail)

    cursor.close()
    return mails

def update_mail(id: int, subject: str):
    conn = make_connection()

    sql = ('UPDATE tempdb.dbo.MAIL SET mai_subject = %s WHERE mai_id = %d' % (subject, id))

    cursor = conn.cursor(sql)
    cursor.execute()
    cursor.close()


def delete_mail(id: int):
    conn = make_connection()

    sql = ('DELETE FROM tempdb.dbo.MAIL WHERE mai_id = %d' % (id))

    cursor = conn.cursor(sql)
    cursor.execute()
    cursor.close()
