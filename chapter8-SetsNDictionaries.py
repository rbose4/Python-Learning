############################## Sets and dictionaries ##########################

############################## Sets ##########################
# set store unique values. It doesn't store data in any particular order. So indexing is not possible.
# all mathematical set operations are possible.


# # Initializing a set
# cast = {"Raechel", "Joey", "Monica", "Chandler"}
# print(cast)
# print(len(cast))
# print(type(cast))
#
# #Initialize empty set
# cast_movie = set()
# print(cast_movie)
# print(len(cast_movie))
#
# names=["Revathi", "Mohanlal", "Innocent", "Nedumudi Venu"]
# #initialize set with a sequence like list
# cast_movie = set(names)
# print(cast_movie)
#
# # adding new items to the set using add method
# cast_movie.add("Mammooty")
# cast_movie.add("Lal")
# print(cast_movie)
# # adding an already existing item doesn't have any effect
# cast_movie.add("Lal")
#
# # check if an element is present using IN operator
#
# if "Joey" in cast:
#     print("Joey is a character in Friends")
# else:
#     print("Joey is not a character in Friends")
#
# # accessing elements in the set. We cannot access by index since sets are unordered.
# # We need to iterate over each element (use a for loop)
#
# print("The cast of characters includes: ")
# for character in cast:
#     print(character)
#
# # displaying sets in sorted order using sorted function. This returns a list (not a set)
# # of elements in sorted order
#
# print(type(sorted(cast_movie)))
# for character in sorted(cast_movie):
#     print(character, type(character))
#
# # discard items using discard method. If the item is already existing in the set, it removes the item.
# # If the item doesn't exists, the method will not have any effect at all.
# cast_movie.discard("Innocent")
# cast_movie.discard("Indrans")
#
# # remove items using remove method. If the item is already existing in the set, it removes the item.
# # If the item doesn't exists, the method raises an exception.
# cast_movie.remove("Nedumudi Venu")
#
# # The below statement throws a keyerror since Indrans is not present in the set.
# cast_movie.remove("Indrans")
#
# # Clear method clear the whole content of the set. The size of the set will be 0 after this operation.
# cast_movie.clear()
#
# # issubset method. It returns true if the set is a subset of a set. Otherwise return false.
# canada_flag={"Red", "White"}
# british_flag={"Red", "Blue", "White"}
# italian_flag={"Red", "White", "Green"}
#
# if canada_flag.issubset(british_flag):
#     print("All canadian flag colors occur in the british flag")
#
# if not italian_flag.issubset(british_flag):
#     print("Atl east one color in italian flag does not occur in the british flag")
#
# # Union method does the set union operation. Duplicates are removed. The operation does not modify either set.
# # The result of union is stored in a new set
# british_italian_Union = british_flag.union(italian_flag)
# print(british_italian_Union)
#
# # Intersetion method does the set intersection operation. Duplicates are removed.
# # The operation does not modify either set.
# # The result of intersection is stored in a new set
# british_italian_Intersection = british_flag.intersection(italian_flag)
# print(british_italian_Intersection)
#
# # Difference operation does set difference operation. set1.difference(set2) gives all element in
# # set1 which are not in set 2.
# # The operation does not modify either set. They return new sets
#
# british_Italian_diff = british_flag.difference(italian_flag)
# print(british_Italian_diff)
#
# # Equality == and inequality !=. Two sets are equal if and only if they have exactly the same elements
# # (including case of letters)
# french = {"White", "Red", "Blue"}
# print(british_flag == french)   # Output: True
# print(canada_flag == french)      # Output: False
# print(canada_flag != french)       # Output: True
############################################################################
##
# This program checks which words in a file are not present
# in a list of correctly spelled words
#

# Import split function from the regular expression module

# from re import split
# PUNC = ".,;:-!?"
# def readWords(filename):
#     wordset = set()
#     infile = open(filename, 'r')
#     for line in infile:
#         line = line.strip()
#         # use character other than alphabet for split
#        # parts = split("^[a-zA-Z]+", line)
#        # print(parts)
#         parts = line.split()
#        # print(parts)
#         for word in parts:
#             if len(word) > 0:
#                 word = word.strip(".,;:-!?'")
#                 wordset.add(word.lower())
#     infile.close()
#     return wordset
#
#
# def main():
#     # Read document and list of words
#     correctlySpelledwords = readWords("correctwords.txt")
#     documentwords = readWords("alice.txt")
#     # print(correctlySpelledwords)
#     # print(documentwords)
#     # print all misspelled words in the document
#     misspelledwords = documentwords.difference(correctlySpelledwords)
#     for word in sorted(misspelledwords):
#         print(word)
#
#
# main()

