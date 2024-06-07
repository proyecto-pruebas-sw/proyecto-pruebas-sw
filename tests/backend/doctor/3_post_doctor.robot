*** Settings ***
Library    REST    http://localhost:8000
Library    DatabaseLibrary 
Suite Setup    Connect To Database    psycopg2    ${db_name}    ${db_user}    ${db_password}    ${db_host}    ${db_port}
Documentation     Test cases for the POST /doctor endpoint
Variables    variables.py

*** Variables ***
${api_url}            http://localhost:8000
${db_name}        medical_directory
${db_user}        postgres
${db_password}    Pruebas12345
${db_host}        localhost
${db_port}        5432

*** Test Cases ***
test-api-11 POST an valid doctor
    POST   /doctor    ${valid_doctor}
    Integer    response status    201
    String    response body name    ${valid_doctor}[name]
    String    response body lastname    ${valid_doctor}[lastname]
    String    response body rut    ${valid_doctor}[rut]
    String    response body city    ${valid_doctor}[city]
    Check If Exists In Database    SELECT * FROM doctors WHERE rut = '${valid_doctor}[rut]'and name = '${valid_doctor}[name]' and lastname = '${valid_doctor}[lastname]' and city = '${valid_doctor}[city]';

test-api-12 POST an invalid doctor without name
    POST   /doctor    ${doctor_without_name}
    Integer    response status    422

test-api-13 POST an invalid doctor without lastname
    POST   /doctor    ${doctor_without_lastname}
    Integer    response status    422

test-api-14 POST an invalid doctor without rut
    POST   /doctor    ${doctor_without_rut}
    Integer    response status    422

test-api-15 POST an invalid doctor without city
    POST   /doctor    ${doctor_without_city}
    Integer    response status    422

test-api-16 POST an invalid doctor without specialties
    POST   /doctor    ${doctor_without_specialties}
    Integer    response status    422

test-api-17 POST an invalid doctor with an experience without job_title
    POST   /doctor    ${doctor_without_experience_job_title}
    Integer    response status    422

test-api-18 POST an invalid doctor with an experience without institution
    POST   /doctor    ${doctor_without_experience_institution}
    Integer    response status    422

test-api-19 POST an invalid doctor with an experience without city
    POST   /doctor    ${doctor_without_experience_city}
    Integer    response status    422

test-api-20 POST an invalid doctor with an experience without country
    POST   /doctor    ${doctor_without_experience_country}
    Integer    response status    422

test-api-21 POST an invalid doctor with an experience without start_date
    POST   /doctor    ${doctor_without_experience_start_date}
    Integer    response status    422

test-api-22 POST an invalid doctor with an experience without end_date
    POST   /doctor    ${doctor_without_experience_end_date}
    Integer    response status    422

test-api-23 POST an invalid doctor with an education without degree
    POST   /doctor    ${doctor_without_education_degree}
    Integer    response status    422

test-api-24 POST an invalid doctor with an education without institution
    POST   /doctor    ${doctor_without_education_institution}
    Integer    response status    422

test-api-25 POST an invalid doctor with an education without city
    POST   /doctor    ${doctor_without_education_city}
    Integer    response status    422

test-api-26 POST an invalid doctor with an education without country
    POST   /doctor    ${doctor_without_education_country}
    Integer    response status    422

test-api-27 POST an invalid doctor with an education without start_date
    POST   /doctor    ${doctor_without_education_start_date}
    Integer    response status    422

test-api-28 POST an invalid doctor with an education without end_date
    POST   /doctor    ${doctor_without_education_end_date}
    Integer    response status    422



