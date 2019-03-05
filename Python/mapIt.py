#! python3
# mapIt.py - Launches a map in the browser using an address from the user input1
import webbrowser, sys

address = input("Where are you trying to find directions for? ")
address = address.replace(" ", "+")

webbrowser.open('https://www.google.com/maps/place/' + address)