#######################################################################################

##
# This program reads unique words from a file and count the unique words.
# Use set when you need to store unique values. You can use list, but the operation will be much slower
#

# def readUniqueWordsFromFile(fileName):
#     try:
#         infile = open(fileName, 'r')
#     except IOError:
#         print("Invalid file.")
#         exit()
#     wordSet = set()
#     for line in infile:
#         line = line.strip()
#         words = line.split()
#         for word in words:
#             if len(word) > 0:
#                 word = word.strip(".,;:-!?'")
#                 wordSet.add(word.lower())
#     infile.close()
#     return wordSet
#
#
# def main():
#     filename = input("Enter file name:")
#     uniqueWords = readUniqueWordsFromFile(filename)
#     print("We have found", len(uniqueWords), " unique words in the file", filename)
#     for word in sorted(uniqueWords):
#         print(word)
#
# main()

############################# Dictionaries  ##########################################################
# A dictionary is a container that keeps associations between keys and values
# Every key in the dictionary has an associated value
# Keys are unique, but a value may be associated with several keys


# # initializing dictionary
#
# favoriteColours = {"Romeo" : "Red", "Adam" : "Blue", "Joe" : "Green"}
# print(favoriteColours)           # Output: {'Romeo': 'Red', 'Adam': 'Blue', 'Joe': 'Green'}
# print(type(favoriteColours))    # Output: <class 'dict'>
#
# emptyDict = dict()
# print(emptyDict)    # Output: {}
#
# contacts = {"Eva": 6476625, "Hrishi": 5194664, "Roopa": 5196625, "Jeeva": 9441363}
# # create a duplicate copy of a dictionary using dict()
# oldcontacts = dict(contacts)
# print(oldcontacts)          # Output: {'Eva': 6476625, 'Hrishi': 5194664, 'Roopa': 5196625, 'Jeeva': 9441363}
#
# # accessing dictionary values. You cannot access the items by index or position
# # A value can only be accessed using its associated key
# # The key supplied to the subscript operator must be a valid key in the dictionary or
# # a KeyError exception will be raised
#
# print(contacts["Hrishi"])   # Output: 5194664
#
# # modify items
# contacts["Hrishi"] = 5192124664
# print(contacts)             # Outptut: {'Eva': 6476625, 'Hrishi': 5192124664, 'Roopa': 5196625, 'Jeeva': 9441363}
#
# # add new items
# contacts["Anu"] = 5194643
# print(contacts)
#
# # adding new elements dynamically
# favColors = {}
# favColors["Rhea"] = "Blue"
# favColors["Karan"] = "Red"
# favColors["Mihir"] = "Purple"
# favColors["Tony"] = "Brown"
# print(favColors)
#
# # Checking if the key is present with in or not in operator
# name = "Eva"
# if name in contacts:
#     print(name, "'s phone number is ", contacts["Eva"])
# else:
#     print(name, "not in contacts")
#
# # Default Keys.
# # Instead of using the in operator, you can simply call the get() method and pass the key and a default value.
# # The default value is returned if there is no matching key
#
# number = contacts.get("Rianna", 911)
# print("Dial", number)           # Output: Dial 911
#
# # Removing elements using pop() method. This removes the entire item, both the key and its associated value.
# contacts.pop("Roopa")
# print(contacts)
#
# # If the key is not in the dictionary, the pop method raises a KeyError exception
# contacts.pop("Mom")
# # To prevent the exception from being raised, you should test for the
# # key in the dictionary:
#
# if "Mom" in contacts:
#     contacts.pop("Mom")
#
# # The pop() method returns the value of the item being removed, so
# # you can use it or store it in a variable:
#
# eva_number = contacts.pop("Eva")
# print(eva_number)
#
# # traversing through dictionary using a for loop
# # Note that the dictionary stores its items in an order that is optimized for efficiency,
# # which may not be the order in which they were added
#
# print("The list of names")
# for key in favColors:
#     print(key)
#
# # Output :
# # The list of names
# # Rhea
# # Karan
# # Mihir
# # Tony
#
# print("The list of colors")
# for value in favColors.values():
#     print(value)
#
# # Output:
# # The list of colors
# # Blue
# # Red
# # Purple
# # Brown
#
# print("The list of  names and their fav colors")
# for key, value in favColors.items():
#     print(key, value)
#
# # Output:
# # The list of  names and their fav colors
# # Rhea Blue
# # Karan Red
# # Mihir Purple
# # Tony Brown
#
# # iterate through keys in sorted order. sorted(dict) is a list
#
# for key in sorted(favColors):
#     print(key, favColors[key])
#
# # Output:
# # Karan Red
# # Mihir Purple
# # Rhea Blue
# # Tony Brown
#
# # iterating more efficiently using items() method.
# # item[0] gives you the key and item[1] gives the value
#
# for item in favColors.items():
#     print(item[0], item[1])
#
# # Output:
# # The list of  names and their fav colors
# # Rhea Blue
# # Karan Red
# # Mihir Purple
# # Tony Brown

