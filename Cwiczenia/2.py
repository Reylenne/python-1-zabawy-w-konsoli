# -*- coding: utf8 -*-

"""
kalkulator BMR - Basal metabolic rate
- na podstawie wzoru BMR dostępnego np. na wikipedii w konsoli oblicz swoje BMR
"""
waga = 63
wazrost =162
wiek = 27
S = -161
PMM =  10 * waga + 6.25 * wzrost * wiek + S
print ( " Moje zapotrzebowanie kaloryczne to: " , PMM * 1.2 , "kcal" )
