from modules.project import *
import os
from colorama import Fore
import json

all_projects = []

def main():
    option = 0
    project = Project("ESMS", "Environmental and Social Management System is Risk Assessment application that evaluates the risk associated with a certain loan", "22-06-2024", "Andrica Mabusela")    
    
    while option != 3:
      #os.system("cls") # clear the current terminal output before executing the code below.
      print(f"{Fore.GREEN}##### Welcome To The Yenzakanje Project Manager #####")
      print(f"{Fore.RED}what would you like to do?{Fore.WHITE}")
      print("1) Create a project")
      print("2) Show all the projects")
      print("3) Quit application")
      
      option = int(input("Enter Your Option: "))
      
      if option == 1:
         create_project()
         write_to_json_file(all_projects)
         
      if option == 2:
          show_all_projects()


def create_project():
     name = input(f"{Fore.GREEN}Please Enter Name Of Project:{Fore.GREEN}")
     description = input("Please Enter The Description Of Your Project:")
     manager = input("Please Enter The Full Name Of The Manager Of Your Project:")
     start_date = input(f"{Fore.GREEN}Please Enter The Start Date Of Your project:{Fore.WHITE}")

     project_data = Project(name, description, start_date, manager)
     project_data.create_project()
     all_projects.append(project_data.project)
     print(f"Project {project_data.project["project Name"]} Has been created Successfully!")
         
def show_all_projects():
    print("All Projects:", all_projects)    
         
def write_to_json_file(list_data):
    json_array = []
    for index in range(len(list_data)):
        json_object = json.dumps(list_data[index], indent=None)
        json_array.append(json_object)
    
    json_array = str(json_array)
    
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
      outfile.write(json_array)

if __name__ == "__main__":
    main()