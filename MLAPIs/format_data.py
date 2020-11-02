import pandas as pd
import re
from datetime import date, datetime
from sklearn.model_selection import train_test_split

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

data_frame = pd.read_csv('nba2k20-full.csv')
df1 = pd.DataFrame(data_frame, columns=['full_name', 'rating', 'position', 'b_day', 'salary', 'height', 'weight', 'team'])

df1['salary'] = [int(salary[1:]) for salary in df1['salary']]
df1['height'] = [float(height[6:]) for height in df1['height']]
df1['rating'] = [int(rating) for rating in df1['rating']]

final_weight = []
ctr = "kg"
pattern = "[" + ctr + "]"

for weight in df1['weight']:
    weight = weight[10:]
    new_weight = re.sub(pattern,"",weight)
    final_weight.append(float(new_weight[:-1]))

final_ages = []
for age in df1['b_day']:
    datetime_obj = datetime.strptime(age, '%m/%d/%y').date()
    age = calculate_age(datetime_obj)
    final_ages.append(int(age))

del df1['b_day']
df1['weight'] = final_weight
df1['age'] = final_ages
print(df1)

