# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:13:59 2020

@author: 66IN
"""

import sports

from pynotifier import Notification

match_info = sports.get_sport("CRICKET")

Notification(title = "Live Cricket Score", description = str(match_info), duration=60).send()