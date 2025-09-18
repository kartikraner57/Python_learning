import logging  

# Step 1: Configure logging
logging.basicConfig(
format='%(asctime)s : %(levelname)s : %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p',
    level=logging.DEBUG   # DEBUG पासून सर्व messages दिसतील
)

# Step 2: Normal print statement
print('Logging Demo')

# Step 3: Different logging levels
logging.debug('Debug Information')       # Developer info
logging.info('Info Information')         # General info
logging.warning('Warning Information')   # Warning
logging.error('Error Information')       # Error
logging.critical('Critical Information') # Critical
