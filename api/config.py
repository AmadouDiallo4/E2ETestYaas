
import os

from Configs.environments import BASE_URL

# configuration API

TIMEOUT = int(os.getenv("YASS_API_TIMEOUT", "20"))
