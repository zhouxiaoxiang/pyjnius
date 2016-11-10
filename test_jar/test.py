#!/usr/bin/python

import os
import jnius_config
from jnius import autoclass

obj = autoclass('Eric')()
print(obj.get())

