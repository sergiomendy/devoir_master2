from git import Repo

repo = Repo.init("./")

add_file = ["test.py","main.py"]  # relative path from git root
repo.index.add(add_file)  # notice the add function requires a list of paths

repo.index.commit("Commit for main and test")