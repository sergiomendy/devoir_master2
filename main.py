import os
import nbformat
import git

folders = {
    "data":{"cleaned":{},"processed":{}, "raw":{} },
    "docs":{},
    "LICENCE":None,
    "Makefile":None,
    "models":{},
    "notebooks": {
        "main.ipynb":None
        },
    "README.md":None,
    "reports":{},
    "requirements.txt":None,
    "src": {
        "utils.py":None,
        "process.py":None,
        "train.py":None
        }
}

def create_folder(directory, folder_name):
    os.makedirs(os.path.join(directory,folder_name), exist_ok=True)
    print(f"Folder '{folder_name}' created successfully!!!!")


def create_file(directory, filename, content):
    path = os.path.join(directory,filename)
    extension = filename.split(".")[-1]
    
    if extension == "ipynb":
        nb = nbformat.v4.new_notebook()
        nb["cells"] = [nbformat.v4.new_code_cell(content)]
        nbformat.write(nb, path)
        print(f"Notebook '{filename}' created successfully!!!!")
    else:
        with open(path,"w") as file:
            if content:
                file.write(content)
            print(f"File '{filename}' created successfully!!!!")

def create_directories_and_files():
    cwd = os.getcwd()
    for f in folders.keys():
        if isinstance(folders.get(f), dict):
            create_folder(cwd,f)
            subs = folders.get(f)
            for sub in subs:
                dir = os.path.join(cwd,f)
                if isinstance(subs.get(sub), dict):
                    create_folder(dir,sub)
                else:
                    content = subs.get(sub)
                    create_file(dir,sub,content)
        else:
            content=folders.get(f)
            create_file(cwd, f, content)


def to_git_repo():
    cwd = os.getcwd()
    try:
        repo = git.Repo.init(cwd)
        repo.git.add(all=True)

        repo.git.commit(m="Initial commit")
        print("Initial commit created")
    except git.GitCommandError as e:
        print(f"Error creating Git repository: {e}") 

if __name__=="__main__":
    create_directories_and_files()
    to_git_repo()