*** Settings ***
Library    REST    http://localhost:8000
Library    DatabaseLibrary 
Suite Setup    Connect To Database    psycopg2    ${db_name}    ${db_user}    ${db_password}    ${db_host}    ${db_port}
Documentation     Test cases for the DELETE /doctor endpoint
Variables    variables.py

*** Variables ***
${api_url}            http://localhost:8000
${db_name}        medical_directory
${db_user}        postgres
${db_password}    Pruebas12345
${db_host}        localhost
${db_port}        5432

*** Test Cases ***
test-api-29 DELETE an existing doctor
    DELETE    /doctor/5
    Integer    response status    200
    Check If Not Exists In Database    SELECT * FROM doctors WHERE id = 5

test-api-30 DELETE a non-existing doctor
    DELETE    /doctor/100
    Integer    response status    404
    String    response body error    Doctor not found