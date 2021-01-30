import csv

counties_pop = []
counties_area = []

path = "csv/florida_county_population.csv"
first_line = True
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if first_line:
            first_line = False
        else:
            counties_pop.append((line[0], float(line[1])))

path = "csv/florida_county_land_areas.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        counties_area.append((line[0], float(line[1].replace(',', ''))))

matching_counties = []
path = "csv/Unemployment.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[87] != '' and line[1] == 'FL' and line[2] != "Florida":
            current = line[2]
            fips = line[0]
            for county_pop, pop in counties_pop:
                if current.lower().__contains__(county_pop.lower()):
                    for county_area, area in counties_area:
                        if current.lower().__contains__(county_area.lower()):
                            matching_counties.append([fips, current, pop/area])
                            break
                    break

wr = csv.writer(open('csv/population_density_by_fips.csv', 'w', newline=''), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
wr.writerow(['FIPS', 'County Name', 'Population density'])
wr.writerows(matching_counties)
