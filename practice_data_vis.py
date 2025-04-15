def plot_individuals_affected_by_entity_type(df):
    # Group by 'Year' and 'Entity Type' and sum the 'Individuals Affected'
    individuals_affected_entity = df.groupby(["Year", "Covered Entity Type"])["Individuals Affected"].sum().reset_index(name="No_of_people_affected_by_Entity_Type")
    print(individuals_affected_entity)

    y_ticks = [10_000_000, 20_000_000, 30_000_000, 40_000_000, 50_000_000, 60_000_000] # Define y-ticks for the graph
    y_labels = [f"{int(y):,}" for y in y_ticks] # Format y-ticks to be more readable with commas

    # Create a stacked area chart for individuals affected by entity type
    plt.stackplot(individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] ==["Healthcare Provider"]]["Year"],
                  individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] == "Healthcare Provider"]["No_of_people_affected_by_Entity_Type"],
                  label="Healthcare Provider", color="blue")
    plt.stackplot(individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] == "Business Associate"]["Year"],
                  individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] == "Business Associate"]["No_of_people_affected_by_Entity_Type"],
                  label="Business Associate", color="grey")
    plt.stackplot(individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] == "Health Plan"]["Year"],
                  individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] == "Health Plan"]["No_of_people_affected_by_Entity_Type"],
                  label="Health Plan", color="orange")
    plt.stackplot(individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] == "Healthcare Clearinghouse"]["Year"],
                  individuals_affected_entity[individuals_affected_entity["Covered Entity Type"] == "Healthcare Clearinghouse"]["No_of_people_affected_by_Entity_Type"],
                  label="Healthcare Clearinghouse", color="green")
    plt.xlabel("Year") # X-axis label for the graph
    plt.xticks(individuals_affected_entity["Year"], rotation=45) # Rotate x-axis labels for better visibility
    plt.ylabel("No_of_people_affected_by_Entity_Type") # Y-axis label for the graph
    plt.yticks(ticks=y_ticks, labels=y_labels) # Set y-ticks for better readability
    plt.title("Individuals Affected by Entity Type (2009 - 2024)") # Title of the graph
    plt.legend(title="Covered Entity Type") # Add legend to differentiate between the types of breaches
    plt.tight_layout() # Adjust layout to make room for the title and labels
    plt.show() # Display the graph