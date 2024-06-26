*** Settings ***
Library    REST    http://localhost:8000
Library    DatabaseLibrary 
Suite Setup    Connect To Database    psycopg2    ${db_name}    ${db_user}    ${db_password}    ${db_host}    ${db_port}
Documentation     Test cases for the PUT /doctor/id endpoint
Variables    variables.py

*** Variables ***
${api_url}            http://localhost:8000
${db_name}        medical_directory
${db_user}        postgres
${db_password}    Pruebas12345
${db_host}        localhost
${db_port}        5432

*** Test Cases ***
test-api-31 PUT an valid doctor
    PUT    /doctor/2    ${valid_doctor_put}
    Integer    response status    200
    String    response body name    ${valid_doctor_put}[name]
    String    response body lastname    ${valid_doctor_put}[lastname]
    String    response body rut    ${valid_doctor_put}[rut]
    String    response body city    ${valid_doctor_put}[city]
    Check If Exists In Database    SELECT * FROM doctors WHERE rut = '${valid_doctor_put}[rut]'and name = '${valid_doctor_put}[name]' and lastname = '${valid_doctor_put}[lastname]' and city = '${valid_doctor_put}[city]';

test-api-32 PUT an invalid doctor without name
    PUT    /doctor/2    ${doctor_without_name}
    Integer    response status    422

test-api-33 PUT an invalid doctor without lastname
    PUT    /doctor/2    ${doctor_without_lastname}
    Integer    response status    422

test-api-34 PUT an invalid doctor without rut
    PUT    /doctor/2    ${doctor_without_rut}
    Integer    response status    422

test-api-35 PUT an invalid doctor without city
    PUT    /doctor/2    ${doctor_without_city}
    Integer    response status    422

test-api-36 PUT a unexisting doctor
    PUT    /doctor/9999    ${valid_doctor_put}
    Integer    response status    404

test-api-39 PUT a doctor with invalid rut
    PUT    /doctor/2    ${doctor_with_invalid_rut}
    Integer    response status    422

test-api-40 PUT a doctor with invalid email
    PUT    /doctor/2    ${doctor_with_invalid_email}
    Integer    response status    422