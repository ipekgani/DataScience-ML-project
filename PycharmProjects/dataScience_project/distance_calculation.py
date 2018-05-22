import pandas as pd
from geopy.distance import vincenty

schools_df = pd.read_csv('Map_of_Schools.csv', header=0, index_col=None)
crimes_df = pd.read_csv('crimes_original_labels.csv', header=0, index_col=None)
crimes_df.rename(columns={'Unnamed: 0': 'Sample num'}, inplace=True)
# crimes_df = crimes_df.iloc[0:50,:]

mins = []
school_loc = []
i=0
for row in schools_df['Location 1']:
    tempStr2 = row
    tempStr2 = tempStr2[4:-1]
    sX, sY = tempStr2.split(',')
    sX = float(sX)
    sY = float(sY)
    school_loc.append((sX, sY))
    i=i+1

# creating an empty dataframe that has the same labels(collumn heads) as schools
nearestSchool=pd.DataFrame(columns=schools_df.columns)
for i in range(len(crimes_df)):
    cy = float(crimes_df.loc[i, 'X'])
    cx = float(crimes_df.loc[i, 'Y'])
    crime = (cx, cy)

    min = 100000000
    index = -1
    found = -1
    # searching nearest school for crime i
    for school in school_loc:
        index = index+1
        dist = vincenty(crime, school).miles
        if dist < min:
            min = dist
            found = index

    s = schools_df.loc[found, :]
    mins.append(min)
    print(min, s['Campus Name'])
    nearestSchool = nearestSchool.append(s, ignore_index=True)

min_df = pd.DataFrame(mins, columns=['Distance'])
res=pd.concat([crimes_df, nearestSchool, min_df],axis=1)
res = res.drop(['Campus Address', 'CDS Code', 'CCSF Entity', 'Lower Age', 'Upper Age', 'Grade Range', 'Category', 'County Name', 'Map Label', 'County FIPS', 'Location 1', 'X', 'Y'], axis=1)

schooltype = []
for i in range(len(res)):
    print(i)
    lowergrade = res.loc[i, 'Lower Grade']
    uppergrade = res.loc[i, 'Upper Grade']
    if uppergrade <= 0:
        schooltype.append('Pre-School')
    elif uppergrade <= 8:
        schooltype.append('Primary School')
    elif uppergrade <= 12:
        schooltype.append('High School')
    else:
        schooltype.append('College')

sch_df = pd.DataFrame(schooltype, columns=['School Type'])
newres=pd.concat([res, sch_df],axis=1)
newres = newres.drop(['Lower Grade', 'Upper Grade'], axis=1)
pd.DataFrame.to_csv(newres, 'crimesandschoolsjustincasewelosestuff_2.csv')

# type_df = pd.get_dummies(newres['School Type'])
# gnrltype_df = pd.get_dummies(newres['General Type'])
# newres = newres.drop(['School Type', 'General Type', 'Campus Name'], axis=1)
# newnewres = pd.concat([newres, type_df, gnrltype_df], axis=1)

pd.DataFrame.to_csv(newnewres, 'crimes_trainingset_2.csv')
print("end")
