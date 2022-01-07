# Create a program using maths and f-Strings that tells us how many
# days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with
# our time left in this format: You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly,
# even the positions of the commas and full stops.

age = input('What is your current age? ')
years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f'You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.'
print(message)
