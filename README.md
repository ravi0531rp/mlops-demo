## A Sample ML Project with best MLops Practices


### Steps :

* Set up the github repo
* Create an Environment
```
conda create -p venv python=3.8 -y

# This creates a virtual env and also places a venv folder inside your repo

conda activate /Users/raprak-blrm20/Desktop/personal/CODES/m-projects/mlops-demo/venv
```

* Initiate Git init and do some initial commit.
```
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ravi0531rp/mlops-demo.git
git push -u origin main

```