*** Settings ***
Documentation           Robot Framework
Library                 Selenium2Library


*** Variables ***
${SERVER}               https://www.google.com
${BROWSER}              Firefox
${DELAY}                1
${TEXT}                 name:q
${PYTHON}               Python
${SEARCH}               name:btnK

*** Keywords ***
Search in Google
    Open Browser        ${SERVER}   ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Input Text          ${TEXT}     ${PYTHON}
    Click Element       ${SEARCH}



*** Test Cases ***
Search
    Search in Google
    [Teardown]    Close Browser