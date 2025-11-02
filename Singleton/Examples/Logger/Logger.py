import os 
from datetime import datetime
from Singleton import Meta

class Logger(metaclass=Meta):
    def __init__(self, log_file='app.log'):
        self.log_file = log_file

        os.makedirs(os.path.dirname(self.log_file), exist_ok=True) if '/' in log_file else None

        self.file = open(self.log_file, mode='a')

    def write(self, level, message):
        timestamp = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message} \n"
        self.file.write(log_entry)
        self.file.flush()

    def info(self, message):
        self.write("INFO", message)

    def warning(self, message):
        self.write("WARNING", message)

    def error(self, message):
        self.write("ERROR", message)

    def close(self):
        if not self.file.closed:
            self.file.close()
        