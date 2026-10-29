
import matplotlib.pyplot as plt

salary = [20000, 25000, 50000, 60000, 18000, 45000]
years = [1, 2, 6, 8, 1, 5]
attrition = [1, 1, 0, 0, 1, 0]

print("HR ANALYTICS REPORT")
print("-------------------")

for i in range(len(salary)):
    status = "Yes" if attrition[i] == 1 else "No"
    print("Employee", i+1, "Salary:", salary[i],
          "Years:", years[i], "Attrition:", status)

print("\nTotal Employees:", len(salary))
print("Employees Left:", sum(attrition))
print("Attrition Rate:", sum(attrition)/len(attrition)*100, "%")

plt.bar(["Left", "Stayed"], [sum(attrition),
        len(attrition)-sum(attrition)])
plt.title("Employee Attrition Analysis")
plt.ylabel("Employees")
plt.show()
