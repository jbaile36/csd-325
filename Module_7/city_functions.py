# Joshua Bailey Module 7 Assignment CSD 325: Adv. Python
# This program defines a function city_country()
# and calls that function to print various combinations
# of City, Country, Population, and Language.

def city_country(city, country, population=None, language=None):
    # Return a string of the form City, Country - population population, language.
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    # Population, but no language, print city, country, and population.
    elif population:
        return f"{city}, {country} - population {population}"
    # No population, but launguage, print city, country, and language.
    elif language:
        return f"{city}, {country}, {language}"
    # No population or language, print just city and country.
    else:
        return f"{city}, {country}"

# Main function, showing city_country function.
def main():
    print(city_country("Santiago", "Chile"))
    print(city_country("London", "England", 9100000))
    print(city_country("Munich", "Germany", 1600000, "German"))
    
# Call main
if __name__ == "__main__":
    main()