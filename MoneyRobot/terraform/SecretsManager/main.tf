# aws_secretsmanager_secret.moneyrobot-dev-secret:
resource "aws_secretsmanager_secret" "moneyrobot-dev-secret" {
    description      = "Creds to access moneyrobot-dev RDS instance."
    name             = "moneyrobot-dev-secret"
    tags             = {}
    tags_all         = {}
}