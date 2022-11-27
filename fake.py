
import pandas as pd

from faker import Faker

 

fake = Faker('de_DE')

df = pd.DataFrame(dtype=str)

names = []

addresses = []

add = []

plz = []

 

pd.set_option('display.max_columns', 4)

 

for _ in range(20):

    names.append(fake.name())

    addresses.append(fake.address())

   

for i in addresses:

    x = i.splitlines()

    add.append(x[0])

    plz.append(x[1])

           

df['Names'] = names

df['Addresses'] = add

df['PLZ City'] = plz

print(df)

 

df.to_csv('output.csv')
