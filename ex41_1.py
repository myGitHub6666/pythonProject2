import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

ptrases = {
    "class %%%(%%%):":
        "make a class named %%% that is_a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ parms.",
    "* * * = % % % ()":
        "set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, call it with paras self, @@@。",
        "***.*** = '***'":
    "from *** get the *** attribute and set it to '***"
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHEASE_FIRST = True
else：
    PHEASE_FIRST = False

#

