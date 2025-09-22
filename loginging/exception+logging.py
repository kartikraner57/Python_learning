import logging

# Step 1: Configure logging (log file, level, format, date)
logging.basicConfig(
    filename='mylog.txt',
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p'
)

# Step 2: Start log
logging.info('A new Request Came')

try:
    # Step 3: Take input
    x = int(input('Enter First Number: '))
    y = int(input('Enter Second Number: '))

    # Step 4: Perform division
    print('The Result:', x / y)

# Step 5: Handle ZeroDivisionError
except ZeroDivisionError as msg:
    print('Cannot divide with zero')
    logging.exception(msg)

# Step 6: Handle ValueError
except ValueError as msg:
    print('Please provide int values only')
    logging.exception(msg)

# Step 7: Complete log
logging.info('Request Processing Completed')
