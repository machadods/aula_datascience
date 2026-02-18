# metodo usado para enviar ao git
# (venv) PS C:\Users\wagner\Desktop\cursoSCTEC\aula_analise_de_dados> cd aula_11_git
# ados\aula_11_git> git add aula_11.py                          ados\aula_11_git> git init
# ados\aula_11_git> git commit -m "my first commit"             rsoSCTEC/aula_analise_de_dados/aula_11_git/.git/
#  1 file changed, 0 insertions(+), 0 deletions(-)
#  create mode 100644 aula_11.py
# (venv) PS C:\Users\wagner\Desktop\cursoSCTEC\aula_analise_de_dados\aula_11_git> git remote add origin https://github.com/machadods/aula_datascience.git
# (venv) PS C:\Usersgit statussktop\cursoSCTEC\aula_analise_de_dados\aula_11_git>
# On branch master
# nothing to commit, working tree clean
# (venv) PS C:\Users\wagner\Desktop\cursoSCTEC\aula_analise_de_dados\aula_11_git> git push
# fatal: The current branch master has no upstream branch.

#     git push --set-upstream origin master

# To have this happen automatically for branches without a tracking
# upstream, see 'push.autoSetupRemote' in 'git help config'.

# (venv) PS C:\Users\wagner\Desktop\cursoSCTEC\aula_analise_de_dados\aula_11_git> git push --set-upstream origin master
# Enumerating objects: 3, done.
# Counting objects: 100% (3/3), done.
# Writing objects: 100% (3/3), 233 bytes | 14.00 KiB/s, done.
# Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
# To https://github.com/machadods/aula_datascience.git
#  * [new branch]      master -> master
# branch 'master' set up to track 'origin/master'.
# (venv) PS C:\Users\wagner\Desktop\cursoSCTEC\aula_analise_de_dados\aula_11_git> 

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np