fileName = input("Please put file name: ")
file = open(fileName, 'r')
print(file)
wordCount = 0
for line in file:
    list = line.split()
    wordCount = wordCount + len(list)
print("number of words in your file")
print(wordCount)
