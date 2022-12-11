f=open("titanic.csv")
'''
for line in f:
    print(line.strip())
    # Strrip  удаляет пробелы
    print(line.count(","))
'''

''' ####### Проверить на количество запятых в строке при итерировав список
for line in f:
    count=line.count(",")
    if count!=12:
        print(count)
'''
line_number=0
female_count=0
male_count=0

female_count_survived=0
male_count_survived=0

for line in f:
    line_number+=1
    if line_number==1:
        continue
    count=line.count(",")
    line=line.strip()
    fields=line.split(",")
    sex=fields[5]
    survived=int(fields[1])
    print(fields)
    print(sex,survived)
    if sex=="male":
        male_count+=1
        if survived==1:
            male_count_survived+=1
    else:
        female_count+=1
        if survived==1:
            female_count_survived+=1

print(f"male: {male_count}, male_count_survived: {male_count_survived},"
      f" percentage: {round(male_count_survived/male_count*100,2)}")
print(f"female: {female_count}, female_count_survived: {female_count_survived},"
      f" percentage: {round(female_count_survived/female_count*100,2)}")
