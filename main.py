from auth import register, login
from project import create_project,view_projects, edit_project, delete_project
while True:
    choice = input("\nDo you want to register or login? (r/l): ").lower()
    if choice == 'r':
        register()
    elif choice == 'l':
       email = login()
       if email:
            while True:
                option= input("\n to create project enter 1\n to show all projects enter 2\n to edit project enter 3\n to delete project enter 4\n").lower()
                if option == '1':
                    create_project(email)
                    continue
                elif option == '2':
                     view_projects()
                     continue
                elif option == '3':
                    edit_project(email)
                    continue
                elif option == '4':
                    delete_project(email)
                    continue

       else:
           continue




    else:
        print("Invalid choice. Enter 'r' for register or 'l' for login.")
