
#Importing os environment variables
import os
from dotenv import load_dotenv

load_dotenv('.env')
api_key = os.getenv('API_TOKEN')
os.environ["REPLICATE_API_TOKEN"] = api_key

import replicate