# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 10:15:58 2021
# CS 5012
PURPOSE: Explore regex development
TOOL FOR TESTING: https://regex101.com/
@author: apt4c
"""

# module for regex work
import re

#############################################################################
# SOME IMPORTANT SPECIAL CHARACTERS / IDEAS:
# ^         - beginning of string 
# $         - end of string
# \b          word boundary - note what happens if we don't use it
# \s        - whitespace
# () for capturing group. allows you to return parts of found expression

# [0-9]{15} - look for digits, repeated 15 times
# [0-8]     - look for these specific digits
# \d        - digit (alternative)

# [-|.|\s]  - match a dash, dot, or whitespace

# Setting word boundaries prevents incorrect match on substring
# For example searching for "male" and matching on "malevolent"

#############################################################################
# EXAMPLE REGEX PATTERNS

# gender 
re_gender = r"\b(male|female)\b"

# visa credit card
re_visa = r"\b(4[0-9]{15})\b"

# phone number without area code
re_phone_no_ac = r"(^|\s)\d{3,4}[-|.|\s]\d{4}($|\.?\s)"

# social security number
re_ssn = r"(^|\s)(?!000)[0-8]\d{2}[-|.](?!00)\d{2}[-|.](?!0000)\d{4}($|\.?\s)"

#############################################################################
# SEARCHING FOR REGEXES IN TEXT

# Find all mentions of "male or female"
doc = 'The first patient is male, age 13. The second patient is female, age 33'
match_gender = re.findall(re_gender, doc, re.IGNORECASE)
print(match_gender)

# use finditer to iterate over all matches
# print the matched text, and its location
match_patterns = re.finditer(re_gender, doc, re.IGNORECASE)
if match_patterns: 
    for mt in match_patterns:
        st = mt.start()
        ed = mt.end()
        print('match text:', mt.string[st:ed], '; start_pos:', st, '; end_pos', ed)

# Find only the first mention; this can be faster as it can quit early.
match_gender = re.search(re_gender, doc, re.IGNORECASE)
print(match_gender)

# If you're doing to reuse a regex, it's faster to compile it
pattern_gender = re.compile(re_gender, re.IGNORECASE)
match_gender = pattern_gender.findall(doc)
print(match_gender)

#############################################################################
# USING CAPTURE GROUPS TO EXTRACT PIECES OF A MATCH

re_specific_street = r"\b(maple)\s(street)\b"
pattern_street = re.compile(re_specific_street, re.IGNORECASE)
doc_twilight_zone = "The Monsters are Due on Maple Street"

match_street = pattern_street.search(doc_twilight_zone)
print(match_street)

# Extract first capture group
match_street.group(1)
# Extract second capture group
match_street.group(2)

# TRY FOR YOURSELF: WHAT HAPPENS IF YOU DON'T USE CAPTURE GROUPS?
re_specific_street = r"\bmaple\sstreet\b"
pattern_street = re.compile(re_specific_street, re.IGNORECASE)
match_street = pattern_street.search(doc_twilight_zone)
match_street.group(1)
match_street.group(2)

#############################################################################
