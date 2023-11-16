

# h) For hvert år finn høyeste middelvind samt medianen for vindstyrke. 
# For å finne medianen, lag ei liste over alle verdiene for det året, sorter lista, og plukk ut det midterste elementet i den sorterte lista. 
# Plott dette for hvert år. Inkluder bare år hvor det er data om vind for mesteparten av året, det må være data for minst 300 dager for at et år skal være gyldig.

import numpy as np
from deloppgave_2a_ekk import data_parser
from datetime import datetime
import matplotlib.pyplot as plt

def return_wind_stats(text_file):
    vaer_data = data_parser(text_file)
    wind_stats = {}
    wind_data = {}
    day_counter = 0
    valid_years = set()

    for row in vaer_data:
        date = row['Dato']
        vindstyrke = row['Max_middelvind']

        if (vindstyrke == "" or vindstyrke == "-") or (date == "" or date == "-"):
            continue
     
        vindstyrke = float(vindstyrke.replace(",", "."))
        date_parsed = datetime.strptime(date, "%d.%m.%Y")
        year = date_parsed.year
        day_counter += 1

        if year not in wind_data:
            wind_data[year] = []
        
        wind_data[year].append(vindstyrke)

        if year not in wind_stats:
            wind_stats[year] = {'highest_mean_wind': 0, 'median_wind': 0}
            if year-1 in wind_stats and day_counter >= 300:
                wind_stats[year-1]['highest_mean_wind'] = np.max(np.mean(wind_data[year-1]))
                wind_stats[year-1]['median_wind'] = np.median(wind_data[year-1])
                valid_years.add(year-1)
                wind_data[year-1] = []
        
            day_counter = 0

    if day_counter >= 300:
        wind_stats[year]['highest_mean_wind'] = np.max(np.mean(wind_data[year]))
        wind_stats[year]['median_wind'] = np.median(wind_data[year])

    return {year: stats for year, stats in wind_stats.items() if year in valid_years}


def plot_wind_stats(text_file): 
    year_wind_stats = return_wind_stats(text_file)

    years = [key for key in year_wind_stats.keys()]
    highest_mean_wind = [value['highest_mean_wind'] for value in year_wind_stats.values()]
    median_wind = [value['median_wind'] for value in year_wind_stats.values()]
    
    plt.plot(years, highest_mean_wind, marker='o', color='blue', label='Høyeste middelvind')
    plt.plot(years, median_wind, marker='o', color='red', label='Median vindstyrke')
    plt.xlabel('År')
    plt.ylabel('Vindstyrke')
    plt.legend()
    plt.show()

plot_wind_stats('snoedybder_vaer_en_stasjon_dogn.csv')