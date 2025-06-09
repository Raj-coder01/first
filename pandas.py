import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}


df = pd.DataFrame(data)


print(df)


average_age = df['Age'].mean()
print("Average age:", average_age)
