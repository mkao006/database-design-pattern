from abc import ABC, abstractmethod
from sqlalchemy import create_engine
import pandas as pd
from dbdp.config import Configuration
from dbdp.credential import Credential


class Connection(ABC):
    def __init__(self,
                 credential: Credential,
                 configuration: Configuration):
        self.credential = credential
        self.configuration = configuration

    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class DataWarehouseConnection(Connection):
    def create_connection(self) -> None:
        self.connection = create_engine(
            self.configuration.connection_string.format(
                self.credential.username,
                self.credential.password,
                self.configuration['server'],
                self.configuration['port'],
                self.configuration['database']
            )
        )

    def get_data(self, query: str) -> pd.DataFrame:
        return pd.read_sql(query, self.connection)


class GBQConnection(Connection):
    def create_connection(self):
        pass

    def get_data(self, query: str) -> pd.DataFrame:
        return pd.read_gbq(
            query=query,
            project_id=self.config.project_id,
            dialect='standard',
            credentials=self.credential,
        )


if __name__ == '__main__':
    from dbdp.config import DataWarehouseConfig
    from dbdp.credential import DataWarehouseCredential

    mssql_con = DataWarehouseConfig(
        credential=DataWarehouseCredential(database='mssql'),
        configuration=DataWarehouseConfig(
            data_source='mssql',
            env='prod',
            config_file_path='dbdp_config.yml')
    )

    mssql_con.get_data('SELECT TOP 10 * FROM ds_Mkt_users')

    redshift_con = DataWarehouseConfig(
        credential=DataWarehouseCredential(database='redshift'),
        configuration=DataWarehouseConfig(
            data_source='redshift',
            env='prod',
            config_file_path='dbdp_config.yml')
    )

    redshift_con.get_data('SELECT TOP 10 * FROM ds_Mkt_users')
