import csv
import json

csvfile = open('201508_trip_data.csv', 'r')
jsonfile = open('201508_trip_data.json', 'w')


fieldnames = ("Trip_id", "Duration", "Start_date", "Start_station", "Start_terminal", "End_date", "End_station", "End_terminal", "Bike_id", "Subscription_type", "Zipcode")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
