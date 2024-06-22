class Project:
    def __init__(self, project_name, project_description, project_start_date, project_manager, project = dict({})):
        self.project_name = project_name
        self.project_description = project_description
        self.project_start_date = project_start_date
        self.project_manager = project_manager
        
    def create_project(self):
        self.project = {
            "project Name": self.project_name,
            "Project Description": self.project_description,
            "Project Start Date": self.project_start_date,
            "Project Manager": self.project_manager
        }
    
    def show_project_details(self):
        print("Project Name:", self.project_name)
        print("Project Description:", self.project_description)
        print("Project Manager:", self.project_manager)
        print("Project Start Date:", self.project_start_date)
        
    def edit_project(self, project_name, project_description, project_manager):
        self.project_name = project_name
        self.project_description = project_description
        self.project_manager = project_manager
        