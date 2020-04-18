# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import json
pd.read_table('output.txt', delimiter = ',').to_json('output.json')