#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.xlim(0, 100)
plt.ylim(0, 30)
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 31, 5))
plt.hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
plt.show()
