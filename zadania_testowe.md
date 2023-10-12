## walidacja_numerow_kart
# Lista zadań testowych do walidacji kart bankowych: walidacja długości numeru karty bankowej
### Aplikacja:
Walidator numeru karty kredytowej
## Zadanie testowe:
Korzystając ze strony generatora kart bankowych (https://www.freeformatter.com/credit-card-number-generator-validator.html) 
napisz listę do testowania manualnego dla sprawdzania długości numeru karty bankowej 

##  Kontrola pozytywna
- [ ] napisz 15 zadań testowych
1. Sprawdź dla karty MasterCard, Visa długości 16 liczb
  
## Sprawdzanie wartości granicznych
  - [ ] napisz zadania na sprawdzanie wartości granicznych
1. Długość liczb 15 albo 17 (dla kart długości 16 np. MasterCard i Visa, x-1 i x+1)

## Kontrola negatywna
 - [ ] napisz 8 zadań testowych
 1. Długość mniejsza albo większa niż 16 (np. 5, 10, 20, 17)
 2. Długość jest 0
 3. Napisać litery, znaki i symbole
