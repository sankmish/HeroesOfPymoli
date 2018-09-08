""" 
1) Although males comprise most of the player base (84%) and therefore most of the total purchases, they spend less on average 
total purchases than females and other/non-disclosed. Males only spend $4.07 on average while females spend $4.47 and 
other/ non-disclosed spend $4.56 on average.

2) Oathbreaker, Last Hope of the Breaking Storm was the most profitable item as well as the most popular item based on purchases.

3) There have been 780 total purchaces on 183 unique items for a total item revenue of $2,379.77.

Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).
"""

# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

totalPlayers = purchase_data["SN"].nunique()
totalPlayers_df = pd.DataFrame({"Total Players" : [totalPlayers]})
totalPlayers_df

uniqueItems = purchase_data["Item ID"].nunique()
averagePrice = purchase_data["Price"].mean()
totalRevenue = purchase_data["Price"].sum()
totalPurchases = purchase_data["Price"].count()
purchasingTotal_df = pd.DataFrame({"Number of Unique Items" : [uniqueItems], "Average Price" : [averagePrice], 
                                   "Number of Purchase": totalPurchases, "Total Revenue" : [totalRevenue]})
purchasingTotal_df["Average Price"] = purchasingTotal_df["Average Price"].map("${:,.2f}".format)
purchasingTotal_df["Total Revenue"] = purchasingTotal_df["Total Revenue"].map("${:,.2f}".format)
purchasingTotal_df

nonrepeatedID_df = purchase_data
nonrepeatedID_df = nonrepeatedID_df.drop_duplicates(subset="SN")
data = nonrepeatedID_df["Gender"].value_counts()
data2  = nonrepeatedID_df["Gender"].value_counts(normalize=True)
genderDemographics_df = pd.DataFrame({"Total Count" : data, "Percentage of Players": data2})
genderDemographics_df["Percentage of Players"] = genderDemographics_df["Percentage of Players"].map("{:,.2f}".format)
genderDemographics_df

gender_df = purchase_data.groupby(["Gender"])
purchaseCount = gender_df["Price"].count()
averagePurchasePrice = gender_df["Price"].mean()
totalPurchaseValue = gender_df["Price"].sum()
genderCount_df = nonrepeatedID_df["Gender"].value_counts()
avgPurchasePerPerson = totalPurchaseValue/genderCount_df
genderPurchasing_df = pd.DataFrame({"Purchase Count" : purchaseCount, "Average Purchase Price" : averagePurchasePrice, 
                                    "Total Purchase Value" : totalPurchaseValue,
                                    "Avg Total Purchase per Person" : avgPurchasePerPerson})
genderPurchasing_df["Average Purchase Price"] = genderPurchasing_df["Average Purchase Price"].map("${:,.2f}".format)
genderPurchasing_df["Total Purchase Value"] = genderPurchasing_df["Total Purchase Value"].map("${:,.2f}".format)
genderPurchasing_df["Avg Total Purchase per Person"] = genderPurchasing_df["Avg Total Purchase per Person"].map("${:,.2f}".format)
genderPurchasing_df

bins = [0, 9, 14, 19, 24, 29, 34, 39, 5000]
groups = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
totalPlayers = len(purchase_data["SN"].unique())
nonrepeatedID_df["Grouped Age"] = pd.cut(nonrepeatedID_df["Age"], bins, labels=groups)
groupedAge_df = nonrepeatedID_df.groupby("Grouped Age")
ageGroupedCount = groupedAge_df["Grouped Age"].count()
ageGroupedPercent = groupedAge_df["Grouped Age"].count() / totalPlayers * 100
ageDemographics_df = pd.DataFrame({"Total Count" : ageGroupedCount, "Percentage of Players": ageGroupedPercent})
ageDemographics_df

