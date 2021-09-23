#!/bin/bash

# This script display a total count of logins by user and IP address, from the current and previous month,
# using the LAST command, sorted by user in alphabetical order.

# Author: Marcelo Monteiro da Silva
# Lab Interview
# Date: 22/09/2021
# Version: 1.0

echo "Login report since August 1st on the server: $(uname -n)"
echo ""
# Search for any user that logged in the system since 2021-08-01
echo "$(last --since 2021-08-01 -i | awk '{if ($1 != "reboot" && $1 != "wtmp" && $1 != "") print $1 " "$3}' | sort -nk1 | uniq -c)"

# Code example to search for two specific users, adaminato and fcharlebois.
#echo "$(last --since 2021-08-01 -i | awk '{if ($1 == "adaminato" || $1 == "fcharlebois") print $1 " "$3}' | sort -nk1 | uniq -c)"