#fra tuple til list
terning = (1,2,3,4,5,6)
print(type(terning))
terning_liste = list(terning)
print(type(terning_liste))
terning_liste[0]=0
print(terning_liste)
terning=tuple(terning_liste)
print(type(terning))
print(terning)

#fra 2-5
print(terning[2:5])
#med minus
print(terning[-1])