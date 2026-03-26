*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000/
${BROWSER}    Chrome

*** Test Cases ***
La pagina de inicio Carga Correctamente
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Page Should Contain    Bienvenido
    Close Browser
