import logging 


logger = logging.getLogger('mathstable')
formatter = logging.Formatter('%(lineno)s %(asctime)s %(levelname)s %(name)s %(message)s')
handler = logging.FileHandler('advanced.log')
streamhandler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.addHandler(streamhandler)
logger.setLevel(logging.DEBUG)

def add(n1,n2):
    logger.debug('Adding two values {} + {} = {}'.format(n1,n2,(n1+n2)))

def sub(n1,n2):
     logger.debug('Adding two values {} - {} = {}'.format(n1,n2,(n1-n2)))
   
def mul(n1,n2):
     logger.debug('Adding two values {} * {} = {}'.format(n1,n2,(n1*n2)))
    
def div(n1,n2):
     logger.debug('Adding two values {} / {} = {}'.format(n1,n2,(n1/n2)))
    
add(2,4)
sub(2,4)
mul(2,4)
div(2,4)