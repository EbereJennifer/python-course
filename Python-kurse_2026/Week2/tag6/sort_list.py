#sort is a method for lists

zahlen = [3, -1, 5, -2]
neue_liste = sorted(zahlen)
print(f"zahlen: {zahlen}, neue_liste: {neue_liste}")

zahlen.sort()
print(f"zahlen: {zahlen}")

city = {"hamburg", "köln", "Aachen", "Frankfurt"} #set doesn't care about the arrangment of the elements inside it
print(type(city), city)
#city.sort method does not exist

city_sorted = sorted(city)
print(type(city_sorted), city_sorted)