from Logger import Logger

log1 = Logger(log_file='logs/app.log')
log2 = Logger(log_file='logs/app.log')

print(log1 is log2)


log1.info("Application started")
log1.warning("Low disk space")
log1.error("Failed to connect to database")