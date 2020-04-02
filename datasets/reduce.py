# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:20:12 2020

@author: paixo
"""

import pandas as pd
import numpy as np
from bert-serving.client import BertClient()

client = BertClient()

vectors = client.encode([“dog”],[“cat”],[“man”])