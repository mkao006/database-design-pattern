import os
from pathlib import Path
import yaml
from typing import Dict
from dataclasses import dataclass, field
from abc import ABC


@dataclass
class Configuration(ABC):
    config: Dict


@dataclass
class DataWarehouseConfig(Configuration):
    data_source: str=field(default='redshift')
    env: str=field(default='prod')

    def __init__(self,
                 data_source: str,
                 env: str,
                 config_file_path: str,
                 search_parent_dir: bool=True) -> None:
        self.data_source = data_source
        self.search_parent_dir = search_parent_dir
        self.config_file_path = config_file_path
        self._set_connection_string()
        self.load_config()

    def _set_connection_string(self) -> None:
        if self.data_source == 'mssql':
            self.connection_string = 'mssql+pyodbc://{}:{}@{}:{}/{}?driver=FreeTDS'
        elif self.data_source == 'redshift':
            self.connection_string = 'postgresql://{}:{}@{}:{}/{}'
        else:
            raise NotImplementedError('Data source specified not implemented')

    def _collapse_config(self, config: Dict) -> Dict:
        '''The function appends the default connection to all other
        environment configuration.

        The function will append specific information such as port to the
        default configuration which are shared.

        '''

        default_config = config.pop('default', None)
        if default_config is None:
            raise ValueError('You must provide a default configuration.')

        for env_key, env_value in config.items():
            for connection_key in env_value.keys():
                configuration = default_config.get(connection_key, {})
                config[env_key][connection_key].update(configuration)

        return config

    def load_config(self) -> None:
        '''The function reads the configuration file.

        If search_parentparent is True, then the function will check all parent
        directory for the config file.

        '''
        search_path = os.getcwd()
        file_path = os.path.join(search_path, self.config_file_path)

        if self.search_parent_dir:
            while not Path(file_path).is_file():
                if len(Path(file_path).parents) > 1:
                    search_path = Path(search_path).parents[0]
                    file_path = os.path.join(search_path, self.config_file_path)
                else:
                    raise FileNotFoundError

        if Path(file_path).is_file():
            with open(file_path, 'r') as config_file:
                configurations = yaml.load(config_file, Loader=yaml.BaseLoader)

        parsed_config = self._collapse_config(configurations)
        self.config = parsed_config[self.env][self.data_source]


@dataclass
class GBQConfig(Configuration):
    def __init__(self, project_id: str) -> None:
        self.config['project_id'] = project_id


if __name__ == '__main__':
    mssql_config = DataWarehouseConfig(
        data_source='mssql',
        env='prod',
        config_file_path='dbdp_config.yml')
    print(mssql_config)
    print(mssql_config.connection_string)

    redshift_config = DataWarehouseConfig(
        data_source='redshift',
        env='prod',
        config_file_path='dbdp_config.yml')
    print(redshift_config)
    print(redshift_config.connection_string)
