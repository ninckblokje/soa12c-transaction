username = raw_input('Username: ')
password = raw_input('Password: ')
url = raw_input('URL: ')

connect(username, password, url)

edit()
startEdit()

cd('/')
cmo.createJMSSystemResource('TransactionModule')

cd('/JMSSystemResources/TransactionModule')
set('Targets',jarray.array([ObjectName('com.bea:Name=DefaultServer,Type=Server')], ObjectName))

activate()

startEdit()

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule')
cmo.createConnectionFactory('TransactionXAFactory')

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionXAFactory')
cmo.setJNDIName('jms/TransactionXAFactory')

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionXAFactory/SecurityParams/TransactionXAFactory')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionXAFactory/ClientParams/TransactionXAFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionXAFactory/TransactionParams/TransactionXAFactory')
cmo.setXAConnectionFactoryEnabled(true)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionXAFactory')
cmo.setDefaultTargetingEnabled(true)

activate()

startEdit()

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule')
cmo.createConnectionFactory('TransactionFactory')

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionFactory')
cmo.setJNDIName('jms/TransactionFactory')

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionFactory/SecurityParams/TransactionFactory')
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionFactory/ClientParams/TransactionFactory')
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionFactory/TransactionParams/TransactionFactory')
cmo.setXAConnectionFactoryEnabled(false)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/ConnectionFactories/TransactionFactory')
cmo.setDefaultTargetingEnabled(true)

activate()

startEdit()

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule')
cmo.createUniformDistributedQueue('TransactionErrorQueue')

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/UniformDistributedQueues/TransactionErrorQueue')
cmo.setJNDIName('jms/TransactionErrorQueue')
cmo.setDefaultTargetingEnabled(true)

activate()

startEdit()

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule')
cmo.createUniformDistributedQueue('TransactionQueue')

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/UniformDistributedQueues/TransactionQueue')
cmo.setJNDIName('jms/TransactionQueue')
cmo.setDefaultTargetingEnabled(true)


cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/UniformDistributedQueues/TransactionQueue/DeliveryFailureParams/TransactionQueue')
cmo.setExpirationPolicy('Redirect')
cmo.setRedeliveryLimit(3)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/UniformDistributedQueues/TransactionQueue/DeliveryParamsOverrides/TransactionQueue')
cmo.setRedeliveryDelay(5000)

cd('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/UniformDistributedQueues/TransactionQueue/DeliveryFailureParams/TransactionQueue')
cmo.setErrorDestination(getMBean('/JMSSystemResources/TransactionModule/JMSResource/TransactionModule/UniformDistributedQueues/TransactionErrorQueue'))

activate()
