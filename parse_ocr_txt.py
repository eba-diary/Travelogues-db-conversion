#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""parse_ocr_txt.py: Parse raw ORC'd text of Kalfatovik's Nile Notes of a Howadji
"""

import re

FIRST_ENTRY_NBR = 789           # First entry number to parse.
OCR_FILENAME = "raw_ocr.txt"    # Filename of OCR text

# keys of the dictionaries that represent Entries and Works respectively
entry_keys = [number, name, works, travel_date, nationality]
work_keys = [title, annotation]

def is_page_header(line):
    """Return True if the given line of text is a page header
    e.g. "278 Nile Notes of a Howadji" (even pages) or "1880-1889 - 279 " (odd pages)
    """
    even_page =  bool(re.match(r"(\d{1,3})( )(Nile Notes of a Howadji)( ?)", line))
    odd_page =  bool(re.match(r"(\d{4}-\d{4})( )(\d{3})( ?)$", line))
    return even_page or odd_page

ocr_file = open(OCR_FILENAME)
ocr_lines = ocr_file.readlines()
ocr_file.close()

entries = []
next_entry_nbr = FIRST_ENTRY_NBR
current_entry = dict.fromkeys(entry_keys)
for line in ocr_lines:
    print(line)