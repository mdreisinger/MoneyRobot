data "aws_iam_policy_document" "createDatabaseTables_assume_role_policy" {
  statement {
    actions = [
      "sts:AssumeRole"
    ]
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "createDatabaseTables_domain_join_policy" {
  statement {
    actions = [
        "secretsmanager:DescribeSecret",
        "secretsmanager:GetSecretValue",
        "ec2:DescribeNetworkInterfaces",
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface",
        "ec2:DescribeInstances",
        "ec2:AttachNetworkInterface"
    ]
    effect = "Allow"
    resources = ["*"]
  }
}

resource "aws_iam_role" "createDatabaseTables-role-0f4ohe5s" {
    name = "createDatabaseTables-role-0f4ohe5s"
    assume_role_policy = data.aws_iam_policy_document.createDatabaseTables_assume_role_policy.json
    inline_policy {
        policy = data.aws_iam_policy_document.createDatabaseTables_domain_join_policy.json
    }
    path = "/service-role/"
}