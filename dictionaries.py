# Merge n Dictionaries (Python 2.7 compatible)

def cdict(*args):
    z={}
    for arg in args:
        if isinstance(arg, dict):
            z.update(arg)
    return z
  
a = { 'A': 'my', 'B': 'aunt'}
b = { 'B': 'horse' } # 'horse' will overwrite 'aunt' because of .update
c = { 'C': 'is' }
d = { 'D': 'very' }
e = { 'E': 'old' }

f = cdict(a,b,c,d,e)
Out[]: {'A': 'my', 'B': 'horse', 'C': 'is', 'D': 'very', 'E': 'old'}


# Dictionary of (List of Lists)

Import pandas as pd
# https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease

features={  'age': ['Age','numerical',['years']],
             'bp': ['Blood Pressure', 'numerical',['mm/Hg']],
             'sg': ['Specific Gravity', 'nominal',  [1.005,1.010,1.015,1.020,1.025]],
             'al': ['Albumin', 'nominal',  [0,1,2,3,4,5]],
             'su': ['Sugar', 'nominal',  [0,1,2,3,4,5]],
            'rbc': ['Red Blood Cells', 'nominal',  ['normal','abnormal']],
             'pc': ['Pus Cell', 'nominal',  ['normal','abnormal']],
            'pcc': ['Pus Cell clumps', 'nominal',  ['present','notpresent']],
             'ba': ['Bacteria', 'nominal',  ['present','notpresent']],
            'bgr': ['Blood Glucose Random', 'numerical',['in mgs/dl']],
             'bu': ['Blood Urea', 'numerical',['in mgs/dl']],
             'sc': ['Serum Creatinine','numerical',['in mgs/dl']],
            'sod': ['Sodium', 'numerical',['mEq/L']],
            'pot': ['Potassium', 'numerical',['mEq/L']],
           'hemo': ['Hemoglobin', 'numerical',['gms']],
            'pcv': ['Packed Cell Volume', 'numerical',['Pct.']],
             'wc': ['White Blood Cell Count', 'numerical',['cells/cumm']],
             'rc': ['Red Blood Cell Count', 'numerical',['millions/cmm']], 
            'htn': ['Hypertension', 'nominal',  ['yes','no']],
             'dm': ['Diabetes Mellitus', 'nominal',  ['yes','no']],
            'cad': ['Coronary Artery Disease', 'nominal',  ['yes','no']],
          'appet': ['Appetite', 'nominal',  ['good','poor']],
             'pe': ['Pedal Edema', 'nominal',  ['yes','no']],
            'ane': ['Anemia', 'nominal',  ['yes','no']],
 'classification': ['Class', 'nominal',  ['ckd','notckd']]
          }
features.keys()
columns=['Description', 'Data Type', 'Unit']

# Different ways of importing and printing
print pd.DataFrame.from_dict(features).set_index([columns]).T.to_string()
print pd.DataFrame.from_dict(features, orient='index').rename(columns= {0: 'Des', 1: 'type', 2: 'unit'}).to_string()
print pd.DataFrame(list(features.iteritems()),columns=['Key','List of Lists']).to_string()
print pd.DataFrame(features,index = columns).T.to_string()

# Create a List of Lists from Dictionary of (List of Lists)
LoL_rows, LoL = [], []
for i in features:
    LoL_rows = [i] # Inserts features.keys() as the first column
    for j in range(len(features[each])):
        LoL_rows.append(features[i][j])
    LoL.append(LoL_rows) 
columns.insert(0,'Short') # Insert Key 
print pd.DataFrame(LoL,columns=columns).sort_values([columns[2],columns[0]]).to_string()


# 1 What does the docs say about these three variables: bgr, rc, and wc?
print features['bgr'] # ['Blood Glucose Random', 'numerical', ['in mgs/dl']]
print features['rc'] # ['Red Blood Cell Count', 'numerical', ['millions/cmm']]
print features['wc'] # ['White Blood Cell Count', 'numerical', ['cells/cumm']]

