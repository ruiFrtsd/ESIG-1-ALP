# Imports

# Constantes

# Procédures et fonctions
def meteo1(humidite, temperature):
    if humidite > 50 and temperature < 20:
        return 'a'
    elif humidite > 60:
        return 'c'
    return 'b'

# Procédure main()
def main():
    print("meteo1(50,15)")
    print(meteo1(50,15))
    print("meteo1(80,25)")
    print(meteo1(50,25))
    print("meteo1(60.1,19)")
    print(meteo1(60.1,19))
# Appel de la procédure main()
if __name__ == "__main__":
    main()
