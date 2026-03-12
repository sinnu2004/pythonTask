# Find location of a word in sentence without using index/find.
import re

s = "Python is a Language"
target = "Language"

match = re.search("Language",s)
print(match)

