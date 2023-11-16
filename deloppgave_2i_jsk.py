

# i) En måte å sjekke trender i temperatur gjennom året er å ta gjennomsnittet av temperaturen for en tidsperiode (for eksempel ei uke eller en måned)
#  og så sjekke om snittet endrer seg. Ved å ta gjennomsnittet så fjerner man at temperaturen går opp og ned fra en dag til den neste.
#  Regn ut gjennomsnittstemperaturen for hver måned (for eksempel april 2007) og legg disse gjennomsnittene i ei ny liste.
#  Bruk funksjonen fra del 1 deloppgave e) for å regne ut ei liste med differanser.
#  Plott både lista over gjennomsnittstemperaturer og lista over differanser med måned og år på x-aksen.
# j) Frivillig, avansert: Ei fil med samme format


from deloppgave_2a_ekk import data_parser
from deloppgave_e import differanse_tall_i_liste
from datetime import datetime
import matplotlib.pyplot as plt 


def calculate_monthly_averages(text_file):
    vaer_data = data_parser(text_file)
    monthly_averages = {}
    monthly_temps = {}
    day_counter = 0

    for row in vaer_data:
        date = row['Dato']
        temperatur = row['Middeltemperatur']

        if (temperatur == "" or temperatur == "-") or (date == "" or date == "-"):
            continue
     
        temperatur = float(temperatur.replace(",", "."))
        date_parsed = datetime.strptime(date, "%d.%m.%Y")
        year_month = date_parsed.strftime("%Y-%m")
        day_counter += 1

        if year_month not in monthly_temps:
            monthly_temps[year_month] = []
        
        monthly_temps[year_month].append(temperatur)

    for year_month, temps in monthly_temps.items():
        monthly_averages[year_month] = sum(temps) / len(temps)

    return monthly_averages


def plot_monthly_temperatures_and_diffs(text_file): 
    monthly_averages = calculate_monthly_averages(text_file)
    temp_diffs = differanse_tall_i_liste(list(monthly_averages.values()))
    months_years = list(monthly_averages.keys())

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(months_years, list(monthly_averages.values()), marker='o', color='green', label='Gjennomsnittstemperatur')
    plt.title('Gjennomsnittstemperatur per måned')
    plt.xlabel('År og måned')
    plt.ylabel('Temperatur (°C)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(months_years[1:], temp_diffs, marker='o', color='blue', label='Differanse i gjennomsnittstemperatur')
    plt.title('Differanse i gjennomsnittstemperatur mellom måneder')
    plt.xlabel('År og måned')
    plt.ylabel('Temperaturdifferanse (°C)')
    plt.legend()

    plt.tight_layout()
    plt.show()

plot_monthly_temperatures_and_diffs('snoedybder_vaer_en_stasjon_dogn.csv')