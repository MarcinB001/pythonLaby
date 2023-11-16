import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# a
dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])

# b
df = df.drop_duplicates()

# c
corr = df['age'].corr(df['limit_bal'])
print(f"Korelacja pomiędzy wiekiem a limitem kredytu: {corr}")

# d
df['bill_amt_X'] = df[['bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6']].sum(axis=1)

# e
oldest_clients = df.sort_values(by='age', ascending=False).head(10)

oldest_clients['education'] = oldest_clients[['education:0', 'education:1', 'education:2', 'education:3', 'education:4', 'education:5', 'education:6']].idxmax(axis=1).str.split(':').str[1].astype(int)

education_mapping = {
    1: 'graduate school',
    2: 'university',
    3: 'high school',
    4: 'others',
    5: 'unknown',
    6: 'unknown'
}

oldest_clients['education'] = oldest_clients['education'].map(education_mapping)

selected_columns = ['limit_bal', 'age', 'education', 'bill_amt_X']

table = oldest_clients[selected_columns]
print(table)

# f
fig, axes = plt.subplots(nrows=3, ncols=1)

axes[0].hist(df['limit_bal'], edgecolor='black', bins=20)
axes[0].set_title('Histogram limitu kredytu')
axes[0].set_xlabel('Limit kredytu')
axes[0].set_ylabel('Liczba klientów')

axes[1].hist(df['age'], edgecolor='black', bins=20)
axes[1].set_title('Histogram wieku')
axes[1].set_xlabel('Wiek')
axes[1].set_ylabel('Liczba klientów')

axes[2].scatter(df['age'], df['limit_bal'])
axes[2].set_title('Zależność limitu kredytu od wieku')
axes[2].set_xlabel('Wiek')
axes[2].set_ylabel('Limit kredytu')

fig.tight_layout()

plt.show()