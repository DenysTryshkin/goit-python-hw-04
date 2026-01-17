from pathlib import Path

def total_salary(path):
    total = 0
    developers_count = 0

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for line in file:
                _, salary = line.strip().split(",")
                total += int(salary)
                developers_count += 1

        if developers_count == 0:
            return 0, 0
                
        average_salary = int(total / developers_count)
        return total, average_salary

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return 0, 0
    
total, average = total_salary("/Users/denys/goit-python-hw-04/task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


