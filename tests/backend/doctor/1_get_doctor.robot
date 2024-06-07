*** Settings ***
Library    REST    http://localhost:8000
Documentation     Test cases for the GET /doctor/{id} endpoint
Variables    variables.py

*** Variables ***
${api_url}            http://localhost:8000

*** Test Cases ***
test-api-9 Get an existing doctor by id
    GET     /doctor/1
    Object    response body
    String    response body name    ${data}[doctors][0][name]
    String    response body lastname    ${data}[doctors][0][lastname]
    String    response body email    ${data}[doctors][0][email]
    String    response body phone    ${data}[doctors][0][phone]
    String    response body birthdate    ${data}[doctors][0][birthdate]
    String    response body city    ${data}[doctors][0][city]
    Integer    response status    200


test-api-10 Get a non-existing doctor by id
    GET     /doctor/1000
    Object    response body
    String    response body error    Doctor not found
    Integer    response status    404