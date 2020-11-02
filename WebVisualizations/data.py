import pandas as pd

# Read the csv file in
df = pd.read_csv("/Users/caitlindonovan/Desktop/ColumbiaBootcamp/Homework/Web-Design-Challenge/WebVisualizations/Resources/cities2.csv")

# Save to file
df.to_html("data.html", index=False)

# Assign to string
table = df.to_html()
print(table)