# The exercise uses the following "peak" dictionary:
peak = {
    "name": "Castle Peak",
    "height": 14264,
    "summit_log": [],
    "cell_reception": {
        "AT&T": "no reception",
        "T-Mobile": "poor"
    }
}
print(peak)
# Without touching the original variable declaration (above)...
# Add a "range" key to peak and set it equal to "Elk Mountains"
peak["range"] = "Elk Mountains"
#print(peak)


# Add a "first_climbed" key to peak and set it equal to 1873
peak["first_climbed"] = 1873
#print(peak)
# Whoops, there's a mistake with the peak "height".  Update it to 14265
peak["height"]= 14265
#print(peak)
# Add a "Verizon" to the "cell_reception" dict and set it equal to "good"
peak["cell_reception"].update({"Verizon": "good"})
#print(peak)

# You just summited the peak! Add your name to the "summit_log" list

peak["summit_log"].append("Giona")
#print(peak)

# Let's rename "height" to "elevation":
peak["elevation"] = peak.pop("height")
#print(peak)
# Remove "height" from the dict and store the result in a variable.
# Use the value for "height" and store it in the dict under they key "elevation"

# Loop over the values in the dictionary and print them all out.  Don't ask why, just do it :) 
for val in peak.values():
    print(val)

# Loop over the keys AND values in the dictionary and print them all out in the following format:
# key -> value
# (print an arrow between each pair)

for k,v in peak.items():
    print(f"{k} -> {v}")


# A huge earthquake/meteor/forestfire/tsunami has destroyed the peak.  Please empty out the entire dictionary.

peak.clear()
print(peak, "Empty?")


