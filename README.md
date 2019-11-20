## Binventor is unhosted and thus unavailable for now. The hosting company I used (won't name names), was simply bad. I may bring it up again in the future.  Sorry for the inconvenience.

# [Binventor](https://binventor.com/)

**Binventor** is a text pasting web app that aims for simple & easy sharing of code snippets.
I started making it as a personal project for myself, in order to improve my web skills.
Then, I got into the Computer Science class at my high school, so I chose to put it online for my class to use.
If you are some random internet person who deliberately/accidentally got here, don't worry, my auto-non-cs-class-person-detector will find & eliminate you!

## Build and run locally (Linux Mac OS)
#### I will be very happy if someone can contribute and add Windows instructions as well! (I'm not a Windows user..)

Tested with Python 3.7 although any python 3+ should work.

It's recommended to use the Pipenv virtual environment instead of raw pip as it makes it a lot more easier to build, run and maintain. (just run `pipenv install` to install all necessary modules from `Pipfile`).

- Clone the repo (or download ZIP and extract if no Git): `git clone https://github.com/TomerShech/Binventor.git`
- `cd Binventor`
- `pip3 install -r requirements.txt` (on Windows it may be just `pip`)
- Install sqlite3, open a Python 3 shell and run:
```py
from app import db
db.create_all()
exit()
```
This will create the database with the `pastes` table.
- Make sure `run.sh` has correct premissions: `chmod +x run.sh` and then `./run.sh`

## Features:

- Manually choosing your code's programming language? no need! Binventor will automatically highlight it for you. (Thanks highlight.js!)

- **Protip:** name your paste with the extension of its language to force the highlighting of that language.
e.g. A paste name *"script.ts"* will make sure your code is highlighted as TypeScript and not as JavaScript!


- No more ugliness or unresponsive design! (Forgive me, Pastebin), Binventor is built with modern standards in mind.

- Your pastes will be deleted ONLY when you want them to. Select the expiration time you think is best.

- Use the keyboard shortcuts you're already familiar with, or, you know.. the regular buttons.


If using a computer, you can use _**CTRL + S**_ to save & get a shareable link, no need to use the button!


If you want to help me by contributing to this project, feel free to create a new pull request.

Thank you all for using my website,
Tomer.
