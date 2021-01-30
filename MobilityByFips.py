import csv

counties = {}
path = "csv/Florida Mobility Data 12-14.csv"
with open(path, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for line in csv_reader:
        if line[6] != '' and line[6] != "census_fips_code":
            if line[6] in counties:
                county = counties[line[6]]
                counties[line[6]] = [float(line[8])+county[0], float(line[9])+county[1], float(line[10])+county[2], float(line[11])+county[3], float(line[12])+county[4], float(line[13])+county[5], float(line[14])+county[6], 1.0+county[7]]
            else:
                counties[line[6]] = [float(line[8]), float(line[9]), float(line[10]), float(line[11]), float(line[12]), float(line[13]), float(line[14]), 1.0]
for county in counties:
    c = counties[county]
    counties[county] = [c[0]/c[7], c[1]/c[7], c[2]/c[7], c[3]/c[7], c[4]/c[7], c[5]/c[7], c[6]/c[7], c[7]]
mobilities_by_fips = [['FIPS', 'Retail and Recreation', 'Grocery and Pharmacy', 'Parks', 'Transit Stations', 'Workplaces', 'Residential', 'Average', 'Data points']]
for county in counties:
    l = [county]
    l.extend(counties[county])
    mobilities_by_fips.append(l)

print(mobilities_by_fips)
# matching_counties = []
# path = "csv/Unemployment.csv"
# with open(path, "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for line in csv_reader:
#         if line[87] != '' and line[1] == 'FL' and line[2] != "Florida":
#             current = line[2]
#             fips = line[0]
#             for county, double_time in counties:
#                 if current.lower().__contains__(county.lower()):
#                     matching_counties.append([fips, current, double_time])
#                     break


wr = csv.writer(open('csv/Mobility_by_fips.csv', 'w', newline=''), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
wr.writerows(mobilities_by_fips)