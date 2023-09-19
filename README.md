# devoir_master2
This programm create a ready to use folders and files that you may use in a datascience project. 

### How was it designed? : 
To design this programm, I create a dict variable where I have folders and files as "key" and and the content of the file or subfolders as values.
A folder is represented by: {}
A file is represented by : None or a str (the content of the file)

After represented the tree as a nested dict, I create some functions to create the tree:
- 1. create_folder : this is used to create a folder
- 2. create_file : this is used to create a file
- 3. create_directories_and_files(folder_name) : this function take an argument where all the tree will be created, in this function we iter the keys of our dict and create the folder or file depending of the type of the value. And after each iteration the following file or folder is added, commited and pushed to git repo.


### How to run it?
To run correctly the main.py programm follow these following steps:
These steps presuppose that this repo is already cloned and you are in the repo.
- 1. run:
     ```bash
     pip install -r requirements.txt
     ```
- 2. python main.py and after you will be asked to give a "project_name" where the tree will be created.
