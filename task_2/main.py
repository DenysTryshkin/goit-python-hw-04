from pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for line in file:
                id, name, age = line.strip().split(",")
                cats_info.append({"id" :id, "name" :name, "age": age})
        return cats_info

    except Exception as e:
        print(f"Error: {e}")
        return []


cats_info = get_cats_info("/Users/denys/Desktop/python/goit-python-hw-04/task_2/cats_file.txt")
print(cats_info)