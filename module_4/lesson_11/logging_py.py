import logging


# critical
# error
# warning
# info
# debug

logging.basicConfig(filename = "app.log", filemode="a" , level=logging.DEBUG, format="%(asctime)s-%(levelname)s-%(message)s")
logging.info("Hi info")
logging.warning("Hi warning")
logging.critical("Hi critical")
# logging.basicConfig(level=logging.WARNING, format="%(asctime)s-%(levelname)s-%(message)s")
logging.debug("hi Warning")