bins = [0, 9, 14, 19, 24, 29, 34, 39, 5000]
groups = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
purchase_data["Grouped Age"] = pd.cut(purchase_data["Age"], bins, labels=groups)
groupedAgePurchases = purchase_data.groupby("Grouped Age")
groupedAgePurchaseCount = groupedAgePurchases["Price"].count()
groupedAgeAveragePurchasePrice =  groupedAgePurchases["Price"].mean()
groupedAgeTotalPurchaseValue =  groupedAgePurchases["Price"].sum()
groupedAgeAverageTotalPurchase = groupedAgeTotalPurchaseValue / ageGroupedCount
agePurchasing_df = pd.DataFrame({"Purchase Count": groupedAgePurchaseCount,
                              "Average Purchase Price": groupedAgeAveragePurchasePrice, 
                             "Total Purchase Value": groupedAgeTotalPurchaseValue, 
                              "Average Total Purchase per Person": groupedAgeAverageTotalPurchase})
agePurchasing_df["Average Purchase Price"] = agePurchasing_df["Average Purchase Price"].map("${:,.2f}".format)
agePurchasing_df["Total Purchase Value"] = agePurchasing_df["Total Purchase Value"].map("${:,.2f}".format)
agePurchasing_df["Average Total Purchase per Person"] = agePurchasing_df["Average Total Purchase per Person"].map("${:,.2f}".format)
agePurchasing_df

groupedSN_df = purchase_data.groupby("SN")
groupedSNPurchaseCount = groupedSN_df["SN"].count()
groupedSNAveragePurchasePrice = groupedSN_df["Price"].mean()
groupedSNTotalPurchaseValue = groupedSN_df["Price"].sum()
SNPurchasing_df = pd.DataFrame({"Purchase Count": groupedSNPurchaseCount,
                              "Average Purchase Price": groupedSNAveragePurchasePrice, 
                             "Total Purchase Value": groupedSNTotalPurchaseValue})
SNPurchasing_df = SNPurchasing_df.sort_values(["Total Purchase Value"], ascending=False)
SNPurchasing_df["Average Purchase Price"] = SNPurchasing_df["Average Purchase Price"].map("${:,.2f}".format)
SNPurchasing_df["Total Purchase Value"] = SNPurchasing_df["Total Purchase Value"].map("${:,.2f}".format)
SNPurchasing_df.head()

groupedItem_df = purchase_data[["Item ID", "Item Name", "Price"]].groupby(["Item ID", "Item Name"])
groupedItemPurchaseCount = groupedItem_df["Item ID"].count()
groupedItemPrice = groupedItem_df["Price"].mean()
groupedItemTotalPurchaseValue = groupedItemPurchaseCount * groupedItemPrice
groupedPopularItem_df = pd.DataFrame({"Purchase Count": groupedItemPurchaseCount,
                              "Average Purchase Price": groupedItemPrice, 
                             "Total Purchase Value": groupedItemTotalPurchaseValue})
groupedPopularItem_df = groupedPopularItem_df.sort_values(["Purchase Count"], ascending=False)
groupedPopularItem_df["Average Purchase Price"] = groupedPopularItem_df["Average Purchase Price"].map("${:,.2f}".format)
groupedPopularItem_df["Total Purchase Value"] = groupedPopularItem_df["Total Purchase Value"].map("${:,.2f}".format)
groupedPopularItem_df.head()

groupedItem2_df = purchase_data[["Item ID", "Item Name", "Price"]].groupby(["Item ID", "Item Name"])
groupedProfitableItemPurchaseCount = groupedItem_df["Item ID"].count()
groupedProfitableItemPrice = groupedItem2_df["Price"].mean()
groupedProfitableItemTotalPurchaseValue = groupedProfitableItemPurchaseCount * groupedProfitableItemPrice
groupedProfitableItem_df = pd.DataFrame({"Purchase Count": groupedProfitableItemPurchaseCount,
                              "Average Purchase Price": groupedProfitableItemPrice, 
                             "Total Purchase Value": groupedProfitableItemTotalPurchaseValue})
groupedProfitableItem_df = groupedProfitableItem_df.sort_values(["Total Purchase Value"], ascending=False)
groupedProfitableItem_df["Average Purchase Price"] = groupedProfitableItem_df["Average Purchase Price"].map("${:,.2f}".format)
groupedProfitableItem_df["Total Purchase Value"] = groupedProfitableItem_df["Total Purchase Value"].map("${:,.2f}".format)
groupedProfitableItem_df.head()