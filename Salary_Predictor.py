#!/usr/bin/env python3


import pandas

population_data_by_county = "/Users/seancross/Desktop/All Projects/Hackathon_2025/Population.csv"
population_data_by_county = pandas.read_csv(population_data_by_county)
county_names = list(population_data_by_county.County.unique())
population_by_county = list(population_data_by_county.Value.unique())

university_attendance_by_county = "/Users/seancross/Desktop/All Projects/Hackathon_2025/University.txt.csv"
university_attendance_by_county_info = pandas.read_csv(university_attendance_by_county)
University_attendance_value = list(university_attendance_by_county_info.Value.unique())

salary_info = "/Users/seancross/Desktop/All Projects/Hackathon_2025/Salaries.txt.csv"
salary_numbers = pandas.read_csv(salary_info)
male_salaries = list(salary_numbers.ValueM.unique())
female_salaries = list(salary_numbers.ValueF.unique())

G_in = str(input("Please enter M for Male or F for female: "))
C_in = input("please enter your county with a capital letter: ")
t = 0
i = 0

while i < 27:
    if C_in == county_names[i]:
        i = 27
    else:
        i += 1
        t += 1

if G_in == "M" or "m":
    salary = str(male_salaries[t] * 52)
elif G_in == "F" or "f":
    salary = str(female_salaries[t] * 52)
else:
    salary = str(male_salaries[t] * 52)

percentage_college_of_attendance = str(((University_attendance_value[t] / population_by_county[t]) * 100) - (((University_attendance_value[t] / population_by_county[t]) * 100) % 0.01))

print("Your Percentage of attendance of third level education within your county is "+percentage_college_of_attendance+"% and the mean annual salary is €"+salary)

