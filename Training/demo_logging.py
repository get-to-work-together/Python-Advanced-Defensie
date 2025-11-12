import logging

logging.basicConfig(
    filename = None, # or to a file 'example.log',
    level = logging.DEBUG,
    format = '%(levelname)s %(asctime)s.%(msecs)03d - %(message)s',
    datefmt = '%Y-%m-%dT%H:%M:%S')

logging.debug('This message should go to the log file')
logging.error('Watch out!')
logging.info('So should this')
logging.warning('And this, too')
logging.error('Watch out!')
logging.critical('ERROR!!!!!')
