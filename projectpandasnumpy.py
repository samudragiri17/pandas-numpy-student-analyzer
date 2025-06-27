import pandas as pd 
import numpy as np

data ={
    "Student ID": [101,102,103,104],
    "Name": ['Ramesh','Sam','Ananya','Sneha'],
    "Maths":[89,91,88,78],
    "Physics": [76,70,87,84],
    "Chemistry": [91,90,88,82],
    "Gender": ['Male','Male','Female','Female'],
    "Age" : [22,23,23,21]
}
df = pd.DataFrame(data)
print(df)

#Explore Data
print(df.head())
print(df.info())
print(df.describe())

#Calculate Total & Average Marks
df["Total"] = df[["Maths","Physics","Chemistry"]].sum(axis=1) #horizontal
df["Average"] = df["Total"]/3
print(df["Total"])
print(df["Average"])

#Classifying Students by Grade
def grade(avg):
    if avg >= 90:
        return "Outstanding"
    elif avg >= 75:
        return "Good"
    elif avg >= 60:
        return "Average"
    else:
        return "Needs Improvement"

df["Grade"] = df["Average"].apply(grade)


#Topper in Each Subject
for subject in ["Maths", "Physics", "Chemistry"]:
    top_student = df[df[subject] == df[subject].max()]
    print(f"Topper in {subject}:")
    print(top_student[["Name", subject]])

#Gender-Based Average Comparison
df.groupby("Gender")[["Maths", "Physics", "Chemistry", "Average"]].mean()

#Use NumPy to Flag Top Student
df["High_Performer"] = np.where(df["Average"] >= 85, "Yes", "No")
print(df["High_Performer"])
