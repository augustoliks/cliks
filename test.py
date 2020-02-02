from git import Repo

repo = Repo('.')
repo.git.add('.')
repo.git.commit('.', '-m', 'carlos')
