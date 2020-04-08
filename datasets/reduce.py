# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:20:12 2020

@author: paixo
"""

import pandas as pd
import numpy as np

df = pd.read_csv('news.csv', encoding='latin-1')
new_df = pd.DataFrame(columns=['news'])

for row in df[:10]:
    print(row)

