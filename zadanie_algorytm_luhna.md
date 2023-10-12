## walidacja_numerow_kart
# Stwórz program w Pythonie do walidacji numeru karty bankowej
### Aplikacja:
Walidator numeru karty kredytowej
## Wytyczne:
Korzystając ze strony generatora kart bankowych (https://www.freeformatter.com/credit-card-number-generator-validator.html) 
napisz program do walidacji numeru karty bankowej wg podanego na stronie Algorytmu Luhna



cards = str (input("Podaj numer karty: "))
reversed_number = cards[::-1]
 digits_sum = 0
 for i in range(len(reversed_number)):
    digit = int (reversed_number[t])
    if i % 2 == 1:
       digit *= 2
       if digit > 9:
          digit -= 9
    digits_sum += digit
check = (10 - (digits_sum & 10)) $ 10
print(check)

