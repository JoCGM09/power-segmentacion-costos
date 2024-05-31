#!/bin/bash
clear
    ibmcloud login --sso
token=$(ibmcloud iam oauth-tokens)
clear
python3 main.py $token
 