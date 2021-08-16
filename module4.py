def function(DataSet):
    """This function takes input parameter as a list of dictionaries and
    filters out population of ASEAN Countries over years between 2004 and
    2014."

    Args:
        DataSet [list[dict]]: list of dictionaries where every
        element of the list is a record of country's population corresponding
        to the respective year
    """
    asean = ["Brunei Darussalam", "Cambodia", "Indonesia", "Laos", "Malaysia",
             "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"]
    years = ['2004', '2007', '2010', '2013']

    # Creating an empty dictionary to keep track of each years population data
    years_hashmap = {}

    # Iterating through the Dataset
    for entry in DataSet:
        if entry['Year'] in years and entry['Region'] in asean:
            if entry['Region'] in years_hashmap.keys():
                years_hashmap[entry['Region']].append(float(entry['Population']
                                                            ))
            else:
                years_hashmap[entry['Region']] = [float(entry['Population'])]
    return years_hashmap
