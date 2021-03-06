############################## Files #################################

# # This program reads from values.txt file and create an outvalue.txt file with values formatted
# # along with total and average
#
# # accept file name from user
# infilename = input("Enter input file name")
# outfilename = input("Enter input file name")
# infilename = infilename.strip()
# outfilename = outfilename.strip()
# # Open files for reading and writing
# infhandle = open(infilename, 'r')
# outfhandle = open(outfilename, 'w')
# # Read the input and write the output
# total = 0.0
# count = 0
# # read lines one by one
# line = infhandle.readline()
# while line != "":
#     line = line.strip()
#     value = float(line)
#     outfhandle.write("%-15.2f\n" % value)
#     total += value
#     count += 1
#     line = infhandle.readline()
# # output the total and average
# outfhandle.write("%-15s\n" % ('-' * 10))
# outfhandle.write("Total: %-8.2f\n" % total)
# outfhandle.write("Average: %-6.2f\n" % int(total/count))
#
# # close files
# outfhandle.close()
# infhandle.close()


# ## This program reads from the file lyrics.txt and print all the words
#
# infhandle = open('lyrics.txt', 'r')
# for line in infhandle:
#     line = line.strip()
#     wordlist = line.split()
#     for word in wordlist:
#         word = word.strip('.,!?')
#         print(word)
# infhandle.close()

# ## The below code demonstartes the use of method "s.splitlines"
# infhandle = open('lyrics.txt', 'r')
# lines = infhandle.read()
# stringsinline = lines.splitlines()
# print(stringsinline)
#
# ## Strip method
# population = "1,34,5678,3445"
# population.strip(",")       # Output: 1,34,5678,3445.
#                             # strip method only remove comma that is first or last character of string.
#                             # Here that is none.
#
# ## Split method demonstrated
# string = "a b  c"
# string.split(" ")  # Output: ['a', 'b', '', 'c']
# string.split()      # Output: ['a', 'b', 'c']
#
# string = "a:bc:d"
# string.split(":")   # Output: ['a', 'bc', 'd']
# string.split(":", 2)   # Output: ['a', 'bc', 'd']
# string.split(":", 1)   # Output: ['a', 'bc:d']
# string.rsplit(":", 1)   # Output: ['a:bc', 'd']
#
# ## Reading chars from a file.
# # This program reads all chars one by one till the end of file. When end of file is reached, infhandle.read(1) returns empty string
# infhandle = open('lyrics.txt', 'r')
# chars = infhandle.read(1)
# print(chars)     # Output : M
# while chars != "":
#     chars = infhandle.read(1)
#     print(chars)
#
# ## Reads 5 characters at a time.
# infhandle = open('lyrics.txt', 'r')
# chars = infhandle.read(5)
# print(chars)     # Output : Mary
#
# ## Read population records of countries from a file and display the data.
# # First line is country name and next line is population
# # This prints a tuple (country, population)
# fname = "PopulationRecords1.txt"
# populationList = list()
# fhandle = open(fname, 'r')
# line = fhandle.readline()
# while line != "":
#     country = line.strip()
#     population = fhandle.readline().replace(",", "").strip()
#     print(population)
#     populationList.append((country, population))
#     line = fhandle.readline()
# print(populationList)
#
# ## Read population records of countries from a file and display the data.
# # Data format is  country:population. One line for each country
# # This prints a dictionary (country, population)
# fname = "PopulationRecords2.txt"
# populationrecDict = dict()
# fhandle = open(fname, 'r')
# for line in fhandle:
#     record = line.split(':')
#     country = record[0]
#     population = record[1].replace(",", "").strip()
#     populationrecDict[country] = population
# print(populationrecDict)
#
# ## Read population records of countries from a file and display the data.
# # Data format is  country population. One line for each country. Country name can contain space too.
# # This prints a dictionary (country, population)
# # Use index position of first digit to extract country name and population
# fname = "PopulationRecords3.txt"
# populationrecDict = dict()
# fhandle = open(fname, 'r')
# for line in fhandle:
#     i = 0
#     while not line[i].isdigit():
#         i += 1
#     digitpos = i
#     country = line[0:i-1]
#     population = line[i: ].replace(",", "").strip()
#     populationrecDict[country] = population
# print(populationrecDict)
#
# # Use rstrip extract country name and population
# fname = "PopulationRecords3.txt"
# populationrecDict = dict()
# fhandle = open(fname, 'r')
# for line in fhandle:
#     record = line.rsplit(" ", 1)
#     country = record[0]
#     population = record[1].replace(",", "").strip()
#     populationrecDict[country] = population
# print(populationrecDict)

# Use regular expression to find the index of first digit extract country name and population
# need to check the answers
# ################################################################################
# ##
# # This program reads data files of the country populations and areas and
# # prints the population density for each country
# #
#
# POPULATION_FILE = "worldpop.txt"
# AREA_FILE ="worldarea.txt"
# REPORT_FTILE = "world_pop_density.txt"
#
#
# def main():
#     # open files
#     popFile = open(POPULATION_FILE, 'r')
#     areaFile = open(AREA_FILE, 'r')
#     reportFile = open(REPORT_FTILE, 'w')
#
#      # read the first data record
#     popData = extractDataRecord(popFile)
#     while len(popData) == 2:
#         # Read next area record
#         areaData = extractDataRecord(areaFile)
#
#         # extract country, population and from the two lists
#         country = popData[0]
#         population = float(popData[1])
#         area = float(areaData[1])
#
#         # Compute density and write it to the file
#         density = 0.0
#         if area > 0.0:
#             density = population/area
#         print(country, population, area, density)
#         reportFile.write("%-40s%15.2f\n" % (country, density))
#
#         # read the next population file
#         popData = extractDataRecord(popFile)
#      # close all files
#     popFile.close()
#     areaFile.close()
#     reportFile.close()
#
#
# def extractDataRecord(inFile):
#     line = inFile.readline()
#     if line == "":
#         return []
#     else:
#         line = line.strip()
#         parts = line.rsplit("\t", 1)
#         return parts
#
#
# main()
################################################################################