# ## This program reads country and population data from file and store it in a dictionary
# # The key is the country. And value is the population
#
# def main ():
#     fname = input("Enter the file name:")
#     if fname == "":
#         fname = "PopulationRecords2.txt"
#     infile = open(fname, 'r')
#     record = extractRecord(infile)
#     while len(record) > 0:
#         print("%-20s %10s" % (record["country"], record["population"]))
#         record = extractRecord(infile)
#
#
# def extractRecord(fhandle):
#     record = {}
#     line = fhandle.readline()
#     line = line.strip()
#     if line != "":
#         parts = line.split(":")
#         record["country"] = parts[0]
#         record["population"] = parts[1]
#     return record
#
#
# main()

############################# Complex sets  ##########################################################

############################# Dictionary of  sets  #########################################

##
# This program builds the index book from terms and page numbers
#

# def main():
#     # create dictionary
#     indexEntries = dict()
#     # get file name
#     fname = input("Enter index data file name")
#     if len(fname) == 0:
#         fname = "indexdata.txt"
#      # open file
#     infile = open(fname, 'r')
#     fields = extractData(infile)
#     while len(fields) > 0:
#         addWord(indexEntries, fields[1], fields[0])
#         fields = extractData(infile)
#    # print(indexEntries)
#     printEntries(indexEntries)
#     infile.close()
#
# def extractData(fhandle):
#     line = fhandle.readline()
#     if line!= "":
#         line = line.strip()
#         parts = line.split(":")
#         page = int(parts[0])
#         term = parts[1].strip()
#         return [page, term]
#     else:
#         return []
#
#
# def addWord(entries, term, page):
#     if term in entries:
#         pageSet = entries[term]
#         pageSet.add(page)
#     else:
#         pageSet = set([page])
#         entries[term] = pageSet
#
# def printEntries(entries):
#     pageset = set()
#     for key in entries:
#         print(key, end=": ")
#         pageset = entries[key]
#         first = True
#         for page in sorted(pageset):
#             if first:
#                 print(page,  end="")
#                 first = False
#             else:
#                 print(",", page, sep="", end="")
#         print()
#
# main()

# ############################# Dictionary of  Lists  #########################################
#
# ##
# # This program read ice cream data from file and create dictionary of lists to store
# # sales price of various flavours for each shop. The output is printed on console in a specific format
# #
#
# def main():
#     # create dictionary to hold list of sales record
#     #salesdata = dict()
#     # assign file name
#     fname = "icecream.txt"
#     # read data from file into dictionary
#     salesdata = readData(fname)
#     printRecords(salesdata)
#
#
# def readData(filename):
#     salesDict = dict()
#     # open file
#     infile = open(filename, 'r')
#     # create dictionary record based on each line in the file
#     for line in infile:
#         line = line.strip()
#         if line != "":
#             salesrecord = line.split(":")
#             # assigning key and value to the dictionary.
#             # Key is the flavour and value is the list of sales price
#             salesDict[salesrecord[0].strip()] = buildListOfSales(salesrecord)
#     return salesDict
#
#
#
# def buildListOfSales(salerecord):
#     # create a list to hold list of values
#     salepriceList = []
#     if len(salerecord) > 0:
#         # adding sale prices to list
#         for i in range(1, len(salerecord)):
#             salepriceList.append(salerecord[i].strip())
#     return salepriceList
#
# def printRecords(salesData):
#     # find the number of stores as the length of the longest store sales list
#     numStores = 0
#     for storeSales in salesData.values():
#         if len(storeSales) > numStores:
#             numStores = len(storeSales)
#
#      # create a list to hold store totals
#     storeTotal = [0.0] * numStores
#     for flavour in sorted(salesData):
#         saleprices = salesData[flavour]
#         flavourprice = 0.0
#         print("%-15s" % flavour, end="")
#         i = 0
#         for item in saleprices:
#             price = float(item)
#             # adding store total
#             storeTotal[i] += price
#             i += 1
#             # adding flavour prices
#             flavourprice += price
#             # printing sale price of each flavour
#             print("%10.2f" % price, end="")
#          # printing total flavour sales
#         print("%17.2f" % flavourprice)
#
#     print("%-15s" %(" "), end="")
#     # printing total flavour sales
#     for price in storeTotal:
#         print("%10.2f" % price, end="")
#
#
# main()
################################## Lab 8, Excercise ###########################
##
#  This program processes a file containing a name followed by data values.
#  If the file doesn't exist or the format is incorrect, you can specify another file.
#

