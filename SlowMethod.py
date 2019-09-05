import matplotlib.pyplot as plt

def openCSV(p_file):

    """Function to open a csv file with path p_file. Returns a 2D list."""

    file = open(p_file, 'r', encoding='utf-8-sig')
    data = [[n for n in line[:-1].split(',')] for line in file]  # DJ: Opens file without including \n character

    return data

if __name__ == '__main__':

    """Initialize lists to store different data extracted from the csv"""

    loans = []
    memberIds = []

    rent = []
    own = []
    mortgage = []

    homeDataDictionary = {}

    """Extract all data from both csvs and remove their headers"""

    loanData = openCSV("loan_data.csv")
    del loanData[0]

    homeData = openCSV("home_ownership_data.csv")
    del homeData[0]

    """Store the memberIDs and loans columns to the appropriate list"""

    for list in loanData:
        loans.append(list[1])
        memberIds.append((list[0]))

    """
    Store the memberIDs as keys and their home ownership status
    as the corresponding value in the initialized dictionary
    """

    for list in homeData:
        homeDataDictionary[list[0]] = list[1]

    """
    Categorize every members' loan amounts to its appropriate 
    list by comparing the memberIds list and the previous dictionary
    """

    for i in range(len(memberIds)):
        homeStatus = homeDataDictionary[memberIds[i]]
        if homeStatus == 'MORTGAGE':
            mortgage.append(float(loans[i]))
        elif homeStatus == 'RENT':
            rent.append(float(loans[i]))
        elif homeStatus == 'OWN':
            own.append(float(loans[i]))

    """Calculate the average of each home ownership status"""

    mortgageMean = sum(mortgage)/len(mortgage)
    rentMean = sum(rent)/len(rent)
    ownMean = sum(own)/len(own)

    """Prepare the graphing values"""

    means = [mortgageMean, ownMean, rentMean]
    labels = ["MORTGAGE", "OWN", "RENT"]

    """Graph the data using matplot and set the labels"""

    plt.bar([0, 1, 2], means, width=0.6)
    plt.xlabel('Home ownership', fontsize=12)
    plt.ylabel('Average loan amount ($)', fontsize=12)
    plt.title('Average loan amounts per home ownership')
    plt.show()






