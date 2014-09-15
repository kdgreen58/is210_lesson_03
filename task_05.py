#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Task 05. A really long loan calculation.'''

import decimal

CUSTNAME = raw_input('What is your name? ')
AMOUNT = int(raw_input('What is the amount of your principal? '))
YEARS = int(raw_input('How many years is this loan being borrowed? '))
QUALIFIED = raw_input('Are you pre-qualified for this loan? ')

if AMOUNT >= 0 and AMOUNT <= 199999:
    if YEARS >= 1 and YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0363') / 12)) **
                          (12 * YEARS))
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0465') / 12)) **
                          (12 * YEARS))
    elif YEARS >= 16 and YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0404') / 12)) **
                          (12 * YEARS))
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0498') / 12)) **
                          (12 * YEARS))
    elif YEARS >= 21 and YEARS <= 30:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0577') / 12)) **
                          (12 * YEARS))
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0639') / 12)) **
                          (12 * YEARS))
    else:
        TOTAL = None
elif AMOUNT >= 200000 and AMOUNT <= 999999:
    if YEARS >= 1 and YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0302') / 12)) **
                          (12 * YEARS))
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0398') / 12)) **
                          (12 * YEARS))
    elif YEARS >= 16 and YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0327') / 12)) **
                          (12 * YEARS))
        elif QUALIFIED == 'No' or QUALIFIED == 'n':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0408') / 12)) **
                          (12 * YEARS))
    elif YEARS >= 21 and YEARS <= 30:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0466') / 12)) **
                          (12 * YEARS))
        else:
            TOTAL = None
    else:
        TOTAL = None
elif AMOUNT >= 1000000:
    if YEARS >= 1 and YEARS <= 15:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0205') / 12)) **
                          (12 * YEARS))
        else:
            TOTAL = None
    elif YEARS >= 16 and YEARS <= 20:
        if QUALIFIED == 'Yes' or QUALIFIED == 'y':
            TOTAL = round(AMOUNT * (1 + (decimal.Decimal('.0262') / 12)) **
                          (12 * YEARS))
        else:
            TOTAL = None
    else:
        TOTAL = None
else:
    TOTAL = None

REPORT = '''Loan Report for: {0:>5}
-------------------------------------------------------------------------------
            \tPrincipal: ${1:>5}
            \tDuration: {2:>5}yrs
            \tPre-qualified?:{3:>3}
            
            \tTotal: ${4:>10}'''.format(CUSTNAME, AMOUNT, YEARS,
                                        QUALIFIED, str(TOTAL))

print REPORT
