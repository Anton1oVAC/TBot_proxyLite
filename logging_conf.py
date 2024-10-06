import logging
import sys

def log_conf():
	# Создаем файловый обработчик
	file_handler = logging.FileHandler('bot.log')
	file_handler.setLevel(logging.DEBUG)
	file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	file_handler.setFormatter(file_formatter)

	# Создаем потоковый обработчик
	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.setLevel(logging.INFO)
	console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	console_handler.setFormatter(console_formatter)

	# Получаем корневой логгер
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)

	# Добавляем обработчики к корневому логгеру
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)

	return logger