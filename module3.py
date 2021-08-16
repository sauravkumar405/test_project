
def function(DataSet):
    
    saarc = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives",
             "Nepal", "Sri Lanka", "Pakistan"]

    # creating a hashmap to track total population count of each year
    years_hashmap: dict[str:float] = {}
    
    # Iterating through the dataset
    for entry in DataSet:
        if entry['Region'] in saarc:
            if entry['Year'] in years_hashmap.keys():
                years_hashmap[entry['Year']] += float(entry['Population'])
            else:
                years_hashmap[entry['Year']] = float(entry['Population'])
                
    # Dicing the plotting data for improved visibility
    years: list[str] = list(years_hashmap.keys())[::3]
    total_population: list[float] = list(years_hashmap.values())[::3]

    ans = []
    ans.append(years)
    ans.append(total_population)
    return ans
