import pandas as pd
import matplotlib.pyplot as plt

# Sample finance data
data = {
    "Category": ["Food", "Transport", "Shopping", "Bills", "Salary"],
    "Amount": [-500, -300, -800, -1000, 5000]
}

df = pd.DataFrame(data)

# Display data
print("💰 Personal Finance Tracker")
print(df)

# Calculate totals
income = df[df["Amount"] > 0]["Amount"].sum()
expenses = abs(df[df["Amount"] < 0]["Amount"].sum())
balance = income - expenses

print("\nTotal Income:", income)
print("Total Expenses:", expenses)
print("Balance:", balance)

# Chart
df.plot(
    x="Category",
    y="Amount",
    kind="bar",
    title="Income and Expenses"
)

plt.ylabel("Amount")
plt.show()

df = pd.DataFrame(data)