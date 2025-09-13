import logging                          # 1
logging.basicConfig(filename='log.txt', level=logging.WARNING)  # 2
print('Logging Demo')                  # 3
logging.debug('Debug Information')     # 4
logging.info('Info Information')       # 5
logging.warning('Warning Information')# 6
logging.error('Error Information')     # 7
logging.critical('Critical Information') # 8
