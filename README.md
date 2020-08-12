# Automation to create GitRepo and Project locally - Python3

This project is just to automate the creation of projects locally and in GitHub

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install libs/requirements. 

```bash

git clone https://github.com/juniorsaldanha/gitAutomateCreateProject
cd gitAutomateCreateProject
cp -rf .* ~/
pip3 install -f requirements.txt
echo source .git.sh >> ~/.bashrc
nano ~/.envgit
```
## Change USERNAMEGIT, PASSWORDGIT, FILEPATH in ~/.envgit

 ``` nano ~/.envgit```

## Usage
Just type the following command above and your project will be created locally and remotely in GitHub. 
```bash
create newProject
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)