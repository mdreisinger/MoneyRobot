# MoneyRobot
An application to manage personal finances.

# Python Version
`3.9`

# Pyenv / Poetry
- [pyenv](https://realpython.com/intro-to-pyenv/)
- [poetry](https://python-poetry.org/docs/basic-usage/)

# Connect to RDS instance from host machine using bastion to tunnel
[rds-connect-ec2-bastion-host](https://aws.amazon.com/premiumsupport/knowledge-center/rds-connect-ec2-bastion-host/)
- `ssh -i ".ssh/bastion-dev-key.pem" -L 3336:moneyrobot-dev.cejrdrwxbhyb.us-west-2.rds.amazonaws.com:3306 ubuntu@ec2-35-90-1-56.us-west-2.compute.amazonaws.com -N -f`
- `mysql -h 127.0.0.1 -P 3336 -u moneyrobot -p`

# Connect to RDS instance from bastion
- `ssh -i ".ssh/bastion-dev-key.pem" ec2-35-90-1-56.us-west-2.compute.amazonaws.com`
- (Conditional) `sudo apt update`
- (Conditional) `sudo apt install mysql-client`
- `mysql -h moneyrobot-dev.cejrdrwxbhyb.us-west-2.rds.amazonaws.com -u moneyrobot -p`

# Entity Relationship Diagram
Edit [here](https://lucid.app/lucidchart/bfb9b9d4-dfc2-4de9-b9f7-2428763bdefa/edit?viewport_loc=-460%2C-59%2C2094%2C938%2CVGZGyrv0Gzg3&invitationId=inv_254e42df-804b-42dd-b150-4e20d3a46bee)

![Alt text](documentation/MoneyRobotERD.png?raw=true "Title")

# Random things to note:
- Defualt ec2 username: ubuntu
- To get poetry to create venv inside project path so that vscode will recognize it: `poetry config virtualenvs.in-project true`
  - If you already have created your project, you need to re-create the virtualenv to make it appear in the correct place:
        
        poetry env list  # shows the name of the current environment
        poetry env remove <current environment>
        poetry install  # will create a new environment using your updated configuration
        
# Package and push to S3
- `poetry build`
- `aws s3 cp dist/moneyrobot-0.1.0-py3-none-any.whl s3://moneyrobot/`
- On Bastion:
  - Install pip `sudo apt install python3-pip`
  - Install aws-cli `sudo apt  install awscli`
  - Download wheel file: `cd /tmp/; aws s3 cp s3://moneyrobot/moneyrobot-0.1.0-py3-none-any.whl .`
  - Install package: `sudo pip install moneyrobot-0.1.0-py3-none-any.whl`