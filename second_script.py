import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_two.csv')

# for some reason one value for year 2018 is missing otherwise the data is clean
# If the website is referring the same data, then they have an extra value for 2018
# Also, there is an asterisk sign and that entry is red colored so I am unsure about that value

# Clean the "Year" column by removing invalid entries
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Drop rows with invalid or missing years
df = df.dropna(subset=['Year'])

# Convert the "Year" column to integers
df['Year'] = df['Year'].astype(int)


# Clean the "Amount" column by removing dollar signs, commas, and extra spaces
df['Amount'] = df['Amount'].str.replace('[\$,]', '', regex=True).str.strip()

# Convert the "Amount" column to numeric
df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

# Convert the "Amount" column to integers
df['Amount'] = df['Amount'].fillna(0).astype(int)

# Count the number of penalties per year

def plot_penalties_year(df):
    # Group the data by year and count the number of penalties
    penalties_per_year = df.groupby('Year').size().reset_index(name='Penalty_Count')
    print(penalties_per_year)

    # Plot the data
    plt.figure(figsize=(10, 6)) # (width, height) in inches
    plt.plot(penalties_per_year['Year'], penalties_per_year['Penalty_Count'], marker='o', color = 'blue')
    
    # Annotate each point with its value
    for i in range(len(penalties_per_year)):
        plt.text(
            penalties_per_year['Year'][i], 
            penalties_per_year['Penalty_Count'][i], 
            str(penalties_per_year['Penalty_Count'][i]), 
            fontsize=15, 
            ha='left', 
            va='top',
            )

    plt.xlabel('Year')
    plt.ylabel('Number of Penalties')
    plt.title('Number of Penalties per Year')
    plt.grid(axis ='y') # Add grid lines for y-axis only
    plt.xticks(penalties_per_year['Year'], rotation=45)
    plt.tight_layout()
    # plt.savefig('penalties_per_year.png') I can save the plot for my report
    plt.show()


def total_penalties_year(df):
    # Group the data by year and sum the penalties
    penalties_per_year = df.groupby(['Year'])['Amount'].sum().reset_index(name='Penalty_sum_year')
    print(penalties_per_year)

    # Plot the data
    y_ticks = [5_000_000, 10_000_000, 15_000_000, 20_000_000, 25_000_000, 30_000_000] # Define y-ticks for the graph
    y_labels = [f"$ {int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas 

    plt.figure(figsize=(12, 7))
    plt.bar(penalties_per_year['Year'], penalties_per_year['Penalty_sum_year'], color='orange')

    # Annotate each bar with its value
    for index, row in penalties_per_year.iterrows():
        plt.text(
            row["Year"], 
            row["Penalty_sum_year"] + 30.0,  # Add an offset for better visibility
            f"$ {row['Penalty_sum_year']:,}", # Format the number with commas and a dollar sign
            ha="center", 
            fontsize=9
        )

    plt.xlabel('Year')
    plt.ylabel('Total Penalty Amount')
    plt.title('Total Penalty Amount per Year')
    plt.xticks(penalties_per_year['Year'], rotation=45)
    plt.yticks(y_ticks, y_labels) # Set the y-ticks and labels
    plt.tight_layout()
    plt.show()


def plot_average_penalty(df):
    # Group the data by year and calculate the average penalty amount
    average_penalty_per_year = df.groupby('Year')['Amount'].mean().reset_index(name='Average_Penalty_Amount')
    print(average_penalty_per_year)

    # Plot the data
    y_ticks = [500_000, 1_000_000, 1_500_000, 2_000_000, 2_500_000, 3_000_000] # Define y-ticks for the graph
    y_labels = [f"$ {int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas 

    plt.figure(figsize=(10, 6)) 
    plt.bar(average_penalty_per_year['Year'], average_penalty_per_year['Average_Penalty_Amount'], color='green', width=0.5)

    # Annotate each bar with its value
    for index, row in average_penalty_per_year.iterrows():
        plt.text(
            row["Year"], 
            row["Average_Penalty_Amount"] + 30.0,  # Add an offset for better visibility
            f"$ {row['Average_Penalty_Amount']:.2f}", # Format the number with commas and a dollar sign
            ha="center", 
            fontsize=7
        )
    plt.xlabel('Year')
    plt.ylabel('Average Penalty Amount')
    plt.yticks(y_ticks, y_labels) # Set the y-ticks and labels
    plt.title('Average Penalty Amount per Year')
    plt.xticks(average_penalty_per_year['Year'], rotation=45)
    plt.tight_layout()
    plt.show()


def plot_median_penalty(df):
    # Group the data by year and calculate the median penalty amount
    median_penalty_per_year = df.groupby('Year')['Amount'].median().reset_index(name='Median_Penalty_Amount')
    print(median_penalty_per_year)

    # Plot the data
    y_ticks = [500_000, 1_000_000, 1_500_000, 2_000_000, 2_500_000, 3_000_000] # Define y-ticks for the graph
    y_labels = [f"$ {int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas 

    plt.figure(figsize=(10, 6)) 
    plt.bar(median_penalty_per_year['Year'], median_penalty_per_year['Median_Penalty_Amount'], color='purple', width=0.5)

    # Annotate each bar with its value
    for index, row in median_penalty_per_year.iterrows():
        plt.text(
            row["Year"], 
            row["Median_Penalty_Amount"] + 30.0,  # Add an offset for better visibility
            f"$ {row['Median_Penalty_Amount']:.2f}", # Format the number with commas and a dollar sign
            ha="center", 
            fontsize=7
        )
    plt.xlabel('Year')
    plt.ylabel('Median Penalty Amount')
    plt.yticks(y_ticks, y_labels) # Set the y-ticks and labels
    plt.title('Median Penalty Amount per Year')
    plt.xticks(median_penalty_per_year['Year'], rotation=45)
   
    plt.tight_layout()
    plt.show()




def main():
    while True:
        print("Welcome to the Penalty Analysis Program!")
        print("Please choose an option:")
        print("1. Plot penalties per year")
        print("2. Plot total penalties per year")
        print("3. Plot average penalty amount per year")
        print("4. Plot median penalty amount per year")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            plot_penalties_year(df)
        elif choice == '2':
            total_penalties_year(df)
        elif choice == '3':
            plot_average_penalty(df)
        elif choice == '4':
            plot_median_penalty(df)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
        print("Exiting the program.")

if __name__ == "__main__":
    main()