# ### Read data from csv file
#
# from csv import reader
#
# filename = "PopData.csv"
# inFile = open(filename)
# csvReader = reader(inFile)
# for row in csvReader:
#     print(row[0])

################################################################################

##
# This program reads data from PopData.csv file. Filter the records based on population density ( 300 < density < 500)
# and writes the filtered data into a new file
#

# from csv import reader, writer
#
# IN_FILENAME = "PopData.csv"
# OUT_FILENAME = "Filter_pop_data.csv"
#
# LOWER_LIMIT = 300.0
# UPPER_LIMIT = 500.0
#
# # open two csv files. one in read mode and other in write mode
# inFile = open(IN_FILENAME)
# csvReader = reader(inFile)
# outFile = open(OUT_FILENAME, 'w')
# csvWriter = writer(outFile)
#
# # Add headers to the output file
# header = ["Country", "Density", "Population", "Area"]
# csvWriter.writerow(header)
# # skip the header row
# next(csvReader)
# for row in csvReader:
#     if LOWER_LIMIT <= float(row[1]) <= UPPER_LIMIT:
#         print(row)
#         newRow = [row[0], row[1], row[3], row[4]]
#         csvWriter.writerow(newRow)
# outFile.close()
# inFile.close()

################################################################################
##
#  Count the number of times certain keywords, read from a separate file
#  occur in another document. Read keywords from keylist.txt. And count these keywords from article1.txt
#

# PUNC = ".,;:-!?"
#
# # read keywords file by taking user input
# keyfileName = input("Enter the filename containing keywords")
# if keyfileName == "":
#     keyfileName = "keylist.txt"
# keyFile = open(keyfileName, 'r')
#
# # read all keywords into a list
# keywordList = list()
# for keyword in keyFile:
#     keyword = keyword.strip()
#     keywordList.append(keyword)
# print(keywordList)
#
# #read file containing the text to check
# infileName = input("Enter the filename containing text to check for keywords:")
# if infileName == "":
#     infileName = "article1.txt"
# infile = open(infileName, 'r')
# # initialize list to store count
# countList = [0] * len(keywordList)
#
# # read words from the file
# for aline in infile:
#     aline = aline.strip()
#     words = aline.split()
#     for aword in words:
#         aword = aword.strip(PUNC)
#         if aword in keywordList:
#             keywordIndex = keywordList.index(aword)
#             countList[keywordIndex] += 1
# # Output keyword and frequency
# print("%-8s %5s" % ("words", "Count"))
# for i in range(len(keywordList)):
#     print("%-8s %5d" % (keywordList[i], countList[i]))
#
# #close files
# keyFile.close()
# infile.close()

################################################################################

##
# Write a program that reads the keywords.txt file and
# calculates the sentiment of a tweet. The keywords.txt file contains
# keywords and their sentiment value.
#

# filename = "keywords.txt"
# infile = open(filename, 'r')
# text = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"
# positiveList = []
# neutralList = []
# negativeList = []
# for line in infile:
#     parts = line.rsplit(" ", 1)
#     if len(parts) == 2:
#         keyword = parts[0]
#         parts[1] = parts[1].strip()
#         sentimentValue = int(parts[1])
#
#     if sentimentValue == 20:
#         positiveList.append(keyword)
#     elif sentimentValue == 0:
#         neutralList.append(keyword)
#     else:
#         negativeList.append(keyword)
# print("The positive words are", positiveList)
# print("The negative words are", negativeList)
# print("The neutral words are", neutralList)
# sentiment = 0
# words = text.strip().split()
# for word in words:
#     if word in positiveList:
#         sentiment += 20
#     elif word in negativeList:
#         sentiment = sentiment - 10
# print("The sentiment of the tweet is", sentiment)

##################################################################
## The above code with exception handling
#
#
filename = input("Enter the file name containing keywords:")
try:
    infile = open(filename, 'r')
except IOError:
    print("File not found, please try again.")
text = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"
positiveList = []
neutralList = []
negativeList = []
for line in infile:
    parts = line.rsplit(" ", 1)
    try:
        keyword = parts[0]
        parts[1] = parts[1].strip()
        sentimentValue = int(parts[1])
    except ValueError as exp:
         print("** Error **",str(exp), " ... Halting program - check input file.")
         exit(0)
    except IndexError as exp:
        print("** Error **", str(exp), " ... Halting program - check input file.")
        exit(0)
    if sentimentValue == 20:
        positiveList.append(keyword)
    elif sentimentValue == 0:
        neutralList.append(keyword)
    else:
        negativeList.append(keyword)
print("The positive words are", positiveList)
print("The negative words are", negativeList)
print("The neutral words are", neutralList)
sentiment = 0
words = text.strip().split()
for word in words:
    if word in positiveList:
        sentiment += 20
    elif word in negativeList:
        sentiment = sentiment - 10
print("The sentiment of the tweet is", sentiment)
infile.close()