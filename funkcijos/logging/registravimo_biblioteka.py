import logging
from time import time

data = time()
filename = f''
logging.basicConfig(level=logging.DEBUG,
                    filename='data/{time}.log',
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S')
logging.debug('This is Debug Message')
logging.info('This is an info message')

# logging/print POP*

#logging.debug()
#logging.info()
#logging.warning()
#logging.error()
#logging.critical()



def calculate_numbers(*args):      # debug f9
    result = {'lyg': 0, "nelyg": 0}
    for n in args:
        if n % 2 ==0:
            result['lyg'] += n
            logging.info(f'{n} pridetas prie lyg')
        else:
            result['nelyg'] +=n

    logging.info(f'garazinama reiksme {result}')
    return result

numbers = [1, 2, 3, 4, 5, 6, 0,]
print(calculate_numbers(*numbers))