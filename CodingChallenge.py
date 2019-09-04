import matplotlib.pyplot as plt
import numpy as np

def openCSV(p_file):
    """Opens the csv file with path p_file. Returns a 2D list."""

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

    means = [mortgageMean, ownMean, rentMean]
    labels = ["MORTGAGE", "OWN", "RENT"]

    index = np.arange(len(labels))
    plt.bar(index, means, width=0.6)
    plt.xlabel('Home ownership', fontsize=12)
    plt.ylabel('Average loan amount ($)', fontsize=12)
    plt.xticks(index, labels, fontsize=12)
    plt.title('Average loan amounts per home ownership')
    plt.show()






