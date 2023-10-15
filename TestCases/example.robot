*** Settings ***
Library    SeleniumLibrary   run_on_failure=Capture Screenshot
Variables   ../PageObjects/pageLocators.py
Resource    ../keywords/keywords.robot
Library    ../utility.py


*** Variables ***

${browserName}    chrome
${driver_path}=    utility.Get Driver Path with Browser Name ${browserName}
${url}     https://the-internet.herokuapp.com

*** Test Cases ***
Login to the Application and Log Out
    [tags]  regression
    set selenium implicit wait    20 sec
    open browser    ${url}    chrome    executable_path=${driver_path}
    Navigate on Login Page
    Login to the Application
    Capture Screenshot
    Log Out From the Application

