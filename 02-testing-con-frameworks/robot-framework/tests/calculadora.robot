*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://127.0.0.1:5000/calculadora.html
${BROWSER}    Chrome

*** Test Cases ***
Calculadora Con Datos Validos
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Element Is Visible    id=datos
    Input Text    id=datos    4,8,15,16,23,42

    Click Button    xpath=//button[contains(., 'Calcular')]

    Wait Until Element Is Visible    id=resultados
    Element Should Contain    id=resultados    Media:
    Element Should Contain    id=resultados    18.00
    Element Should Contain    id=resultados    Mediana:
    Element Should Contain    id=resultados    15.50
    Element Should Contain    id=resultados    Varianza:
    Element Should Contain    id=resultados    151.67
    Element Should Contain    id=resultados    Desv. Estándar:
    Element Should Contain    id=resultados    12.32

    Close Browser