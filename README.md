# Active_learning

1) create a virtual environment:
write this command in cmd to create a virtual environment

python -m venv venv


2) open the project into your code editor (for me i use visual code)
shortcut to open the project into VS code type 

code .


3) installing requirements
open the terminal in vs code and activate your virtual environment by this command

venv/Scripts/activate


4) then install all requirement 
if you are using python version > 3.9 please  go to requirements.txt and replace    backports.zoneinfo==0.2.1   by   backports.zoneinfo;python_version<"3.9"
  and then type the below command

pip install -r requirements.txt



5) wait till all the requirements have been installed. then run the server by this command

python manage.py runserver



