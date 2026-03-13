print("===== LIFE DECISION ENGINE =====")

age = int(input("Enter your age: "))
salary = int(input("Enter your monthly salary: "))
experience = float(input("Enter years of experience: "))
skill_level = input("Skill Level (beginner/intermediate/advanced): ").lower()
health = input("Health Status (poor/average/good): ").lower()
savings = int(input("Enter total savings: "))
goal = input("Primary Goal (job/business/study/freedom): ").lower()
stress = input("Stress Level (low/medium/high): ").lower()
city_type = input("City Type (metro/tier2/rural): ").lower()

print("\n===== ANALYSIS RESULT =====")

# AGE BASED LOGIC
if age < 18:
    print("You are too young for financial independence.")
    if skill_level == "advanced":
        print("Gifted. Start freelancing early.")
    elif skill_level == "intermediate":
        print("Focus on sharpening core skills.")
    else:
        print("Explore different fields.")
else:
    if age >= 18 and age <= 25:
        print("Early career stage.")
        if experience < 1:
            print("You need real-world exposure.")
            if skill_level == "beginner":
                print("Join internship immediately.")
            elif skill_level == "intermediate":
                print("Apply for entry-level roles.")
            else:
                print("You are underpaid probably.")
        elif experience >= 1 and experience < 3:
            print("Growth stage.")
            if salary < 30000:
                print("Underpaid. Switch job.")
            elif salary >= 30000 and salary < 70000:
                print("Average salary bracket.")
            else:
                print("High performer early.")
        else:
            print("Unusual experience for this age.")
    elif age > 25 and age <= 35:
        print("Prime career building stage.")
        if savings < 100000:
            print("Financial risk zone.")
            if salary < 50000:
                print("Increase income urgently.")
            else:
                print("Control lifestyle inflation.")
        else:
            print("Stable financial foundation.")
            if goal == "business":
                print("Good time to take calculated risk.")
            elif goal == "job":
                print("Climb leadership ladder.")
            elif goal == "study":
                print("Higher education ROI must be calculated.")
            else:
                print("Plan early retirement strategy.")
    else:
        print("Late career stage.")
        if savings < 500000:
            print("Retirement risk detected.")
        else:
            print("You are financially ahead.")

# HEALTH BRANCHING
if health == "poor":
    print("Health is priority.")
    if stress == "high":
        print("Burnout zone.")
    elif stress == "medium":
        print("Moderate recovery needed.")
    else:
        print("Low stress but poor health — check lifestyle.")
elif health == "average":
    print("Maintain discipline.")
    if salary > 100000:
        print("Invest in fitness coach.")
    else:
        print("Adopt structured routine.")
else:
    print("Health advantage detected.")
    if goal == "business":
        print("Energy supports entrepreneurship.")
    elif goal == "study":
        print("Strong focus potential.")
    else:
        print("Use this edge wisely.")

# SAVINGS LOGIC
if savings < 10000:
    print("Emergency fund missing.")
elif savings >= 10000 and savings < 100000:
    print("Basic cushion present.")
elif savings >= 100000 and savings < 500000:
    print("Mid-level security.")
else:
    print("High security level.")

# SALARY DEEP BRANCHING
if salary < 20000:
    print("Critical income zone.")
    if city_type == "metro":
        print("Survival mode.")
    elif city_type == "tier2":
        print("Barely manageable.")
    else:
        print("Low cost survival possible.")
elif salary >= 20000 and salary < 60000:
    print("Lower middle bracket.")
    if experience < 2:
        print("Income aligned with experience.")
    else:
        print("Stagnation risk.")
elif salary >= 60000 and salary < 150000:
    print("Upper middle bracket.")
    if skill_level == "advanced":
        print("Justified income.")
    else:
        print("Upgrade skills for next jump.")
else:
    print("High income bracket.")
    if savings < salary * 3:
        print("Spending too much.")
    else:
        print("Good wealth building pattern.")

# STRESS TREE
if stress == "high":
    if goal == "freedom":
        print("You crave independence.")
    elif goal == "job":
        print("Corporate burnout likely.")
    else:
        print("Re-evaluate commitments.")
elif stress == "medium":
    print("Manageable pressure.")
else:
    print("Stable mental zone.")

# FINAL SUMMARY
if health == "good" and savings > 100000 and skill_level == "advanced":
    print("\nVerdict: High Growth Individual.")
elif stress == "high" and savings < 50000:
    print("\nVerdict: Immediate Reset Required.")
elif goal == "business" and savings > 200000:
    print("\nVerdict: Launch Plan Possible.")
elif goal == "study" and age < 30:
    print("\nVerdict: Good Time for Higher Education.")
else:
    print("\nVerdict: Optimize current position.")

print("\n===== END OF ANALYSIS =====")