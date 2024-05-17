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
test-api-11 POST a valid doctor
    POST   /doctor    ${valid_doctor}
    Integer    response status    201
    String    response body name    ${valid_doctor}[name]
    String    response body lastname    ${valid_doctor}[lastname]
    String    response body rut    ${valid_doctor}[rut]
    String    response body city    ${valid_doctor}[city]
    Check If Exists In Database    SELECT * FROM doctors WHERE rut = '${valid_doctor}[rut]'and name = '${valid_doctor}[name]' and lastname = '${valid_doctor}[lastname]' and city = '${valid_doctor}[city]';

test-api-12 POST a doctor without name
    POST   /doctor    ${doctor_without_name}
    Integer    response status    422

test-api-13 POST a doctor without lastname
    POST   /doctor    ${doctor_without_lastname}
    Integer    response status    422

test-api-14 POST a doctor without rut
    POST   /doctor    ${doctor_without_rut}
    Integer    response status    422

test-api-15 POST a doctor without city
    POST   /doctor    ${doctor_without_city}
    Integer    response status    422

test-api-16 POST a doctor without specialties
    POST   /doctor    ${doctor_without_specialties}
    Integer    response status    422