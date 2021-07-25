from keyring import get_password
from dataclasses import dataclass, field
from abc import ABC
from google.oauth2.service_account import Credentials as GoogleCredentials


class CredentialNotFoundError(Exception):
    """Exception when the data warehouse credentials were not found in
    the keyring.

    """
    def __init__(self, credential_name: str):
        self.message = f'''
            "{credential_name}" was not been found in Keyring, please set them following the README.
        '''
        super().__init__(self.message)


@dataclass
class Credential(ABC):
    """ Abstract class for handling log-in credentials for database connnection.
    """
    def __init__(self):
        pass


@dataclass
class GBQCredential(Credential):
    """ Credential class for Google Big Query.
    """
    credentials: GoogleCredentials

    def __init__(self, credential_file_path: str) -> GoogleCredentials:
        self.credentials = GoogleCredentials.from_service_account_file(credential_file_path)


@dataclass
class DataWarehouseCredential(Credential):
    """Credential class for  data warehouse.
    """
    username: str
    password: str
    database: str=field(default='redshift')

    def __init__(self, database: str) -> None:
        self.database = database
        self.username = get_password(f'{self.database}', 'username')
        if not self.username:
            raise CredentialNotFoundError(credential_name='username')
        self.password = get_password(f'{self.database}', self.username)
        if not self.password:
            raise CredentialNotFoundError(credential_name='password')


if __name__ == '__main__':
    mssql_cred = DataWarehouseCredential(database='mssql')
    redshift_cred = DataWarehouseCredential(database='redshift')
    gbq_cred = GBQCredential(credential_file_path='fabled-autonomy-89301-3b32ec51e147.json')
    print(mssql_cred)
    print(redshift_cred)
    print(gbq_cred)
