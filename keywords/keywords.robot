*** Settings ***
Library    SeleniumLibrary

*** Variables ***

*** Keywords ***

Get All Links Count and Visit
     wait until Element is Visible    xpath://li/a
     ${AllLinksCount}    get element count    xpath://li/a
     log to console    ${AllLinksCount}    here
     FOR    ${INDEX}    IN RANGE    1    ${AllLinksCount}
            wait until keyword succeeds    60s    500s Click Element    xpath://li/${INDEX}//a
            ${currUrl}    get location
            log to console    ${currUrl}
            go to    ${url}
     END

Capture Screenshot
    capture page screenshot    filename=selenium-screenshot--(index).png
