#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
get_ipython().run_line_magic('matplotlib', 'inline')
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv('Newversion.csv')
df.head()


# In[3]:


df.describe()


# In[4]:


df.isnull().sum().sum()


# In[5]:


df.info()


# In[6]:


# Find columns with NaN values
columns_with_nan = df.columns[df.isnull().any()].tolist()

# Find rows with NaN values in the entire DataFrame
rows_with_nan = df[df.isnull().any(axis=1)]

# Print columns with NaN values
print("Columns with NaN values:")
print(columns_with_nan)
# Print rows with NaN values
if not rows_with_nan.empty:
    print("\nRows with NaN values:")
    print(rows_with_nan)
else:
    print("\nNo rows with NaN values found.")


# In[7]:


import pandas as pd

# Drop rows with NaN values
df_cleaned = df.dropna()
df_cleaned.to_csv('cleaned_dataset.csv', index=False)
df1=pd.read_csv('cleaned_dataset.csv')


# In[8]:


df1.isnull().sum().sum()


# In[9]:


for i in df1.columns:
    print(i)
    print(df1[i].value_counts())


# In[10]:


df1.info()


# In[11]:


import pandas as pd

# List of column names to remove
columns_to_remove = ['Timestamp', 'Bwd PSH Flags', 'Fwd PSH Flags','Fwd URG Flags','Bwd URG Flags','FIN Flag Cnt','CWE Flag Count','Fwd Byts/b Avg','Fwd Blk Rate Avg','Bwd Byts/b Avg','Bwd Pkts/b Avg','Bwd Blk Rate Avg']  # Replace with your actual column names

# Remove the specified columns
df1 = df1.drop(columns=columns_to_remove)
df1.info()
# Now 'df1' contains the dataset with the specified columns removed


# In[12]:


df1.plot(kind='box',subplots=True,layout=(23,3),figsize=(20,40))
plt.show()


# In[13]:


df1.plot(kind='box', subplots=False, figsize=(20,40))


# In[14]:


from sklearn.preprocessing import LabelEncoder

# Identify categorical columns in the dataset
categorical_columns = df1.select_dtypes(include=['object']).columns

# Create a LabelEncoder instance
label_encoder = LabelEncoder()

# Apply LabelEncoder to each categorical column
for column in categorical_columns:
    df1[column] = label_encoder.fit_transform(df1[column])

# Print the dataset with encoded categorical values
df1.to_csv('stage1.csv',index=False)
df2=pd.read_csv('stage1.csv')
df2['Label'].value_counts()


# In[15]:


df2.isnull().sum().sum()


# In[16]:


df2.info()


# In[17]:


df2['Label'] = df2['Label'].apply(lambda x: 1 if x != 0 else x)
df2.isnull().sum().sum()


# In[18]:


df2.head()


# In[19]:


df2=pd.read_csv('stage1.csv')
# List of feature names  to be included in the new dataset
selected_features = ['Bwd Pkt Len Std' ,  'PSH Flag Cnt' , 'Fwd Seg Size Min' ,  'Bwd Pkt Len Min' , 'ACK Flag Cnt' , 'Fwd IAT Std' , 'Init Fwd Win Byts', 'Flow IAT Max'  ,   'Bwd Pkts/s' ,  'Bwd IAT Tot'   , 'URG Flag Cnt' ,  'Pkt Len Min' , 'Label']

# Create a new dataset with selected features
df2_new = df2[selected_features]
df2_new['Label'] = df2['Label'].apply(lambda x: 1 if x != 0 else x)

# Save the new dataset to a CSV file
df2_new.to_csv('new_dataset.csv', index=False)

# Read the new dataset to check if it was created successfully
df2_new1 = pd.read_csv('new_dataset.csv')


# In[20]:


df2_new1['Label'].value_counts()


# In[21]:


df2_new1.info()


# In[22]:


from sklearn.preprocessing import MinMaxScaler
import numpy as np
# Load your dataset from a CSV file
file_path = 'new_dataset.csv'

# Load dataset
df = pd.read_csv(file_path)

# Check for constant columns and remove them
non_constant_columns = df.columns[df.nunique() > 1]
df = df[non_constant_columns]

# Check for infinite values and replace them with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Drop rows with NaN values
df.dropna(inplace=True)

