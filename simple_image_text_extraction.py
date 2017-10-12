import os
import pytesseract
from PIL import Image
from autocorrect import spell
import grammar_check

text = pytesseract.image_to_string(Image.open("Bruce-Lee-Absorb.png"))

tool = grammar_check.LanguageTool('en-GB')
matches = tool.check(text)
ctext= grammar_check.correct(text, matches)
print ctext

