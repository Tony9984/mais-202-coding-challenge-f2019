def openCSV(p_file):
    """Opens the txt file with path p_file and separated by delimiter delim. Returns a 2D list."""

    file = open(p_file, 'r', encoding='utf-8-sig')
    data = [[n for n in line[:-1].split(',')] for line in file]  # DJ: Opens file without including \n character

    return data

loanData = openCSV("loan_data.csv")
del loanData[0]

homeData = openCSV("home_ownership_data.csv")
del homeData[0]

if __name__ == '__main__':
    loans = []
    memberIds = []
    rent = []
    own = []
    mortgage = []
    homeDataDictionary = {}
    for list in loanData:
        loans.append(list[1])
        memberIds.append((list[0]))

    for list in homeData:
        homeDataDictionary[list[0]] = list[1]

    for i in range(len(memberIds)):
        homeStatus = homeDataDictionary[memberIds[i]]
        if homeStatus == 'MORTGAGE':
            mortgage.append(float(loans[i]))
        elif homeStatus == 'RENT':
            rent.append(float(loans[i]))
        else:
            own.append(float(loans[i]))
    mortgageMean = sum(mortgage)/len(mortgage)
    rentMean = sum(rent)/len(rent)
    ownMean = sum(own)/len(own)

    print(mortgageMean)
    print(rentMean)
    print(ownMean)





