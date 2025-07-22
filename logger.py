# logger.py
import logging

# ساخت لاگر مرکزی
logger = logging.getLogger("zoo_logger")
logger.setLevel(logging.INFO)

# تعریف هندلر فایل
file_handler = logging.FileHandler("zoo.log")
file_handler.setLevel(logging.INFO)

# قالب لاگ‌ها
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# اضافه کردن هندلر
logger.addHandler(file_handler)
