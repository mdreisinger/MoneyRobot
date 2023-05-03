# aws_iam_role.bastion_role:
resource "aws_iam_role" "bastion_role" {
    assume_role_policy    = jsonencode(
        {
            Statement = [
                {
                    Action    = "sts:AssumeRole"
                    Effect    = "Allow"
                    Principal = {
                        Service = "ec2.amazonaws.com"
                    }
                },
            ]
            Version   = "2012-10-17"
        }
    )
    description           = "Allows EC2 instances to call AWS services on your behalf."
    force_detach_policies = false
    managed_policy_arns   = [
        "arn:aws:iam::aws:policy/AmazonS3FullAccess",
        "arn:aws:iam::aws:policy/SecretsManagerReadWrite",
        "arn:aws:iam::aws:policy/service-role/AWSAppRunnerServicePolicyForECRAccess",
    ]
    max_session_duration  = 3600
    name                  = "bastion_role"
    path                  = "/"
    tags                  = {}
    tags_all              = {}
}