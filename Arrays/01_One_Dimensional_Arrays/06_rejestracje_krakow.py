# Zadanie 6: wypisywanie numerów rejestracyjnych z Krakowa.
polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]

counter = 1  # Numer kolejny wyświetlonego krakowskiego pojazdu.

for car_number in polish_license_plates:
    # Rejestracje krakowskie zaczynają się od KR albo KK.
    if car_number.startswith("KR") or car_number.startswith("KK"):
        print(f"{counter}. {car_number}")
        counter += 1  # Zwiększamy numer tylko po znalezieniu pasującej rejestracji.
