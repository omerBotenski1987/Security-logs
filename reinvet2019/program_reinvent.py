import logs_template_reinvent
import log_data_reinvent

logs_program_reinvent = [


    ###########################################################################################
    #                                    Reinvent  story                                      #
    #               benign activity from 7:00 - 11:00 and from 11:35 - 12:30                  #
    #               malicious activity at 11:30 dana clicks the malicious link with the URL   #
    #               nmap scanning from 12:00 - 12:30 every 5 minutes                          #
    #               first suspicious connection attempt from dana PC to DC at 20:01           #
    #               more connection attempt at 20:10                                          #
    #                                                                                         #
    #                                                                                         #
    # 7:00 - 11:00 -> benign logins from users (rdp included) every 30 minutes                #
    # All day traffic every 20 minutes ( with malicious IPs as well)                          #
    # 11:29 -> Dana receives a mail with malicious link and double click it                   #
    # 11:30 -> Dana is redirected to a malicious URL that download the fileless payload       #
    # 11:35 - 12:30 - benign logins from users every 10 minutes                               #
    # 12:00 - 12:30 - Nmap scanning every 5 minutes                                           #
    #           * can add a log for RDP vulnerability scanning                                #
    # 20:01 -> first suspicious RDP connection from dana pc to DC                             #
    # 20:10 -> more malicious connection attempt to the DC using Dana's credentials           #
    #                                                                                         #
    ###########################################################################################
#failed login from users
{"log_type": logs_template_reinvent.logon_failed_4625_log, "from_time": "06:59:00", "to_time": "07:00:00", "every": 60 * 1, "cross_fields": False,
 "add_logzio_security": False, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_reinvent.benign_users},
         {"field_name": 'event_data|WorkstationName', "values": log_data_reinvent.benign_users_pc},
         {"field_name": 'event_data|IpAddress', "values": log_data_reinvent.internal_ip_addresses},
         {"field_name": 'event_data|LogonType', "values":log_data_reinvent.normal_logon_type}

     ]
     },


# 7:00 - 11:00 normal login activituy - winevent log

{"log_type": logs_template_reinvent.logon_success_4624_log, "from_time": "07:00:00", "to_time": "07:10:00", "every": 60 * 1, "cross_fields": False,
 "add_logzio_security": False, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_reinvent.benign_users},
         {"field_name": 'event_data|WorkstationName', "values": log_data_reinvent.benign_users_pc},
         {"field_name": 'event_data|IpAddress', "values": log_data_reinvent.internal_ip_addresses},
         {"field_name": 'event_data|LogonType', "values":log_data_reinvent.normal_logon_type}

     ]
     },
# 11:29 - 11:30 link redirect to the paypal web site
{"log_type": logs_template_reinvent.suricata_url, "from_time": "07:15:00", "to_time": "07:17:00", "every": 60 * 1, "cross_fields": False,
 "add_logzio_security": False, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'source_hostn', "values": log_data_reinvent.dana_user_pc},
         {"field_name": 'src_ip', "values": log_data_reinvent.dana_ip_address},
         {"field_name": 'http|http_hostname', "values": log_data_reinvent.paypal_domain},
         {"field_name": 'http|http_refer', "values": log_data_reinvent.paypal_login_page},

     ]
     },
# 11:30 - 11:31 malicious URL log from Dana PC
{"log_type": logs_template_reinvent.suricata_redirect, "from_time": "07:20:00", "to_time": "07:21:00", "every": 60 * 1, "cross_fields": False,
     "add_logzio_security": False, "url_field": 'http|http_redirect',
     "fields": [
         {"field_name": 'source_host', "values": log_data_reinvent.dana_user_pc},
         {"field_name": 'src_ip', "values": log_data_reinvent.dana_ip_address},
         {"field_name": 'http|http_redirect', "values": log_data_reinvent.malicious_url},
         {"field_name": 'http|http_hostname', "values": log_data_reinvent.malicious_domain}

     ]
     },
{"log_type": logs_template_reinvent.suricata_redirect, "from_time": "11:30:00", "to_time": "11:31:00", "every": 60 * 1, "cross_fields": False,
     "add_logzio_security": False, "url_field": 'http|http_redirect',
     "fields": [
         {"field_name": 'source_host', "values": log_data_reinvent.dana_user_pc},
         {"field_name": 'src_ip', "values": log_data_reinvent.dana_ip_address},
         {"field_name": 'http|http_redirect', "values": log_data_reinvent.malicious_url},
         {"field_name": 'http|http_hostname', "values": log_data_reinvent.malicious_domain}
         ]
 },


# 11:35 - 12:30 normal login activituy - winevent log

{"log_type": logs_template_reinvent.logon_success_4624_log, "from_time": "07:24:00", "to_time": "07:34:00", "every": 60 * 3, "cross_fields": False,
 "add_logzio_security": False, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_reinvent.benign_users},
         {"field_name": 'event_data|WorkstationName', "values": log_data_reinvent.benign_users_pc},
         {"field_name": 'event_data|IpAddress', "values": log_data_reinvent.internal_ip_addresses},
         {"field_name": 'event_data|LogonType', "values": log_data_reinvent.normal_logon_type}
     ]
     },

#12:00 - 12:30 -> Nmap scans from Dana PC toward the network
{"log_type": logs_template_reinvent.zeek_nmap, "from_time": "07:40:00:00", "to_time": "07:46:00", "every": 60 * 3, "cross_fields": False,
 "add_logzio_security": False, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'id.orig_h', "values": log_data_reinvent.dana_ip_address},
         {"field_name": 'id.resp_h', "values": log_data_reinvent.server_ip_address},
         {"field_name": 'id.resp_p', "values": log_data_reinvent.scanned_ports},
         {"field_name": 'id.orig_p', "values": log_data_reinvent.source_ports}

     ]
 },
 {"log_type": logs_template_reinvent.zeek_rdp, "from_time": "07:50:00", "to_time": "07:52:00", "every": 60 * 1,"cross_fields": False,
  "add_logzio_security": False, "ip_field": 'data|srcip',
  "fields": [
      {"field_name": 'id.orig_h', "values": log_data_reinvent.dana_ip_address},
      {"field_name": 'id.resp_h', "values": log_data_reinvent.server_ip_address},


  ]
  },

#20:01 first connection attempt to dc from dana

{"log_type": logs_template_reinvent.logon_failed_4625_log, "from_time": "07:54:00", "to_time": "07:55:00", "every": 60 * 1, "cross_fields": False,
 "add_logzio_security": False, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_reinvent.malicious_user},
         {"field_name": 'event_data|WorkstationName', "values": log_data_reinvent.server_name},
         {"field_name": 'event_data|IpAddress', "values": log_data_reinvent.dana_ip_address},
         {"field_name": 'event_data|LogonType', "values":log_data_reinvent.rdp_logon_type}

     ]
     },

#20:10 - 20:23 -> failed RDP logins from malicious sources with Dana's user name.

{"log_type": logs_template_reinvent.logon_failed_4625_log, "from_time": "08:00:00", "to_time": "08:23:00", "every": 60 * 1, "cross_fields": True,
 "add_logzio_security": False, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_reinvent.malicious_user},
         {"field_name": 'event_data|WorkstationName', "values": log_data_reinvent.server_name},
         {"field_name": 'event_data|IpAddress', "values": log_data_reinvent.malicious_addresses},
         {"field_name": 'event_data|LogonType', "values":log_data_reinvent.rdp_logon_type}

     ]
     },
]