import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("Zomato-data- (1).csv")



def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)


dataframe['rate'] = dataframe['rate'].apply(handleRate)


def show_head():
    print(dataframe.head())


def show_info():
    print(dataframe.info())


def countplot_restaurant_type():
    sns.countplot(x=dataframe['listed_in(type)'])
    plt.xlabel("Type of restaurant")
    plt.show()


def votes_by_restaurant_type():
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})
    plt.plot(result, c='green', marker='o')
    plt.xlabel('Type of restaurant', c='red', size=20)
    plt.ylabel('Votes', c='red', size=20)
    plt.show()


def max_voted_restaurant():
    max_votes = dataframe['votes'].max()
    restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
    print('Restaurant(s) with the maximum votes:')
    print(restaurant_with_max_votes)


def countplot_online_order():
    sns.countplot(x=dataframe['online_order'])
    plt.show()


def ratings_distribution():
    plt.hist(dataframe['rate'], bins=5)
    plt.title('Ratings Distribution')
    plt.show()


def countplot_approx_cost():
    couple_data = dataframe['approx_cost(for two people)']
    sns.countplot(x=couple_data)
    plt.show()


def boxplot_online_order_vs_rating():
    plt.figure(figsize=(6, 6))
    sns.boxplot(x='online_order', y='rate', data=dataframe)
    plt.show()


def heatmap_online_order_vs_type():
    pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
    plt.title('Heatmap')
    plt.xlabel('Online Order')
    plt.ylabel('Listed In (Type)')
    plt.show()


# Switch-case like dictionary
switch_case = {
    1: show_head,
    2: show_info,
    3: countplot_restaurant_type,
    4: votes_by_restaurant_type,
    5: max_voted_restaurant,
    6: countplot_online_order,
    7: ratings_distribution,
    8: countplot_approx_cost,
    9: boxplot_online_order_vs_rating,
    10: heatmap_online_order_vs_type
}


def main():
    while True:
        print("\nChoose an operation:")
        print("1. Show first 5 rows")
        print("2. Show dataset info")
        print("3. Countplot of restaurant type")
        print("4. Total votes by restaurant type")
        print("5. Restaurant with maximum votes")
        print("6. Countplot of online order")
        print("7. Ratings distribution")
        print("8. Countplot of approx cost")
        print("9. Boxplot of online order vs rating")
        print("10. Heatmap of online order vs type")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice in switch_case:
            switch_case[choice]()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
