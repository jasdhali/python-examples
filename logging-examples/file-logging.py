import logging
logger = logging.getLogger(__name__) 
logging.basicConfig(filename='example.log',encoding='utf-8',level=logging.DEBUG)
logging.debug('This should go to log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')