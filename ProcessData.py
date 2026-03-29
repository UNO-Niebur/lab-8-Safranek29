#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  def makeID(first, last, idNum):
    idLen = len(idNum)
    while len(last) < 5:
      last = last + "X"
    id = (first[0] + last + idNum[idLen -3: ]).lower()
    return id
  
  def makeMaj(major, year):
    major = major.upper()
    if year == "Freshman":
      year = "FR"
    elif year == "Sophomore":
      year = "SO"
    elif year == "Junior":
      year = "JR"
    elif year == "Senior":
      year = "SR"
    Maj_Year = major[0:3] + "-" + year
    return Maj_Year

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    major = data[6]
    year = data[5]

    studentID = makeID(first, last, idNum)
    maj = makeMaj(major, year)
    output = last + "," + first + "," + studentID + "," + maj + "\n"
    outFile.write(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
