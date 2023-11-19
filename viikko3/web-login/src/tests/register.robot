*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  emly
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  em
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Username should contain atleast 3 characters

Register With Valid Username And Invalid Password
    Set Username  emlya
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Credentials
    Register Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  emlya
    Set Password  salasana123
    Set Password Confirmation  salasana12
    Submit Credentials
    Register Should Fail With Message  Password does not match password confirmation

Login After Successful Registration
    Set Username  emly
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  emly
    Set Password  salasana123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  emlya
    Set Password  salasana123
    Set Password Confirmation  salasana12
    Submit Credentials
    Register Should Fail With Message  Password does not match password confirmation
    Go To Login Page
    Set Username  emlya
    Set Password  salasana123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login
    
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
