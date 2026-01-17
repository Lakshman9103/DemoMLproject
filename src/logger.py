import logging
import os
from datetime import datetime

Log_Filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join("logs", Log_Filename)
os.makedirs(logs_path, exist_ok=True)   

log_file_path = os.path.join(logs_path, Log_Filename)

logging.basicConfig(
    filename=log_file_path, 
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S'
)


