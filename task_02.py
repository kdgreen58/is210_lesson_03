#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Code for Task 02. Blood Pressure input."""

USERINPUT = int(raw_input('What is your blood pressure? '))

if USERINPUT >= 160:
    BP_STATUS = 'Emergency'
elif USERINPUT >= 140 and USERINPUT <= 159:
    BP_STATUS = 'High'
elif USERINPUT >= 120 and USERINPUT <= 139:
    BP_STATUS = 'Warning'
elif USERINPUT >= 90 and USERINPUT <= 119:
    BP_STATUS = 'Ideal'
else:
    BP_STATUS = 'Low'

print 'Your status is currently: {0}!'.format(BP_STATUS)          
