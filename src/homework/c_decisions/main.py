import decisions

options = int(input('Please enter a number for options: '))

total = int(input('Please enter a number for options: '))

result = decisions.get_options_ratio(options, total)

print(decisions.get_faculty_rating(result))
