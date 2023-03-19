# aws_iam_role.createDatabaseTables-role-0f4ohe5s:
resource "aws_iam_role" "createDatabaseTables-role-0f4ohe5s" {
    assume_role_policy    = jsonencode(
        {
            Statement = [
                {
                    Action    = "sts:AssumeRole"
                    Effect    = "Allow"
                    Principal = {
                        Service = "lambda.amazonaws.com"
                    }
                },
            ]
            Version   = "2012-10-17"
        }
    )
    force_detach_policies = false
    managed_policy_arns   = [
        "arn:aws:iam::126493000772:policy/service-role/AWSLambdaBasicExecutionRole-11d69ec0-4afb-4b49-8af7-2362c8b96866",
    ]
    max_session_duration  = 3600
    name                  = "createDatabaseTables-role-0f4ohe5s"
    path                  = "/service-role/"
}