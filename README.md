## walidacja_numerow_kart
# Zadania do wykonania:

1. Uzupełnij plik **zadania_testowe.md**: Stwórz listę zadań testowych do walidacja długości numeru karty bankowej
2. Stwórz funkcję w Pythonie do walidacji poprawności numeru karty bankowej (wytyczne są umieszczone w pliku **zadanie_algorytm_luhna.md**)



## 1. Dla MasterCard długość = 16
## 2. Niepoprawna długość >16 np 5, <16 np 20, niepoprawna długość = 0, niepoprawny ciąg zawiera tekst, symbole specialne
## 3. wartości brzegowe 15, 16, 17




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


