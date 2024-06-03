import psycopg2

conn = psycopg2.connect(
    dbname='medical_directory',
    user='postgres',
    password='Pruebas12345',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

cur.execute('TRUNCATE TABLE doctor_specialties, experiences, educations, doctors, specialties RESTART IDENTITY CASCADE')
conn.commit()
cur.close()
conn.close()