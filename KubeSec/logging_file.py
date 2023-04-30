import logging

def LoggingObject():
    format_str = '%(asctime)s %(message)s'
    file_name = 'project-LOGGER.log'
    logging.basicConfig(format=format_str, filename=file_name,level=logging.INFO)
    loggerObj = logging.getLogger('project-LOGGER.log')
    return loggerObj