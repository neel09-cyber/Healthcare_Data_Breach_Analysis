import datetime 
import pandas as pd
# pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt

#Creating a dataframe
df = pd.read_csv("data.csv")

#Prints general information about the dataframe
# print(df.info())

#Prints the first 12 lines of the data
# print(df.head())

#Prints the last 12 lines of the data
# print(df.tail(12))

#Prints the functions like sum(), mean(), etc.
# print(df.describe())


#Data Cleaning
# print("Initial Data Shape: ", df.shape)

# print("Missing values in each column BEFORE cleaning: ")
#print(df.isnull().sum())

# print("Duplicate values in the dataset: ")
#print(df.duplicated().sum())


# --------------------------------------------------------------------------------------------
#Data visualization

# Data Cleaning and Preparation for Visualization
# Convert the date column to datetime and extract the year
df["Breach Submission Date"] = pd.to_datetime(df["Breach Submission Date"], format="%m/%d/%Y", errors="coerce")
df["Year"] = df["Breach Submission Date"].dt.year

# Combine "Theft" and "Loss" into a single category "Theft/Loss"
df["Type of Breach"] = df["Type of Breach"].replace({"Theft": "Theft/Loss", "Loss": "Theft/Loss"})

# Filter rows so only years 2009 to 2024 remain. However, I am confident that my data is in the range from year 2009 to 2024
# filtered_df = df[df["Year"].between(2009, 2024)]


# 1st graph
# Now group by 'Year' and count how many breaches occurred each year