# Min-Max scaling for numeric columns (int64 and float64)
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

if numeric_columns:
    scaler = MinMaxScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# Display the scaled dataset
df.to_csv('df.csv',index=False)
df3=pd.read_csv('df.csv')


# In[23]:


df3.info()


# In[24]:


df3['Label'].value_counts()


# In[25]:


df3['Label'] = df3['Label'].apply(lambda x: 1 if x > 0 else 0)
df3['Label'].value_counts()


# In[26]:


from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split

X = df3.drop('Label', axis=1)  # Features
y = df3['Label']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

mutual_info = mutual_info_classif(X_train, y_train)
mutual_info = pd.Series(mutual_info)
mutual_info.index = X_train.columns
mutual_info.sort_values(ascending=False)


# In[27]:


mutual_info.sort_values(ascending=False).plot.bar(figsize=(20, 8));


# In[28]:


# from sklearn.feature_selection import SelectKBest
# sel_five_cols = SelectKBest(mutual_info_classif, k=20)
# sel_five_cols.fit(X_train, y_train)
# X_train.columns[sel_five_cols.get_support()]


# In[29]:


# col=['Dst Port', 'FlowDuration', 'Fwd Pkt Len Mean', 'Bwd Pkt Len Mean',
#        'Flow Pkts/s', 'Flow IAT Mean', 'Flow IAT Max', 'Fwd Header Len',
#        'Fwd Pkts/s', 'Pkt Len Max']
# X_train=X_train[col]
# X_test=X_test[col]


# In[30]:


plt.figure(figsize=(12,10))
p=sns.heatmap(X_train.corr(), annot=True,cmap ='RdYlGn')


# In[31]:


from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score
df3.replace([np.inf, -np.inf], 1e15, inplace=True)

X = df3.drop('Label', axis=1)  # Features
y = df3['Label']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Initialize the Gaussian Naive Bayes model with regularization (var_smoothing)
gnb = GaussianNB(var_smoothing=1e-9)  # You can experiment with different values

# Train the model on the training set
gnb.fit(X_train, y_train)

# Make predictions on the training set
y_train_pred = gnb.predict(X_train)

# Make predictions on the test set
y_test_pred = gnb.predict(X_test)

# Calculate accuracy and precision on both sets
accuracy_train = accuracy_score(y_train, y_train_pred)
precision_train = precision_score(y_train, y_train_pred, average='weighted')

accuracy_test = accuracy_score(y_test, y_test_pred)
precision_test = precision_score(y_test, y_test_pred, average='weighted')

# Print accuracy and precision on both sets
print(f'Training Accuracy: {accuracy_train:.5f}, Training Precision: {precision_train:.5f}')
print(f'Testing Accuracy: {accuracy_test:.5f}, Testing Precision: {precision_test:.5f}')

# Check for overfitting
if accuracy_train - accuracy_test > 0.05 or precision_train - precision_test > 0.05:
    print("The model might be overfitting.")
else:
    print("The model does not seem to be overfitting.")


# In[ ]:





# In[32]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score

X = df3.drop('Label', axis=1)  # Features
y = df3['Label']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Initialize the Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)  # You can adjust hyperparameters

# Train the model on the training set
rf_classifier.fit(X_train, y_train)

# Make predictions on the training set
y_train_pred = rf_classifier.predict(X_train)

# Make predictions on the test set
y_test_pred = rf_classifier.predict(X_test)

# Calculate accuracy and precision on both sets
accuracy_train = accuracy_score(y_train, y_train_pred)
precision_train = precision_score(y_train, y_train_pred, average='weighted')

accuracy_test = accuracy_score(y_test, y_test_pred)
precision_test = precision_score(y_test, y_test_pred, average='weighted')

# Print accuracy and precision on both sets
print(f'Training Accuracy: {accuracy_train:.5f}, Training Precision: {precision_train:.5f}')
print(f'Testing Accuracy: {accuracy_test:.5f}, Testing Precision: {precision_test:.5f}')

# Check for overfitting
if accuracy_train - accuracy_test > 0.05 or precision_train - precision_test > 0.05:
    print("The model might be overfitting.")
else:
    print("The model does not seem to be overfitting.")


