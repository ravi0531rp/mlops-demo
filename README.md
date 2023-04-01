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

* Add the .gitignore (preferably on github as it gives a good template) and then pull the changes to local. 

* Create setup.py and requirements.txt in root directory!

* Add the setup code to setup.py

* Create a src folder at root and then create an ```__init__.py``` file inside it. That will help src become a package.

* Since we added a ```-e .``` in the requirements.txt file, so when we run ```pip install -r requirements.txt``` , it also builds our package using the setup.py file.

* Once done, it creates a ```mlops_demo.egg-info``` folder as our built package.

* Create a components folder inside src. Add ```__init__.py```, ```data_ingestion.py```, ```data_transformation.py``` and ```model_trainer.py```

* Create a pipeline folder inside src. Add ```__init__.py```, ```train_pipeline.py```, ```predict_pipeline.py```

* Create ```exception.py```, ```logger.py``` and ```utils.py``` in src