# 2 Load up kidney_disease.csv and drop all rows that have any nans.
tedit(path + 'Module4/Datasets/kidney_disease.csv') # Open with TextEdit
df = pd.read_csv(path + 'Module4/Datasets/kidney_disease.csv', index_col=0)
df = df.dropna(axis=0)  # remove any row with nans

# 3 Select only the following columns: bgr, rc, and wc. 
brw = df[['bgr','rc','wc']].reset_index(drop=True)
brw.dtypes


prw = df[['pcv','rc','wc']]
for each in range(len(prw)): # Cheack if each row contains numeric values
        print  map(lambda x: isinstance(x, (int, float, long)), prw.iloc[each,:])
        
# 4 Do a check of your dataframe's dtypes
df.dtypes

for each in df.columns: # Match dtypes with doc
    print each,'\t', df[each].dtypes, features[each][1:3]
    

df.pcv = pd.to_numeric(df.pcv, downcast='float', errors='coerce')
df.rc = pd.to_numeric(df.rc, downcast='float', errors='coerce')
df.wc = pd.to_numeric(df.wc, downcast='float', errors='coerce')

prw = df[['pcv','rc','wc']].reset_index(drop=True)
for each in range(len(prw)): # Cheack if each row contains numeric values
        print  map(lambda x: isinstance(x, (int, float, long)), prw.iloc[each,:])
for each in range(len(prw)): # Cheack if each row contains strings
        print  map(lambda x: isinstance(x, str), prw.iloc[each,:])
prw= prw.applymap(float) # Convert entire DataFrame to float
brw = df[['bgr','rc','wc']].reset_index(drop=True)

# 5 Print the variance of your dataset, as well as a .describe() printout.
brw = df[['bgr','rc','wc']].reset_index(drop=True)
for each in brw.columns:
    print each, brw[each].var() # Prints variance
brw.describe()
brw.dtypes

# 6 Reduce your dataset to two principal components by run it through PCA,

df = pd.read_csv(path + 'Module4/Datasets/kidney_disease.csv', index_col=0)
df = df.dropna(axis=0)  # remove any row with nans


df.pcv = pd.to_numeric(df.pcv, downcast='float', errors='coerce')
df.rc = pd.to_numeric(df.rc, downcast='float', errors='coerce')
df.wc = pd.to_numeric(df.wc, downcast='float', errors='coerce')

catagorical, ordinal, nominal = [],[], []
for each in df.columns: # Match dtypes with doc
    if features[each][1]=='nominal':
        catagorical.append(each) # Append categorical columns
for each in catagorical:
    if len(features[each][2]) > 2:      
        ordinal.append(each) # Append ordinal columns
    else:    
        nominal.append(each) # Append nominal columns
for each in ordinal:
    df[each] = df[each].astype('category', ordered=True) # categories=features[each][2]).cat.codes
#    print features[each][2]    
# print catagorical; print nominal; print ordinal
# df.select_dtypes(include=['object']).head()


df = pd.get_dummies(df,columns=nominal)
df.dtypes

labels = ['red' if i=='ckd' else 'green' for i in df.classification]

for each in ordinal:
    print df[each].head(5)
    df[each].cat.codes
    dict( enumerate(df[each].cat.categories) )


# How to sort a Dictionary
links_key = {'Z is first': 'Zebra', 'A is second': 'Amazing', 'B is third': 'Baboon', 'Y is fourth': 'Yankees'}
printo = {'Z is first': 1, 'A is second': 2, 'B is third': 3, 'Y is fourth': 4}

In[]:  a = sorted(links_key, key=printo.__getitem__)
In[]:  a
Out[]: ['Z is first', 'A is second', 'B is third', 'Y is fourth']

In:    b = [links_key[i] for i in sorted(links_key, key=printo.__getitem__)]
In[]:  b
Out[]: ['Zebra', 'Amazing', 'Baboon', 'Yankees']

In[]:  zip(a,b)
Out[]: 
[('Z is first', 'Zebra'),
 ('A is second', 'Amazing'),
 ('B is third', 'Baboon'),
 ('Y is fourth', 'Yankees')]
