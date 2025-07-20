from datetime import datetime

date_format = "%d-%m-%Y"
def get_last_project_id():

        with open("projects.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                return int(last_line.split(":")[0])
            else:
                return 0


def create_project (email):

    while True :
        title = input ("Enter the title of the project : ")
        if  not title:
            print("project title can't be empty")
            continue
        if  not title.replace(" ", "").isalpha():
            print("project title can have only letters")
            continue
        break
    while True :
        details = input ("Enter the details of the project : ")
        if  not details:
            print("project details can't be empty")
            continue
        if  not details.replace(" ", "").isalpha():
            print("project details can have only letters")
            continue
        break
    while True :
        total_target = input ("Enter the total target of the project : ")
        if  not total_target:
            print("project total target can't be empty")
            continue
        if  not total_target.isdigit():
            print("project total target can have only numbers")
            continue
        total_target = int(total_target)
        break
    while True:
        start_date = input("Enter the start date of the project (dd-mm-yyyy): ")
        end_date = input("Enter the end date of the project (dd-mm-yyyy): ")

        try:
            start = datetime.strptime(start_date, date_format)
            end = datetime.strptime(end_date, date_format)

            if end > start:
                break
            else:
                print("End date must be after the start date.")
                continue
        except ValueError:
            print("Invalid date format. Please use dd-mm-yyyy.")
            continue
    project_id = get_last_project_id() + 1
    with open("projects.txt", "a") as file:
        file.write(f"{project_id} : owner: {email}, title: {title}, details: {details}, total target: {total_target}, start date: {start_date}, end date: {end_date}\n")
    print("\n Project created successfully!")


def view_projects():

        with open("projects.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No projects found.")
                return
            print("\nAll Projects:\n")
            for line in lines:
                print(line.strip())


def edit_project(email):
    project_id = input("Enter project ID to edit: ").strip()
    updated_projects = []
    found = False

    with open("projects.txt", "r") as file:
        for line in file:
            if line.startswith(project_id) and f"owner: {email}" in line:
                print("Project found!")


                title = input("New title: ")
                details = input("New details: ")
                target = input("New total target: ")

                parts = line.strip().split(", ")
                new_line = f"{project_id} : owner: {email}, title: {title}, details: {details}, total target: {target}, {parts[-2]}, {parts[-1]}"
                updated_projects.append(new_line + "\n")
                found = True
            else:
                updated_projects.append(line)

    with open("projects.txt", "w") as file:
        file.writelines(updated_projects)

    print("Project updated!" if found else "Project not found or not yours.")





def delete_project(email):
    project_id = input("Enter the ID of the project you want to delete: ").strip()
    new_lines = []
    deleted = False

    with open("projects.txt", "r") as file:
        for line in file:
            if line.startswith(project_id) and f"owner: {email}" in line:
                deleted = True
            else:
                new_lines.append(line)

    with open("projects.txt", "w") as file:
        file.writelines(new_lines)

    if deleted:
        print("Your project has been deleted.")
    else:
        print("Couldn’t find a project with that ID under your account.")
