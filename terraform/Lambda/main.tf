# aws_lambda_function.createDatabaseTables:
resource "aws_lambda_function" "createDatabaseTables" {
    s3_bucket                      = "moneyrobot"
    s3_key                         = "create_db_tables_package.zip"
    description                    = "Creates empty tables to intialize a new moneyrobot database."
    function_name                  = "createDatabaseTables"
    handler                        = "CreateTables.create_tables"
    memory_size                    = 1500
    package_type                   = "Zip"
    role                           = "arn:aws:iam::126493000772:role/service-role/createDatabaseTables-role-0f4ohe5s"
    runtime                        = "python3.9"
    timeout                        = 600
    environment {
        variables = {
            RDS_HOST = ""
            USERNAME = ""
            PASSWORD = ""
            DB_NAME = ""
        }
    }
    vpc_config {
        security_group_ids = [
            "sg-0456ac3f894e8f5f9",
        ]
        subnet_ids         = [
            "subnet-02ea99e4e256f543c",
            "subnet-035dbb05ef24c3cb5",
            "subnet-04c898d90048b637f",
            "subnet-092bacb96803819f3",
        ]
    }
}