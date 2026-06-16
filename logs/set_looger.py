import logging


logging.basicConfig(handlers=[logging.FileHandler('app.log'), logging.StreamHandler()], format="%(asctime)s >>>> %(levelname)s:%(message)s",level=logging.DEBUG)

logger = logging.getLogger('my_logger')