# def main():
#     done = False
#     while not done:
#         try:
#             filename = input("Enter the file name: ")
#             outfilename = input("Enter the output file name: ")
#             data = readFile(filename)
#             ## add sum code and writing to file here ###
#             # Calculate the total population
#             print("Sum: ", sum(data))
#             # total = 0
#             # for value in data:
#             #     total = total + value
#             # print("Total:", total)
#             # method to write total into file
#             writeFile(outfilename, sum(data))
#             done = True
#         except IOError:
#             print("Error: File not found.")
#         except ValueError:
#             print("Error: File contents are invalid.")
#         except RuntimeError as error:
#             print("Error:", str(error))
#
#
# ## Opens a file and call method to read data.
# #  @param filename the name of the file holding the data
# #  @return a list containing the data in the file
# #
#
# def readFile(filename):
#     infile = open(filename, 'r')
#     try:
#         return readData(infile)
#     finally:
#         infile.close()
#
# ## Reads a data set.
# #  @param inFile the input file containing the data
# #  @return the data set in a list
# #
#
# def readData(inFile):
#     data = []
#     for line in inFile:
#         if line != "":
#             line = line.strip()
#             line = line.split(':')
#             ## Below line may raise value error exception if second part after split is not an integer
#             pop_num = int(line[1])
#             data.append(pop_num)
#
#     # make sure there are no more values in the file
#     line = inFile.readline()
#     if line != "":
#         raise RuntimeError("End of file expected")
#     return data
#
# ## Writes the parameter passed into a file
# #  @param filename the name of the file holding the data
# #  @return a list containing the data in the file
# #
#
# def writeFile(filename, total):
#     outfile = open(filename, 'w')
#     try:
#         outfile.write("The total population is %d" % total)
#     finally:
#         outfile.close()
#
#
# main()

################################## Lab 9, Excercise ###########################
## This program reads data from a file and create dictionaries

def readDataToDict():
    filename = "rawdata.txt"
    infile = open(filename, 'r')

    cname_perCapDict = dict()
    dictCountryName = dict()
    countryList = []
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for line in infile:
        line = line.strip()
        line = line.split(":")
        key = line[1].strip()
        value = line[2].strip()
        cname_perCapDict[key] = value.upper()
    #print(cname_perCapDict)
    for i in range(len(alphabets)):
        char = alphabets[i]
        for item in cname_perCapDict.keys():
            if item.startswith(char):
               # print(item)
                countryList.append(item.upper())
        dictCountryName[char] = list(countryList)
        countryList.clear()
    return dictCountryName


def getCountryName(dictCName, instring):
    dictCountryName = dict(dictCName)
    char = ""
    if instring != "":
        if len(instring) == 1:
            char = instring[0]
            char = char.upper()
            #print(sorted(dictCountryName[char]))
            for item in sorted(dictCountryName[char]):
                print(item)
        else:
            char = instring[0]
            char = char.upper()
            nameList = sorted(dictCountryName[char])
            for item in nameList:
                if item.startswith(instring.upper()):
                    print(item)
    else:
        raise ValueError("Invalid string")


def main():
     dictCName = readDataToDict()
     getCountryName(dictCName, "No")

main()