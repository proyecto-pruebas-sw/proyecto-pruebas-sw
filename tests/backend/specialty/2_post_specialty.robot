*** Settings ***
Library    REST    http://localhost:8000
Library    DatabaseLibrary 
Suite Setup    Connect To Database    psycopg2    ${db_name}    ${db_user}    ${db_password}    ${db_host}    ${db_port}
Documentation     Test cases for the POST /specialty endpoint
Variables    variables.py

*** Variables ***
${api_url}            http://localhost:8000
${db_name}        medical_directory
${db_user}        postgres
${db_password}    Pruebas12345
${db_host}        localhost
${db_port}        5432

*** Test Cases ***
test-specialty-2 POST an valid specialty
    POST   /specialty    ${valid_specialty}
    Integer    response status    201
    String    response body name    ${valid_specialty}[name]
    Check If Exists In Database    SELECT * FROM specialties WHERE name = '${valid_specialty}[name]';

test-specialty-3 POST an invalid specialty
    POST   /specialty    ${invalid_specialty}
    Integer    response status    422