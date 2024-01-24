#!/usr/bin/python3
"""Login session test."""

import logging
import sys

from pyajax.ajax_manager import AjaxManager

DEBUG = False

LOGIN = "email@example.it" #ONLY USER CREDENTIALS ARE SUPPORTED! DO NOT LOGIN WITH THE INSTALLER CREDENTIALS!!!
PASSWORD = "yourpassword"
USER_ROLE = "USER"
X_API_KEY = "DERFGRTHTRFHNGN/14954"


# Show debug logs to stdout
if DEBUG:
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Initialization of devices manager
manager = AjaxManager(LOGIN, PASSWORD, USER_ROLE, X_API_KEY)

# Print the session token
session_token = manager._session_token #DA RIVEDERE
print("Session Token:", session_token)
