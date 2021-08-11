import logging
import sys

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOG_FILE = "jeeves.log"

def get_console_handler():
	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.setFormatter(FORMATTER)
	return console_handler

def get_file_handler():
	file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8', mode='a')
	file_handler.setFormatter(FORMATTER)
	return file_handler

def get_logger(logger_name):
	logger = logging.getLogger(logger_name)

	logger.setLevel(logging.DEBUG) # better to have too much log than not enough

	logger.addHandler(get_console_handler())
	logger.addHandler(get_file_handler())

	# with this pattern, it's rarely necessary to propagate the error up to parent
	logger.propagate = False

	return logger