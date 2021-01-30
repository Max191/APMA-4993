import csv

counties = []
path = "csv/Florida_Avg_Doubling_Times.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[0] != '' and line[0] != "County":
            counties.append((line[0], line[1]))

matching_counties = []
path = "csv/Unemployment.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[87] != '' and line[1] == 'FL' and line[2] != "Florida":
            current = line[2]
            fips = line[0]
            for county, double_time in counties:
                if current.lower().__contains__(county.lower()):
                    matching_counties.append([fips, current, double_time])
                    break


wr = csv.writer(open('csv/Doubling_time_by_fips.csv', 'w', newline=''), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
wr.writerow(['FIPS', 'County Name', 'Avg Doubling Time'])
wr.writerows(matching_counties)