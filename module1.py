
def function(DataSet):
    population = []
    years = []
    # Iterating through the DataSet entry
    for entry in DataSet:
        if entry['Region'] == "India":
            population.append(entry['Population'])
            years.append(entry['Year'])
    # Dicing the data for improved visibility
    population = population[::3]
    years = years[::3]
    ans = []
    ans.append(population)
    ans.append(years)
    return ans
