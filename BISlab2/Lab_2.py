    # =========================
# LAB 2: LINEAR REGRESSION
# Predict Profit and Transactions based on Sales
# =========================

# Import required libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load Data
# Replace the file path with your local path or read directly if in same directory
file_path = r'C:\Users\Banana\Documents\BIS Lab Report\BIS Lab 2\Lab_2_Data.xlsx'
df = pd.read_excel(file_path, sheet_name='Lab_2_Data')

# Display initial data (optional)
print(df.head())

# 2. Prepare Data
# Separate rows with available Profit values for training
profit_train = df[df['Profit'].notnull()]
X_profit = profit_train[['Sales']].values
y_profit = profit_train['Profit'].values

# Separate rows with available Transactions values for training
transactions_train = df[df['Transactions'].notnull()]
X_trans = transactions_train[['Sales']].values
y_trans = transactions_train['Transactions'].values

# 3. Train Linear Regression Models

# Model to predict Profit based on Sales
profit_model = LinearRegression()
profit_model.fit(X_profit, y_profit)

# Model to predict Transactions based on Sales
transactions_model = LinearRegression()
transactions_model.fit(X_trans, y_trans)

# 4. Make Predictions

# Predict missing Profit
missing_profit = df[df['Profit'].isnull()]
predicted_profit = profit_model.predict(missing_profit[['Sales']].values)

# Fill predicted Profit into dataframe
df.loc[df['Profit'].isnull(), 'Profit'] = predicted_profit

# Predict missing Transactions
missing_trans = df[df['Transactions'].isnull()]
predicted_trans = transactions_model.predict(missing_trans[['Sales']].values)

# Fill predicted Transactions into dataframe
df.loc[df['Transactions'].isnull(), 'Transactions'] = predicted_trans

# 5. Visualize Results

plt.figure(figsize=(14,6))

# Plot for Profit
plt.subplot(1,2,1)
plt.scatter(X_profit, y_profit, color='blue', label='Actual Profit')
plt.scatter(missing_profit['Sales'], predicted_profit, color='red', label='Predicted Profit')
for i, txt in enumerate(predicted_profit):
    plt.annotate(f'{txt:.1f}', (missing_profit['Sales'].values[i], predicted_profit[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Actual vs Predicted Profit')
plt.legend()

# Plot for Transactions
plt.subplot(1,2,2)
plt.scatter(X_trans, y_trans, color='green', label='Actual Transactions')
plt.scatter(missing_trans['Sales'], predicted_trans, color='orange', label='Predicted Transactions')
for i, txt in enumerate(predicted_trans):
    plt.annotate(f'{txt:.1f}', (missing_trans['Sales'].values[i], predicted_trans[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('Sales')
plt.ylabel('Transactions')
plt.title('Actual vs Predicted Transactions')
plt.legend()

plt.tight_layout()
plt.show()

# 6. Display updated dataframe with predictions
print(df)

# 7. Optional: Save updated data to Excel for your lab report
# df.to_excel('Lab_2_Data_with_Predictions.xlsx', index=False)
