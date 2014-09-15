#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Task 04. Alarm Clock'''

WEEKDAY = (raw_input('What day of the week is it? ').lower())[:3]

CURTIME = int(raw_input('What time is it? '))

if WEEKDAY == 'sat' or WEEKDAY == 'sun' or CURTIME < 600:
    SNOOZE = True
else:
    SNOOZE = False
if SNOOZE is False:
    print 'BEEP! ' * 5
