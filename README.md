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
- `ssh -i ".ssh/bastion-dev-key.pem" ubuntu@ec2-35-90-1-56.us-west-2.compute.amazonaws.com`
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
        
# Package and push database_setup to S3
- `poetry build`
- `aws s3 cp dist/moneyrobot-0.1.0-py3-none-any.whl s3://moneyrobot/`
- On Bastion:
  - Install pip `sudo apt install python3-pip`
  - Install aws-cli `sudo apt  install awscli`
  - Download wheel file: `cd /tmp/; aws s3 cp s3://moneyrobot/moneyrobot-0.1.0-py3-none-any.whl .`
  - Install package: `sudo pip install moneyrobot-0.1.0-py3-none-any.whl`

# Push API image to ECR
- `aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 126493000772.dkr.ecr.us-west-2.amazonaws.com`
- `docker build -t moneyrobotapi . --platform linux/amd64`
- `docker tag moneyrobotapi:latest 126493000772.dkr.ecr.us-west-2.amazonaws.com/moneyrobotapi:latest`
- `docker push 126493000772.dkr.ecr.us-west-2.amazonaws.com/moneyrobotapi:latest`
- **ALL IN ONE:** `aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 126493000772.dkr.ecr.us-west-2.amazonaws.com;docker build -t moneyrobotapi . --platform linux/amd64;docker tag moneyrobotapi:latest 126493000772.dkr.ecr.us-west-2.amazonaws.com/moneyrobotapi:latest;docker push 126493000772.dkr.ecr.us-west-2.amazonaws.com/moneyrobotapi:latest; say "Image Pushed"`

# Connect to moneyrobotapi EC2
- `ssh -i ".ssh/bastion-dev-key.pem" ubuntu@ec2-34-219-46-236.us-west-2.compute.amazonaws.com`

# Run api on moneyrobotapi EC2:
- (Conditional) `cd /tmp; curl -fsSL https://get.docker.com -o get-docker.sh; sh get-docker.sh`
- (Conditional) `sudo apt install awscli`
- `aws ecr get-login-password --region us-west-2 | sudo docker login --username AWS --password-stdin 126493000772.dkr.ecr.us-west-2.amazonaws.com`
- `sudo docker pull 126493000772.dkr.ecr.us-west-2.amazonaws.com/moneyrobotapi:latest`
- `sudo docker run 126493000772.dkr.ecr.us-west-2.amazonaws.com/moneyrobotapi`

# Connect to API from host machine:
- In web browser: http://ec2-34-219-46-236.us-west-2.compute.amazonaws.com/docs

# Queries
## Rent
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ('Rent');`

## Utilities
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Xcel energy", "xfinity", "Parking permit", "Conservice", "T-mobile", "AWS");`

## Groceries
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ('Groceries');`

## Transportation
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Vehicle maintenance", "Gas", "Car wash", "Parking fees", "DMV fees", "Tolls", "Transportation");`

## Medical Expenses
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Prescriptions", "Medical Appoiintments");`

## Personal Expenses
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Wardrobe", "Home stuff", "Toiletries");`

## Entertainment and Hobbies
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Eating out & drinks", "Entertainment", "Snowboarding", "Course fees", "Subscriptions", "Hobbies", "Tools", "AWS", "Guns", "Ammo", "Gun stuff", "Plant stuff", "Bike stuff");`

## Pets
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Dog vet fees", "Cat vet fees", "Dog medication", "Cat medication", "Dog food", "Cat food", "Dog supplies", "Cat supplies", "Dog sitting", "Cat sitting", "Dog license", "ESA Fees");`

## Gifts
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Gifts");`

## Investments
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Investments");`

## Other
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Other");`

## Income
- `SELECT SUM(transaction_amount) FROM transactions WHERE transaction_date > '2023-03-01' and transaction_date < '2023-04-01' AND transaction_category IN ("Income", "Support from dad", "Income - Other");`