def plot_healthcare_breaches_by_year(df):
    # Group by 'Year' and count the number of breaches
    breach_counts_by_year = df.groupby("Year")["Breach Submission Date"].count().reset_index(name="No_of_Breaches")
    print(breach_counts_by_year)

    # Let's visualize this data filtration into a bar graph now
    plt.bar(breach_counts_by_year["Year"], breach_counts_by_year["No_of_Breaches"], color="blue")
    for index, row in breach_counts_by_year.iterrows():
        plt.text(row["Year"], row["No_of_Breaches"] + 10.0, str(row["No_of_Breaches"]), ha="center", fontsize=9) # Annotate each bar with the count of breaches
    plt.xlabel("Year")
    plt.xticks(breach_counts_by_year["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_Breaches")
    plt.title("Healthcare Data Breaches of 5000+ Records (2009 - 2024)")
    plt.tight_layout() # Adjust layout to make room for the title and labels
    plt.show()



# ---------------------------------------------------------------------------------
# 2nd graph
# Now let's visualize the number of individuals affected by healthcare security breaches over the years in a line graph.

def plot_individuals_affected_by_year(df):
    # Group by 'Year' and sum the 'Individuals Affected'
    ind_aff_by_year = df.groupby("Year")["Individuals Affected"].sum().reset_index(name="No_of_people_affected")
    print(ind_aff_by_year)

    y_ticks = [10_000_000, 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000, 70_000_000, 80_000_000, 90_000_000, 100_000_000, 110_000_000 ] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas, e.g., 10,000,000

    # Let's visualize this data filtration into a line graph now
    plt.plot(ind_aff_by_year["Year"], ind_aff_by_year["No_of_people_affected"], color="red") # Adding marker for better visibility
    plt.xlabel("Year")
    plt.xticks(ind_aff_by_year["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_people_affected")
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability, adjust as needed    plt.title("Individuals Affected by Healthcare Security Breaches (2009 - 2024)")
    plt.grid(True) # Add grid lines for better readability 
    plt.tight_layout()
    plt.show()


# --------------------------------------------------------------------------------
# 3rd graph
# Now let's visualize the causes of healthcare data breaches over the years in a line graph.

def plot_causes_of_breaches_by_year(df):
    # Group by 'Year' and 'Type of Breach' and count the number of breaches
    causes_by_year = df.groupby(["Year", "Type of Breach"])["Breach Submission Date"].count().reset_index(name="No_of_Breaches_type")
    print(causes_by_year)
    plt.plot(causes_by_year[causes_by_year["Type of Breach"] == "Hacking/IT Incident"]["Year"],
            causes_by_year[causes_by_year["Type of Breach"] == "Hacking/IT Incident"]["No_of_Breaches_type"],
            label="Hacking/IT Incident", color="blue")
    plt.plot(causes_by_year[causes_by_year["Type of Breach"] == "Theft/Loss"]["Year"],
            causes_by_year[causes_by_year["Type of Breach"] == "Theft/Loss"]["No_of_Breaches_type"],
            label="Theft/Loss", color="grey")
    plt.plot(causes_by_year[causes_by_year["Type of Breach"] == "Unauthorized Access/Disclosure"]["Year"],
            causes_by_year[causes_by_year["Type of Breach"] == "Unauthorized Access/Disclosure"]["No_of_Breaches_type"],
            label="Unauthorized Access/Disclosure", color="orange")
    plt.plot(causes_by_year[causes_by_year["Type of Breach"] == "Improper Disposal"]["Year"], 
            causes_by_year[causes_by_year["Type of Breach"] == "Improper Disposal"]["No_of_Breaches_type"],
            label="Improper Disposal", color="green")
    plt.xlabel("Year") # X-axis label for the graph
    plt.xticks(causes_by_year["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel('No_of_Breaches_type') # Y-axis label for the graph
    plt.title("Causes of Healthcare Data Breaches (2009 - 2024)") # Title of the graph
    plt.tight_layout() # Adjust layout to make room for the title and labels
    plt.legend()
    plt.grid(True) # Add grid lines for better readability
    plt.show() # Display the graph



# 4th graph

# Let's visualize how many individuals were affected by each type of breach from 2009 to 2024.
# Group by 'Year' and 'Type of Breach' and sum the 'Individuals Affected'

def plot_individuals_by_type(df):
    individuals_by_type = df.groupby(["Year", "Type of Breach"])["Individuals Affected"].sum().reset_index(name="No_of_people_affected_type")
    print(individuals_by_type)

    y_ticks = [10_000_000, 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000, 70_000_000, 80_000_000, 90_000_000, 100_000_000, 110_000_000 ] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas, e.g., 10,000,000
    # Now let's visualize the individuals affected by each type of breach in a line graph
    plt.plot(individuals_by_type[individuals_by_type["Type of Breach"] == "Hacking/IT Incident"]["Year"],
            individuals_by_type[individuals_by_type["Type of Breach"] == "Hacking/IT Incident"]["No_of_people_affected_type"],
            label="Hacking/IT Incident", color="blue")
    plt.plot(individuals_by_type[individuals_by_type["Type of Breach"] == "Theft/Loss"]["Year"],
            individuals_by_type[individuals_by_type["Type of Breach"] == "Theft/Loss"]["No_of_people_affected_type"],
            label="Theft/Loss", color="grey")
    plt.plot(individuals_by_type[individuals_by_type["Type of Breach"] == "Unauthorized Access/Disclosure"]["Year"],
            individuals_by_type[individuals_by_type["Type of Breach"] == "Unauthorized Access/Disclosure"]["No_of_people_affected_type"],
            label="Unauthorized Access/Disclosure", color="orange")
    plt.plot(individuals_by_type[individuals_by_type["Type of Breach"] == "Improper Disposal"]["Year"],
            individuals_by_type[individuals_by_type["Type of Breach"] == "Improper Disposal"]["No_of_people_affected_type"],
            label="Improper Disposal", color="green")
    plt.xlabel("Year") # X-axis label for the graph
    plt.xticks(individuals_by_type["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel('No_of_people_affected_type') # Y-axis label for the graph
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability, adjust as needed
    plt.title("Individuals Affected by Type of Healthcare Data Breaches (2009 - 2024)") # Title of the graph
    plt.tight_layout() # Adjust layout to make room for the title and labels        
    plt.legend() # Add a legend to differentiate between the types of breaches
    plt.grid(True) # Add grid lines for better readability 
    plt.show() # Display the graph


# 5th graph
# We're now plotting only Hacking/IT Incident to see its trend over the years separately. This can help in understanding the impact of this specific type of breach.
def plot_hacking_trend(df):
    # Group by 'Year' and count the number of breaches specifically for "Hacking/IT Incident"
    hacking_trend = df[df["Type of Breach"] == "Hacking/IT Incident"].groupby("Year")["Breach Submission Date"].count().reset_index(name="No_of_Breaches_Hacking")
    print(hacking_trend)
    # Let's visualize this data filtration into a bar graph now
    plt.bar(hacking_trend["Year"], hacking_trend["No_of_Breaches_Hacking"], color="blue")
    for index, row in hacking_trend.iterrows():
        plt.text(row["Year"], row["No_of_Breaches_Hacking"] + 10.0, str(row["No_of_Breaches_Hacking"]), ha="center", fontsize=9) # Annotate each bar with the count of breaches
    plt.xlabel("Year")
    plt.xticks(hacking_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_Breaches_by_Hacking") # Y-axis label for the graph, specifically for Hacking/IT Incident
    plt.title("Hacking/IT Incidents (2009 - 2024)")
    plt.tight_layout() # Adjust layout to make room for the title and labels
    plt.show() 

# 6th graph 
# Now we'll plot the individuals affected by Hacking/IT Incident over the years in a line graph to see its trend. This will help us understand the impact of this specific type of breach on individuals affected.
def plot_hacking_individuals_trend(df):
    # Group by 'Year' and sum the 'Individuals Affected' specifically for "Hacking/IT Incident"
    hacking_individuals_trend = df[df["Type of Breach"] == "Hacking/IT Incident"].groupby("Year")["Individuals Affected"].sum().reset_index(name="No_of_people_affected_Hacking")
    print(hacking_individuals_trend)

    y_ticks = [10_000_000, 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000, 70_000_000, 80_000_000, 90_000_000, 100_000_000] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas

    # Let's visualize this data filtration into a line graph now
    plt.stackplot(hacking_individuals_trend["Year"], hacking_individuals_trend["No_of_people_affected_Hacking"], color="red") # Using stackplot to visualize the trend of individuals affected by Hacking/IT Incident
    plt.xlabel("Year")
    plt.xticks(hacking_individuals_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_people_affected_Hacking")
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability
    plt.title("Individuals Affected by Hacking/IT Incidents (2009 - 2024)")
    plt.tight_layout()
    plt.show()      

# 7th graph
# For Unauthorized Access/Disclosure, we will create a similar bar graph to visualize its trend over the years. This will help us understand how this specific type of breach has evolved over time.
def plot_unauthorized_trend(df):
    # Group by 'Year' and count the number of breaches specifically for "Unauthorized Access/Disclosure"
    unauthorized_trend = df[df["Type of Breach"] == "Unauthorized Access/Disclosure"].groupby("Year")["Breach Submission Date"].count().reset_index(name="No_of_Breaches_Unauthorized") # Count the number of breaches for Unauthorized Access/Disclosure
    print(unauthorized_trend)
    # Let's visualize this data filtration into a bar graph now
    plt.bar(unauthorized_trend["Year"], unauthorized_trend["No_of_Breaches_Unauthorized"], color="blue")
    for index, row in unauthorized_trend.iterrows():
        plt.text(row["Year"], row["No_of_Breaches_Unauthorized"] + 10.0, str(row["No_of_Breaches_Unauthorized"]), ha="center", fontsize=9) # Annotate each bar with the count of breaches
    plt.xlabel("Year")
    plt.xticks(unauthorized_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_Breaches_by_Unauthorized") # Y-axis label for the graph, specifically for Hacking/IT Incident
    plt.title("Unauthorized Access/Disclosure Incidents (2009 - 2024)")
    plt.tight_layout() # Adjust layout to make room for the title and labels
    plt.show()


# 8th graph
# Let's create a stacked area chart to visualize the trend of individuals affected by Unauthized Access/Disclosure over the years. This will help us understand the impact of this specific type of breach on individuals affected.
def plot_unauthorized_individuals_trend(df):
    # Group by 'Year' and sum the 'Individuals Affected' specifically for "Unauthorized Access/Disclosure"
    unauthorized_individuals_trend = df[df["Type of Breach"] == "Unauthorized Access/Disclosure"].groupby("Year")["Individuals Affected"].sum().reset_index(name="No_of_people_affected_Unauthorized")
    print(unauthorized_individuals_trend)

    y_ticks = [10_000_000, 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000, 70_000_000, 80_000_000, 90_000_000, 100_000_000] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas

    # Let's visualize this data filtration into a stacked area chart now
    plt.stackplot(unauthorized_individuals_trend["Year"], unauthorized_individuals_trend["No_of_people_affected_Unauthorized"], color="red") # Using stackplot to visualize the trend of individuals affected by Unauthorized Access/Disclosure
    plt.xlabel("Year")
    plt.xticks(unauthorized_individuals_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_people_affected_Unauthorized")
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability
    plt.title("Individuals Affected by Unauthorized Access/Disclosure Incidents (2009 - 2024)")
    plt.tight_layout()
    plt.show()



# 9th graph
# Let's create a bar chart for Improper Disposal incidents to visualize its trend over the years. This will help us understand how this specific type of breach has evolved over time.
def plot_improper_disposal_trend(df):
    # Group by 'Year' and count the number of breaches specifically for "Improper Disposal"
    improper_disposal_trend = df[df["Type of Breach"] == "Improper Disposal"].groupby("Year")["Breach Submission Date"].count().reset_index(name="No_of_Breaches_Improper_Disposal") # Count the number of breaches for Improper Disposal
    print(improper_disposal_trend)
    
    plt.bar(improper_disposal_trend["Year"], improper_disposal_trend["No_of_Breaches_Improper_Disposal"], color="blue") # Create a bar chart for Improper Disposal trend
    for index, row in improper_disposal_trend.iterrows():
        # Annotate each bar with the count of breaches
        plt.text(row["Year"], row["No_of_Breaches_Improper_Disposal"] + 10.0, str(row["No_of_Breaches_Improper_Disposal"]), ha="center", fontsize=9)
    plt.xlabel("Year") # X-axis label for the graph
    plt.ylabel("No_of_Breaches_Improper_Disposal") # Y-axis label for the graph, specifically for Improper Disposal
    plt.xticks(improper_disposal_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.title("Improper Disposal Incidents (2009 - 2024)") # Title of the graph
    plt.tight_layout()
    plt.show()


# 10th graph
# Now let's create a stack plot for the individuals that were affected by Improper Disposal over the years. This will help us understand the impact of this specific type of breach on individuals affected.
def plot_improper_disposal_individuals_trend(df):
    # Group by 'Year' and sum the 'Individuals Affected' specifically for "Improper Disposal"
    improper_disposal_individuals_trend = df[df["Type of Breach"] == "Improper Disposal"].groupby("Year")["Individuals Affected"].sum().reset_index(name="No_of_people_affected_Improper_Disposal")
    print(improper_disposal_individuals_trend)

    y_ticks = [10_000_000, 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas

    # Let's visualize this data filtration into a stacked area chart now
    plt.stackplot(improper_disposal_individuals_trend["Year"], improper_disposal_individuals_trend["No_of_people_affected_Improper_Disposal"], color="red") # Using stackplot to visualize the trend of individuals affected by Improper Disposal
    plt.xlabel("Year")
    plt.xticks(improper_disposal_individuals_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_people_affected_Improper_Disposal")
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability
    plt.title("Individuals Affected by Improper Disposal Incidents (2009 - 2024)") # Title of the graph
    plt.tight_layout()
    plt.show()


# 11th graph 
# Let's create a bar chart for Theft/Loss incidents to visualize its trend over the years. This will help us understand how this specific type of breach has evolved over time.
def plot_theft_loss_trend(df):
    # Group by 'Year' and count the number of breaches specifically for "Theft/Loss"
    theft_loss_trend = df[df["Type of Breach"] == "Theft/Loss"].groupby("Year")["Breach Submission Date"].count().reset_index(name="No_of_Breaches_Theft_Loss") # Count the number of breaches for Improper Disposal
    print(theft_loss_trend)
    
    plt.bar(theft_loss_trend["Year"], theft_loss_trend["No_of_Breaches_Theft_Loss"], color="blue") # Create a bar chart for Theft/Loss trend
    for index, row in theft_loss_trend.iterrows():
        # Annotate each bar with the count of breaches
        plt.text(row["Year"], row["No_of_Breaches_Theft_Loss"] + 10.0, str(row["No_of_Breaches_Theft_Loss"]), ha="center", fontsize=9)
    plt.xlabel("Year") # X-axis label for the graph
    plt.ylabel("No_of_Breaches_Theft_Loss") # Y-axis label for the graph, specifically for Theft/Loss
    plt.xticks(theft_loss_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.title("Theft/Loss Incidents (2009 - 2024)") # Title of the graph
    plt.tight_layout()
    plt.show()



#12th graph
# Let's add the stack plot for the individuals affected by Theft/Loss over the years. This will help us understand the impact of this specific type of breach on individuals affected.
def plot_theft_loss_individuals_trend(df):
    # Group by 'Year' and sum the 'Individuals Affected' specifically for "Theft/Loss"
    theft_loss_individuals_trend = df[df["Type of Breach"] == "Theft/Loss"].groupby("Year")["Individuals Affected"].sum().reset_index(name="No_of_people_affected_Theft_Loss")
    print(theft_loss_individuals_trend)

    y_ticks = [10_000_000, 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas

    # Let's visualize this data filtration into a stacked area chart now
    plt.stackplot(theft_loss_individuals_trend["Year"], theft_loss_individuals_trend["No_of_people_affected_Theft_Loss"], color="red") # Using stackplot to visualize the trend of individuals affected by Theft/Loss
    plt.xlabel("Year")
    plt.xticks(theft_loss_individuals_trend["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_people_affected_Theft_Loss")
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability
    plt.title("Individuals Affected by Theft/Loss Incidents (2009 - 2024)") # Title of the graph
    plt.tight_layout()
    plt.show()

#13th graph
# Now I will visualize the average size (individuals affected) of healthcare data breaches by year in a line graph. This will help us understand the average impact of breaches over time.
def plot_average_size_by_year(df):
    # Group by 'Year' and calculate the average size of breaches (individuals affected) for each year
    average_size_by_year = df.groupby("Year")["Individuals Affected"].mean().reset_index(name="Average_Size")
    print(average_size_by_year)

    y_ticks = [50_000, 100_000, 150_000, 200_000, 250_000, 300_000, 350_000, 400_000, 450_000] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas  
    
    plt.plot(average_size_by_year["Year"], average_size_by_year["Average_Size"], marker='o', color="green") # Line graph with markers for better visibility
    plt.xlabel("Year") # X-axis label for the graph
    plt.xticks(average_size_by_year["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("Average_Size") # Y-axis label for the graph, representing the average size of breaches
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability, adjust as needed
    plt.title("Average Size of Healthcare Data Breaches by Year (2009 - 2024)") # Title of the graph
    plt.tight_layout() # Adjust layout to make room for the title and labels
    plt.grid(True) # Add grid lines for better readability
    plt.show() # Display the graph



# 14th graph
# Median Healthcare Data Breach Size by Year (2009 - 2024)
def plot_median_size_by_year(df):
    # Group by 'Year' and calculate the median size of breaches (individuals affected) for each year
    median_size_by_year = df.groupby("Year")["Individuals Affected"].median().reset_index(name="Median_Size")
    print(median_size_by_year)

    plt.bar(median_size_by_year["Year"], median_size_by_year["Median_Size"], color="purple") # Bar graph for median size by year
    for index, row in median_size_by_year.iterrows():
        # Annotate each bar with the median size
        plt.text(row["Year"], row["Median_Size"] + 15.0, str(int(row["Median_Size"])), ha="center", fontsize=9)
    plt.xlabel("Year") # X-axis label for the graph
    plt.xticks(median_size_by_year["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("Median_Size") # Y-axis label for the graph, representing the median size of breaches
    plt.title("Median Healthcare Data Breach Size by Year (2009 - 2024)") # Title of the graph
    plt.tight_layout() # Adjust layout to make room for the title and labels
    plt.show() # Display the graph


def main():
    while True:
        print("\nSelect a graph to display: ")
        print("1. Healthcare Data Breaches by Year (Bar Graph)")
        print("2. Individuals Affected by Healthcare Security Breaches (Line Graph)")
        print("3. Causes of Healthcare Data Breaches (Line Graph)")
        print("4. Individuals Affected by Type of Healthcare Data Breaches (Line Graph)")
        print("5. Healthcare Data Breaches Trend for Hacking/IT Incident (Bar Graph)") # Added this option to visualize Hacking/IT Incident separately
        print("6. Individuals Affected by Hacking/IT Incidents (Area Chart)")
        print("7. Healthcare Data Breaches Trend for Unauthorized Access/Disclosure (Bar Graph)") # Added this option to visualize Unauthorized Access/Disclosure separately
        print("8. Individuals Affected by Unauthorized Access/Disclosure Incidents (Area Chart)") # Added this option to visualize Unauthorized Access/Disclosure separately
        print("9. Healthcare Data Breaches Trend for Improper Disposal (Bar Graph)") # Added this option to visualize Improper Disposal separately
        print("10. Individuals Affected by Improper Disposal Incidents (Area Chart)") # Added this option to visualize Improper Disposal separately
        print("11. Healthcare Data Breaches Trend for Theft/Loss (Bar Graph)") # Added this option to visualize Theft/Loss separately
        print("12. Individuals Affected by Theft/Loss Incidents (Area Chart)") # Added this option to visualize Theft/Loss separately
        print("13. Average Data Breach Size by Year (Line Graph)") # Added this option to visualize the average size of breaches by year
        print("14. Median Healthcare Data Breach Size by Year (Bar Graph)") # Added this option to visualize the median size of breaches by year        
        print("15. Exit")
        choice = input("Enter your choice (1-15): ")

        if choice == "1":
            plot_healthcare_breaches_by_year(df)
        elif choice == "2":
            plot_individuals_affected_by_year(df)
        elif choice == "3":
            plot_causes_of_breaches_by_year(df)
        elif choice == "4":
            plot_individuals_by_type(df)
        elif choice == "5":
            plot_hacking_trend(df)
        elif choice == "6":
            plot_hacking_individuals_trend(df)
        elif choice == "7":
            plot_unauthorized_trend(df)        
        elif choice == "8":
            plot_unauthorized_individuals_trend(df)
        elif choice == "9":
            plot_improper_disposal_trend(df)
        elif choice == "10":
            plot_improper_disposal_individuals_trend(df)
        elif choice == "11":
            plot_theft_loss_trend(df)  
        elif choice == "12":
            plot_theft_loss_individuals_trend(df)
        elif choice == "13":
            plot_average_size_by_year(df)
        elif choice == "14":
            plot_median_size_by_year(df)        
        elif choice == "15":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 15.") 


if __name__ == "__main__":
    main()