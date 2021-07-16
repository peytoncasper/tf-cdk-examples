
resource "aws_wafv2_rule_group" "example" {
  name        = "complex-example"
  description = "An rule group containing all statements"
  scope       = "REGIONAL"
  capacity    = 500

  rule {
    name     = "rule-1"
    priority = 1

    action {
      block {}
    }

    dynamic "statement" {
      for_each = [{
        "not_statements": [{
          "and_statements": [{
            "geo_match_statements": [{
              "country_codes": ["US"]
            }]
          }]
        }],
        "or_statements": []
      }]
      content {
        dynamic "not_statement" {
          for_each = statement.value["not_statements"]
          content {
            statement {
              dynamic "and_statement" {
                for_each = not_statement.value["and_statements"]
                content {
                  statement {
                    dynamic "geo_match_statement" {
                      for_each = and_statement.value["geo_match_statements"]
                      content {
                        country_codes = geo_match_statement.value["country_codes"]
                      }
                    }
                  }
                }
              }
            }
          }
        }

        dynamic "or_statement" {
          for_each = statement.value["or_statements"]
          content {
            statement {

            }
          }
        }
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = false
      metric_name                = "rule-1"
      sampled_requests_enabled   = false
    }
  }


  visibility_config {
    cloudwatch_metrics_enabled = false
    metric_name                = "friendly-metric-name"
    sampled_requests_enabled   = false
  }

  tags = {
    Name = "example-and-statement"
    Code = "123456"
  }
}