# In[33]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix


X = df3.drop(columns=['Label'])
y = df3['Label']

# Convert categorical labels to integers if needed
# Example: y = pd.factorize(y)[0]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN Classifier
knn_model = KNeighborsClassifier(n_neighbors=20)  # You can adjust the number of neighbors as needed

# Train the model on the training set
knn_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy:.5f}")
print(f"Precision: {precision:.5f}")

# # Check for overfitting
# if accuracy_train - accuracy_test > 0.05 or precision_train - precision_test > 0.05:
#     print("The model might be overfitting.")
# else:
#     print("The model does not seem to be overfitting.")


# In[34]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score

X = df3.drop('Label', axis=1)  # Features
y = df3['Label']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Initialize the Decision Tree classifier
dt_classifier = DecisionTreeClassifier(random_state=42)  # You can adjust hyperparameters

# Train the model on the training set
dt_classifier.fit(X_train, y_train)

# Make predictions on the training set
y_train_pred = dt_classifier.predict(X_train)

# Make predictions on the test set
y_test_pred = dt_classifier.predict(X_test)

# Calculate accuracy and precision on both sets
accuracy_train = accuracy_score(y_train, y_train_pred)
precision_train = precision_score(y_train, y_train_pred, average='weighted')

accuracy_test = accuracy_score(y_test, y_test_pred)
precision_test = precision_score(y_test, y_test_pred, average='weighted')

# Print accuracy and precision on both sets
print(f'Training Accuracy: {accuracy_train:.5f}, Training Precision: {precision_train:.5f}')
print(f'Testing Accuracy: {accuracy_test:.5f}, Testing Precision: {precision_test:.5f}')

# Check for overfitting
if accuracy_train - accuracy_test > 0.05 or precision_train - precision_test > 0.05:
    print("The model might be overfitting.")
else:
    print("The model does not seem to be overfitting.")


# In[36]:


# we'll initialize each model and store it by name in a dictionary
model = {}

# Logistic Regression
from sklearn.linear_model import LogisticRegression
model['Logistic Regression'] = LogisticRegression()


# Decision Trees
from sklearn.tree import DecisionTreeClassifier
model['Decision Trees'] = DecisionTreeClassifier(max_depth=3)

# Random Forest
from sklearn.ensemble import RandomForestClassifier
model['Random Forest'] = RandomForestClassifier()

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
model['Naive Bayes'] = GaussianNB()

from sklearn.neighbors import KNeighborsClassifier
model['K-Nearest Neighbor'] = KNeighborsClassifier(n_neighbors=20)


# In[38]:


from sklearn.metrics import accuracy_score, precision_score, recall_score

accuracy, precision, recall = {}, {}, {}

for key in model.keys():

    # Fit the classifier
    model[key].fit(X_train, y_train)

    # Make predictions
    predictions = model[key].predict(X_test)

    # Calculate metrics
    accuracy[key] = accuracy_score(predictions, y_test)
    precision[key] = precision_score(predictions, y_test)
    recall[key] = recall_score(predictions, y_test)


# In[40]:


df_model = pd.DataFrame(index=model.keys(), columns=['Accuracy', 'Precision', 'Recall'])
df_model['Accuracy'] = accuracy.values()
df_model['Precision'] = precision.values()
df_model['Recall'] = recall.values()

df_model


# In[41]:


ax = df_model.plot.barh()
ax.legend(
    ncol=len(model.keys()), 
    bbox_to_anchor=(0, 1), 
    loc='lower left', 
    prop={'size': 14}
)
plt.tight_layout()


# In[42]:


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()


# In[43]:


model.fit(X_train, y_train)


# In[44]:


#print accuracy
print("Accuracy: ",model.score(X_test,y_test) * 100)


# In[45]:


#save the model
import pickle
filename = 'savemodel.sav'
pickle.dump(model, open(filename, 'wb'))


# In[46]:


X_test.head()


# In[47]:


load_model = pickle.load(open(filename,'rb'))


# In[48]:


load_model.predict([[0.214406, 1.0, 0.454545, 0.0, 0.0, 0.004561, 0.125015, 7.942742e-03, 2.449596e-06, 0.011336, 0.0, 0.0]]) 


# In[ ]:




