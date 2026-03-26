*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000/
${BROWSER}    Chrome

*** Test Cases ***
Navegacion Principal Del Sistema
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Page Should Contain    Bienvenido

    Click Element    xpath=//a[contains(@href, 'notas.html')]
    Wait Until Page Contains    Próximamente

    Click Element    xpath=//a[contains(@href, 'index.html')]
    Wait Until Page Contains    Bienvenido

    Click Element    xpath=//a[contains(@href, 'estadistica.html')]
    Wait Until Location Contains    estadistica.html

    Close Browser