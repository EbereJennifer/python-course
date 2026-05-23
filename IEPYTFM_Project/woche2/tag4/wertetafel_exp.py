
import math
def wertetafel(start, end, anzahl):
    abstand = (end - start) / (anzahl - 1)   # abstand is distance
    for i in range(anzahl):
        x = start + i * abstand
        y = math.exp(x)
        print(f"x = {x:8.4f}, exp(x) = {y:16.4e}")    # e here means wissenschaftliche Darstellung von kommazahlen. scientific notation
                                                      # 8 → total width (minimum number of characters)


wertetafel(10, 100, 20)

# start → where to begin (e.g. 10)
# end → where to stop (e.g. 100)
# anzahl → how many values you want (e.g. 20)
# anzahl - 1?  Because: If you want 20 values, you have 19 gaps between them
# for i in range(anzahl): this runs exactly anzahl times (e.g. 20)
# x = start + i * abstand: This generates evenly spaced values between start and end So you get something like: 10, 14.7, 19.4, ..., 100
# y = math.exp(x) Computes:y = e^x, This grows very fast, especially between 10 and 100.
# This function answers: “What are the values of  𝑒 ** 𝑥 between 10 and 100 at 20 evenly spaced points?”


