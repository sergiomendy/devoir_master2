# MENDY Serge Wilson --- Master 2 - Data Science
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
        "main.ipynb":"from math import sqrt\n\nprint(sqrt(25))"
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
        

def create_directories_and_files(folder_name):
    cwd = os.getcwd()
    repo = git.Repo(cwd)
    create_folder(cwd, folder_name)

    for f in folders.keys():
        is_folder = isinstance(folders.get(f), dict)
        if is_folder:
            create_folder(folder_name,f)
            subs = folders.get(f)
            for sub in subs:
                dir = os.path.join(folder_name,f)
                if isinstance(subs.get(sub), dict):
                    create_folder(dir,sub)
                else:
                    content = subs.get(sub)
                    create_file(dir,sub,content)
        else:
            content=folders.get(f)
            create_file(folder_name, f, content)
        
        if is_folder:
            path = os.path.join(folder_name, f)
            repo.index.add([path])
            repo.index.commit(f"Adding {f} folder and its contents")
        else:
            path = os.path.join(folder_name, f)
            repo.index.add([path])
            repo.index.commit(f"Adding {f} file")

        branch = repo.active_branch
        repo.git.push('origin', branch)


if __name__=="__main__":
    folder_name = input("Enter the name of your folder: ")
    create_directories_and_files(folder_name)