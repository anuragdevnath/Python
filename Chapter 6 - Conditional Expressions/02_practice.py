 # Taking marks input for 3 subjects (out of 100)
num1 = int(input("Enter your marks out of 100 in subject 1: "))
num2 = int(input("Enter your marks out of 100 in subject 2: "))
num3 = int(input("Enter your marks out of 100 in subject 3: "))

# Calculate overall percentage
percentage = ((num1 + num2 + num3) / 300) * 100

# Flag to track if any subject is below 33%
individual = 1  # 1 = passed in all subjects, 0 = failed in at least one

# Check if any subject has marks less than 33
if num1 < 33:
    individual = 0
if num2 < 33:
    individual = 0
if num3 < 33:
    individual = 0

# Final result based on conditions
if individual == 0 and percentage < 33:
    print("❌ Failed: Less than 33% overall and failed in one or more subjects.")
elif individual == 0 and percentage >= 33:
    print("⚠️ Passed overall, but failed in one or more subjects individually.")
else:
    print("✅ Passed: All subjects cleared and percentage is sufficient.")
