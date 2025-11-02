from config_manager import ConfigManager
from admin import Admin


config1 = ConfigManager("./config.json")
print(config1)
# config1._config["app_name"] = "InvoiceService Updated"

new_admin = Admin("didar", "HelloWorld123")
new_admin2 = Admin("ayshat", 'Ayshat123')

print(config1)