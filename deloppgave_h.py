def vekstrater(temperatur):
    total_vekst = 0

    for temp in temperatur:
        if temp > 5:
            vekstrater = temp - 5
            total_vekst += vekstrater

    return total_vekst
