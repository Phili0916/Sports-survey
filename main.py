survey = {}
response = None

while response != "":
  response = input('What is your favorite baseball team? \n')
  if response != "":
    if response in survey:
      survey[response] = survey[response] + 1
    else:
      survey[response] = 1

print('Favorite baseball teams vote totals are : ')
for team, scores in survey.items():
  print('-', team, ':', scores)
