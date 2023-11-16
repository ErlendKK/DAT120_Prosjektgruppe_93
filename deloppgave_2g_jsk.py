

# Finn antall penværsdager for hvert år og plott dette.
#  Man kan finne antall penværsdager ved å sjekke gjennomsnittlig skydekke.
#  Hver dag med verdi 3 eller lavere er en penværsdag.
#  Inkluder bare år hvor det er data om skydekke for mesteparten av året, det må være data for minst 300 dager for at et år skal være gyldig.


from deloppgave_2a_ekk import data_parser
from datetime import datetime
import matplotlib.pyplot as plt


def return_number_of_clear_days(text_file):
    vaer_data = data_parser(text_file)
    clear_days_count = {}
    clear_days = 0
    day_counter = 0
    valid_years = set()

    for row in vaer_data:
        date = row['Dato']
        skydekke = row['Gj_skydekke']

        if (skydekke == "" or skydekke == "-") or (date == "" or date == "-"):
            continue
     
        skydekke = float(skydekke.replace(",", "."))
        date_parsed = datetime.strptime(date, "%d.%m.%Y")
        year = date_parsed.year
        day_counter += 1

        if year not in clear_days_count:
            clear_days_count[year] = 0
            if year-1 in clear_days_count and day_counter >= 300:
                clear_days_count[year-1] = clear_days
                valid_years.add(year-1)
        
            day_counter = 0
            clear_days = 0
        
        if skydekke <= 3:  # Endret betingelsen her
            clear_days += 1

    if day_counter >= 300:
        clear_days_count[year] = clear_days

    return {year: days for year, days in clear_days_count.items() if year in valid_years}


def plot_number_of_clear_days(text_file): 
    year_clear_days = return_number_of_clear_days(text_file)

    years = [key for key in year_clear_days.keys()]
    clear_days = [value for value in year_clear_days.values()]
    
    plt.plot(years, clear_days, marker='o', color='green', label='Antall penværsdager')
    plt.xlabel('År')
    plt.ylabel('Antall dager')
    plt.legend()
    plt.show()

plot_number_of_clear_days('snoedybder_vaer_en_stasjon_dogn.csv')