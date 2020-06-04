import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=master;'
                      'Database=tempdb;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM tempdb.dbo.MAIL')