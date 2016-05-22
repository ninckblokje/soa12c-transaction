username = raw_input('Username: ')
password = raw_input('Password: ')
url = raw_input('URL: ')

connect(username, password, url)

edit()
startEdit()

cd('/')
cmo.createJDBCSystemResource('TransactionXADS')

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS')
cmo.setName('TransactionXADS')

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS/JDBCDataSourceParams/TransactionXADS')
set('JNDINames',jarray.array([String('jdbc/xa/transaction')], String))

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS')
cmo.setDatasourceType('GENERIC')

dbPassword = raw_input('Database Password: ')

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS/JDBCDriverParams/TransactionXADS')
cmo.setUrl('jdbc:oracle:thin:@//localhost:1521/XE')
cmo.setDriverName('oracle.jdbc.xa.client.OracleXADataSource')
cmo.setPassword(dbPassword)

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS/JDBCConnectionPoolParams/TransactionXADS')
cmo.setTestTableName('SQL ISVALID\r\n\r\n')

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS/JDBCDriverParams/TransactionXADS/Properties/TransactionXADS')
cmo.createProperty('user')

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS/JDBCDriverParams/TransactionXADS/Properties/TransactionXADS/Properties/user')
cmo.setValue('transaction')

cd('/JDBCSystemResources/TransactionXADS/JDBCResource/TransactionXADS/JDBCDataSourceParams/TransactionXADS')
cmo.setGlobalTransactionsProtocol('TwoPhaseCommit')

cd('/JDBCSystemResources/TransactionXADS')
set('Targets',jarray.array([ObjectName('com.bea:Name=DefaultServer,Type=Server')], ObjectName))

activate()

startEdit()
