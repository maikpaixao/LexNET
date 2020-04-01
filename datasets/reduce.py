# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:20:12 2020

@author: paixo
"""

import pandas as pd
import numpy as np

df = pd.read_csv('BLESS/train.tsv')

percent = 0.1*len(df)

print(int(percent))
