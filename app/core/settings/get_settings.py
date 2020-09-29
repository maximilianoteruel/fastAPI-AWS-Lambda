import os
from .dev import DevSettings
from .prod import ProdSettings

# Settings
environment = os.getenv("ENVIRONMENT", "DEV")

if environment == "DEV":
    settings = DevSettings()
elif environment == "PROD":
    settings = ProdSettings()
