# GuitarTabsMaker
Take screenshots of Guitar Tabs in youtube videos

Using guide : 

- Create an empty directory called "ScreeShots"
- Create an empty directory called "tabs"
- download from github with git clone
- in terminal (creates a virtual environment to install all dependencies)
    - python -m venv venv
    - venv\Scripts\activate
  Intstall dependencies :
    pip install -r requirements.txt

Finaly, run the main program : 
  python .\GuitarTabsMaker.py 

Once running:
  - Chose a fileName
  - Paste a youtube url

The program will then temporarly download the youtube video
  - Then select the screen part where the tabs are located
  - Finaly select a position in the tab that will only change when the tab changes
    
Wait a few secs and you ll get your brand new guitar tab ! 
You ll find it in the 'tabs' directory
Every temporary files will be deleted once the tab is created
