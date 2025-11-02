from logger import Logger
from config import Config

log1 = Logger()
log2 = Logger()
cfg1 = Config()
cfg2 = Config()


print("Logger instances same?", log1 is log2) 
print("Config instances same?", cfg1 is cfg2) 

log1.log("System started")
log2.log("User logged in")
log1.show_logs()  

cfg1.set_theme("Dark")
cfg2.set_language("FR")
print(cfg1.theme, cfg1.language) 
print(cfg2.theme, cfg2.language) 