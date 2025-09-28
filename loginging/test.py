import logging
logging.basicConfig(
                    filename='mylog10072019.txt',
                    level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p'
					)
logging.info('A new request came...')
try:
	x=int(input('Enter First Number:'))
	y=int(input('Enter Second Number:'))
	print('The Result:',x/y)

except ZeroDivisionError as msg:
	print('cannot divide with zero')
	logging.exception(msg)

	logging.exception(msg)

logging.info('Request processing completed'