import pymssql
from mail import Mail
import os


def make_connection():
    return pymssql.connect(server=os.environ['DB_SERVER'],
                           user=os.environ['DB_USER'],
                           password=os.environ['DB_PASSWORD'],
                           database=os.environ['DB_NAME'])


def create_mail(subject: str):
    conn = make_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tempdb.dbo.MAIL (mai_subject) VALUES (%s);", subject)
    cursor.close()
    conn.commit()
    conn.close()


def read_all():
    conn = make_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT mai_id, mai_subject FROM tempdb.dbo.MAIL;")

    mails = []

    for row in cursor.fetchall():
        mail = Mail(0, '')

        mail.id = row[0]
        mail.subject = row[1]

        if mail.id != 0:
            mails.append(mail)

    cursor.close()
    conn.close()
    return mails


def update_mail(id: int, subject: str):
    conn = make_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE tempdb.dbo.MAIL SET mai_subject = %s WHERE mai_id = %d", (subject, id))
    cursor.close()
    conn.commit()
    conn.close()


def delete_mail(id: int):
    conn = make_connection()
    cursor = conn.cursor()

    sql = ("DELETE FROM tempdb.dbo.MAIL WHERE mai_id = %d" % id)

    cursor.execute(sql)
    cursor.close()
    conn.close()
