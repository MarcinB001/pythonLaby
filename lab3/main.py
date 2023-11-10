import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

# a
dataset = load_dataset("imodels/credit-card")
df = pd.DataFrame(dataset['train'])

# b
df = df.drop_duplicates()

X = df.drop(columns=['default.payment.next.month'])
y = df['default.payment.next.month'].values

# c
correlation = df['age'].corr(df['limit_bal'])
print(f"Korelacja pomiędzy wiekiem a limitem kredytu: {correlation}")

# d
df['total_bill_amt'] = df[['bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6']].sum(axis=1)

# e
oldest_clients = df.sort_values(by='age', ascending=False).head(10)

selected_columns = ['limit_bal', 'age', 'education:0', 'education:1', 'education:2', 'total_bill_amt']

table = oldest_clients[selected_columns]
print(table)


# f
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

axes[0, 0].hist(df['limit_bal'], bins=20, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Histogram Limitu Kredytu')
axes[0, 0].set_xlabel('Limit Kredytu')
axes[0, 0].set_ylabel('Liczba Klientów')

axes[0, 1].hist(df['age'], bins=20, color='lightcoral', edgecolor='black')
axes[0, 1].set_title('Histogram Wieku')
axes[0, 1].set_xlabel('Wiek')
axes[0, 1].set_ylabel('Liczba Klientów')

axes[1, 0].scatter(df['age'], df['limit_bal'], color='green', alpha=0.5)
axes[1, 0].set_title('Zależność Limitu Kredytu od Wieku')
axes[1, 0].set_xlabel('Wiek')
axes[1, 0].set_ylabel('Limit Kredytu')

fig.tight_layout()

plt.show()