from logs_template_nginx import nginx_log
import log_data_nginx

logs_program_nginx = [
    #####################################################################################
    # nginx alert logs - for the Summary Dashboard - 01:00 - 1 log needed to create rules
    #
    #####################################################################################
    {"log_type": nginx_log, "from_time": "01:00:00", "to_time": "01:10:00", "every": 10, "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'remote_addr', "values": log_data_nginx.nginx_remote_addr}
     ]
    }
]