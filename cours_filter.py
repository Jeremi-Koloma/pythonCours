# La function Filter permet de filter une liste
years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

# Filter les années supérieur à 2011


def years_greater_2011(year):
    return year > 2011


print(list(filter(years_greater_2011, years)))
print(years)
