

"""
class str:

    def capitalize()

    def casefold()

    def upper()

    def lower()

    def isalpha() -> return true if string is alphabet return false otherwise

    def isdigit() -> return true if string object is digit false otherwise

    def isalnum() -> return true if string is alphabet or number return false otherwise

    def index(str) -> return index of first occurance of str else return valuerror

    def count(str) -> return num of times sub string occurs in the string object
   
    def startswith(prefix) -> retuen true if string object starts with given prefix else return false

    def endswith(suffix) -> return true if string object ensa with given suffix else false

    def strip(char) -> return copy of string in which chars removed from both end

    def lstrip(char) -> return copy of string in which char removed from begining/left side

    def rstrip(char) -> return copy of string in which char removed from end/right side


"""

name = "Luminartechnolab"

name1 = "ajay"

name3 = "athira"

name4 = "AMMU"

name2 = "10"

new_name = name.casefold()

new_name1 = name1.capitalize()

new_name3 = name3.upper()

new_name4 = name4.lower()

new_name2 = name2.isdigit()

print(new_name3)

print(new_name4)

print(new_name1)

print(new_name2)

print(new_name)

print(name.isalpha())

print(name1[0:2])

print(name.index("tec"))

occ= name1.count("a")

print(occ)

print(name.startswith("Lum"))

print(name.endswith("lab"))

name5 = "<ajay>"

new_name5 = name5.strip("< >")

print(new_name5)

