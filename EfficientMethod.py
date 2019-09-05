import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':

    """Extract raw data from csvs"""

    loanData = pd.read_csv("loan_data.csv")
    homeData = pd.read_csv("home_ownership_data.csv")

    """Combine both data frames and keep relevant columns"""

    df = pd.merge(homeData, loanData, how='left', on='member_id')
    df1 = df[['loan_amnt', 'home_ownership']]

    """Calculate average of each home ownership status"""

    means = df1.groupby(['home_ownership']).mean()

    """Convert data frame to a list to use matplot"""

    meansList = means.values.tolist()

    graphMeans = []

    for subList in meansList:
        for mean in subList:
            graphMeans.append(mean)

    """Graphing using matplotlib"""

    plt.bar([0, 1, 2], graphMeans, width=0.6)
    plt.xlabel('Home ownership', fontsize=12)
    plt.ylabel('Average loan amount ($)', fontsize=12)
    plt.title('Average loan amounts per home ownership')
    plt.show()


