import os
import sys
import json


from dotenv import load_dotenv
load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URL")
print(MONGODB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from network.exception.exception import NetworkSecurityException
from netsecurity.logging.logger import logging