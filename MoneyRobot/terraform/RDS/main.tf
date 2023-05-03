# aws_db_instance.MoneyRobotDatabase:
resource "aws_db_instance" "MoneyRobotDatabase" {
    allocated_storage                     = 20
    auto_minor_version_upgrade            = true
    availability_zone                     = "us-west-2c"
    backup_retention_period               = 7
    backup_window                         = "13:30-14:00"
    ca_cert_identifier                    = "rds-ca-2019"
    copy_tags_to_snapshot                 = true
    customer_owned_ip_enabled             = false
    db_name                               = "moneyrobot"
    db_subnet_group_name                  = "default"
    delete_automated_backups              = true
    deletion_protection                   = true
    enabled_cloudwatch_logs_exports       = [
        "general",
    ]
    engine                                = "mysql"
    engine_version                        = "8.0.32"
    iam_database_authentication_enabled   = true
    identifier                            = "moneyrobot-dev"
    instance_class                        = "db.m6i.large"
    iops                                  = 3000
    kms_key_id                            = "arn:aws:kms:us-west-2:126493000772:key/3d678adb-a24b-4204-8293-126d5dd6ab4f"
    license_model                         = "general-public-license"
    maintenance_window                    = "mon:07:00-mon:09:00"
    max_allocated_storage                 = 100
    monitoring_interval                   = 60
    monitoring_role_arn                   = "arn:aws:iam::126493000772:role/rds-monitoring-role"
    multi_az                              = false
    network_type                          = "IPV4"
    option_group_name                     = "default:mysql-8-0"
    parameter_group_name                  = "default.mysql8.0"
    performance_insights_enabled          = true
    performance_insights_kms_key_id       = "arn:aws:kms:us-west-2:126493000772:key/3d678adb-a24b-4204-8293-126d5dd6ab4f"
    performance_insights_retention_period = 7
    port                                  = 3306
    publicly_accessible                   = false
    security_group_names                  = []
    skip_final_snapshot                   = true
    storage_encrypted                     = true
    storage_throughput                    = 125
    storage_type                          = "gp3"
    tags                                  = {}
    tags_all                              = {}
    username                              = "moneyrobot"
    vpc_security_group_ids                = [
        "sg-0456ac3f894e8f5f9",
    ]
}