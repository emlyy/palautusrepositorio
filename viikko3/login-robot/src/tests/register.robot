*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  emly  salasana1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  testemly  salasana2
    Output Should Contain  Username taken

Register With Too Short Username And Valid Password
    Input Credentials  em  salasana3
    Output Should Contain  Username should contain atleast 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ååå  salasana4
    Output Should Contain  Username should only contain characters from a-z

Register With Valid Username And Too Short Password
    Input Credentials  emlya  sala
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  emlyaa  salasana
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Create User And Input Register Command
    Create User  testemly  pa55word
    Input Register Command
