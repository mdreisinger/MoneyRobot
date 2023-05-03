# aws_instance.bastion:
resource "aws_instance" "bastion" {
    ami                                  = "ami-0735c191cf914754d"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 2
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = true
    get_password_data                    = false
    hibernation                          = false
    iam_instance_profile                 = "bastion_role"
    instance_initiated_shutdown_behavior = "stop"
    instance_type                        = "t3.small"
    key_name                             = "bastion-dev-key"
    monitoring                           = false
    placement_partition_number           = 0
    private_ip                           = "172.31.20.102"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-035dbb05ef24c3cb5"
    tags                                 = {
        "Name" = "bastion"
    }
    tags_all                             = {
        "Name" = "bastion"
    }
    tenancy                              = "default"
    vpc_security_group_ids               = [
        "sg-0456ac3f894e8f5f9",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    credit_specification {
        cpu_credits = "unlimited"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = true
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        encrypted             = false
        iops                  = 3000
        tags                  = {}
        throughput            = 125
        volume_size           = 8
        volume_type           = "gp3"
    }
}
# aws_instance.moneyrobotapi:
resource "aws_instance" "moneyrobotapi" {
    ami                                  = "ami-0735c191cf914754d"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 2
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = true
    get_password_data                    = false
    hibernation                          = false
    iam_instance_profile                 = "bastion_role"
    instance_initiated_shutdown_behavior = "stop"
    instance_type                        = "t3.small"
    key_name                             = "bastion-dev-key"
    monitoring                           = false
    placement_partition_number           = 0
    private_ip                           = "172.31.28.200"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-035dbb05ef24c3cb5"
    tags                                 = {
        "Name" = "moneyrobotapi"
    }
    tags_all                             = {
        "Name" = "moneyrobotapi"
    }
    tenancy                              = "default"
    vpc_security_group_ids               = [
        "sg-0456ac3f894e8f5f9",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    credit_specification {
        cpu_credits = "unlimited"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = true
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        encrypted             = false
        iops                  = 3000
        tags                  = {}
        throughput            = 125
        volume_size           = 8
        volume_type           = "gp3"
    }
}