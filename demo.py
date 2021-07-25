from dbdp.credential import DataWarehouseCredential
from dbdp.credential import GBQCredential
from dbdp.connection import DataConnection
from dbdp.connection import GBQConnection
from dbdp.config import DataWarehouseConfig
from dbdp.config import GBQConfig

ss_test_query = 'SELECT TOP 10 * FROM ds_Mkt_users'
rs_test_query = 'SELECT * FROM elements.ds_elements_sso_users LIMIT 10'


########################################################################
#  Example for MSSQL
########################################################################

# load credentials
mssql_cred = DataWarehouseCredential(database='mssql')

# get configuration
mssql_config = DataWarehouseConfig(
    data_source='redshift',
    env='prod',
    config_file_path='dbdp_config.yml')

# create the connection
mssql_con = DataConnection(
    credential=mssql_cred,
    configuration=mssql_config
)

# Get the data
mssql_con.get_data(ss_test_query)


########################################################################
#  Example for Redshift
########################################################################

# load credentials
redshift_cred = DataWarehouseCredential(database='redshift')

# get configuration
redshift_config = DataWarehouseConfig(
    data_source='redshift',
    env='prod',
    config_file_path='dbdp_config.yml')

# create the connection
redshift_con = DataConnection(
    credential=redshift_cred,
    configuration=redshift_config
)

# Get the data
redshift_con.get_data(ss_test_query)

########################################################################
# Example for GBQ
########################################################################

# load credentials
gbq_credential = GBQCredential(credential_file_path='service-account-credential.json')

# get configuration
gbq_config = GBQConfig(project_id='98771639')

# create the connect
gbq_con = GBQConnection(credential=gbq_credential, configuration=gbq_config)
