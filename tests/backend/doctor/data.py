import psycopg2
import json

conn = psycopg2.connect(
    dbname='medical_directory',
    user='postgres',
    password='Pruebas12345',
    host='localhost',
    port='5432'
)

cur = conn.cursor()

with open('initial_data.json') as file:
    data = json.load(file)

# Insert especialties
for specialty in data['specialties']:
    cur.execute(
        'INSERT INTO specialties (name) VALUES (%s)',
        (specialty['name'],)
    )

conn.commit()

# Insert doctors
for doctor in data['doctors']:
    cur.execute(
        'INSERT INTO doctors (name, lastname, rut, email, phone, birthdate, city) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id',
        (doctor['name'], doctor['lastname'], doctor['rut'], doctor['email'], doctor['phone'], doctor['birthdate'], doctor['city'])
    )
    doctor_id = cur.fetchone()[0]

    # Insert doctor_specialties
    for specialty in doctor['specialties']:
        cur.execute(
            'INSERT INTO doctor_specialties (doctor_id, specialty_id) VALUES (%s, %s)',
            (doctor_id, specialty)
        )

    # Insert experiences
    for experience in doctor['experiences']:
        cur.execute(
            'INSERT INTO experiences (job_title, description, institution, city, country, start_date, end_date, doctor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (experience['job_title'], None, experience['institution'], experience['city'], experience['country'], experience['start_date'], experience['end_date'], doctor_id)
        )

    # Insert educations
    for education in doctor['educations']:
        cur.execute(
            'INSERT INTO educations (degree, description, institution, city, country, start_date, end_date, doctor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (education['degree'], None, education['institution'], education['city'], education['country'], education['start_date'], education['end_date'], doctor_id)
        )

conn.commit()
cur.close()
conn.close()


