import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__) #create object form getlogger #test case _name_
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter) #setting the format of log file

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.WARNING)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")



