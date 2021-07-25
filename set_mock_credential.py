""" This script sets mock credential for testing.
"""

import keyring

USERNAME = "username"
PASSWORD = "password"

keyring.set_password("redshift", "username", USERNAME)
keyring.set_password("redshift", USERNAME, PASSWORD)

keyring.set_password("mssql", "username", USERNAME)
keyring.set_password("mssql", USERNAME, PASSWORD)
