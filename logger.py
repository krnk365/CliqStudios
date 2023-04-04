import logging
import datetime as dt

def myLogger(level,msg):
    logging.basicConfig(filename='logs.log',
                        format='%(asctime)s %(message)s')

    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    getattr(logger,level)(msg)