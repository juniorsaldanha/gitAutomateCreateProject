import os, sys
from github import Github
from dotenv import load_dotenv

load_dotenv(dotenv_path=".envgit")

path = os.getenv("FILEPATH")
usernamegit = os.getenv("USERNAMEGIT")
passwordgit = os.getenv("PASSWORDGIT")

class clientGit:
    def __init__(self, user:str, password:str, default_path:str):
        self.user = user
        self.password = password
        self.default_path = default_path
        self.project = str(sys.argv[1])
        self.Client = Github(self.user, self.password).get_user()
    
    def create_folder(self):
        try:
            os.mkdir(str(self.default_path) + str(self.project))
            os.chmod(str(self.default_path) + str(self.project))
            print(f"Folder Created and permission fixed!\n")
        except Exception as err:
            print(f"Exception in Create Folder: {err}\n")
    
    def create_git(self):
        try:
            repo = self.Client.create_repo(self.project)
            print(f"repo value: {repo}\n")
            print(f"Succesfully created repository git {self.project} in {self.default_path}{self.project}!\n")
        except Exception as err:
            print(f"Exception in Create Git: {err}\n")
    
if __name__ == "__main__":
    try:
        newProject = clientGit(user=usernamegit,password=passwordgit,default_path=path)
        newProject.create_folder()
        newProject.create_git()
        print(f"Done, new project in GitHub github.com/{newProject.user}/{newProject.project}.git")
    except Exception as err:
        print(f"ERROR MAIN: {err}")

