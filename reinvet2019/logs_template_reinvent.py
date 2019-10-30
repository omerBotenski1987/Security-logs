suricata_url = {
  "type": "suricata",
  "source_host" : "Dana-pc",
  "flow_id": 94004070932976,
  "in_iface": "eth0",
  "event_type": "fileinfo",
  "src_ip": "10.0.0.0",
  "src_port": 4498,
  "dest_ip": "141.8.224.25",
  "dest_port": 80,
  "proto": "TCP",
  "http": {
    "hostname": "gioogle.com",
    "http_user_agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "http_content_type": "text/html",
    "http_refer": "http://gioogle.com/test",
    "http_method": "GET",
    "protocol": "HTTP/1.1",
    "status": 200,
    "length": 416
  },
  "app_proto": "http",
  "fileinfo": {
    "filename": "/",
    "state": "CLOSED",
    "stored": False,
    "size": 714,
    "tx_id": 0
  }
}

suricata_redirect = {
  "type": "suricata",
  "source_host" : "Dana-pc",
  "flow_id": 94004070932976,
  "in_iface": "eth0",
  "event_type": "fileinfo",
  "src_ip": "10.0.0.0",
  "src_port": 4498,
  "dest_ip": "141.8.224.25",
  "dest_port": 80,
  "proto": "TCP",
  "http": {
    "hostname": "gioogle.com",
    "http_user_agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "http_content_type": "text/html",
    "http_refer": "http://gioogle.com/test",
    "http_redirect" : "test",
    "http_method": "GET",
    "protocol": "HTTP/1.1",
    "status": 200,
    "length": 416
  },
  "app_proto": "http",
  "fileinfo": {
    "filename": "/",
    "state": "CLOSED",
    "stored": False,
    "size": 714,
    "tx_id": 0
  }
}

zeek_nmap = {
  "uid": "CA6CxhzLCfpj8QoGi",
  "type": "zeek",
  "id.orig_h": "185.175.93.105",
  "id.orig_p": 45516,
  "id.resp_h": "172.31.90.254",
  "id.resp_p": 8203,
  "proto": "tcp",
  "duration": 0.143054,
  "orig_bytes": 0,
  "resp_bytes": 0,
  "conn_state": "REJ",
  "local_orig": False,
  "local_resp": False,
  "missed_bytes": 0,
  "history": "SrR",
  "orig_pkts": 2,
  "orig_ip_bytes": 80,
  "resp_pkts": 1,
  "resp_ip_bytes": 40,
  "tunnel_parents": [

  ]
}

zeek_rdp = {
  "uid": "CDOflk3QeQ7g7Q7mv2",
  "type": "zeeke",
  "id.orig_h": "74.219.104.106",
  "id.orig_p": 10555,
  "id.resp_h": "172.31.90.254",
  "id.resp_p": 3389,
  "cookie": "Administrator",
  "cert_count": 0

}

logon_success_4624_log = {
	"process_id": 596,
	"logzio_codec": "plain",
	"event_data": {
		"TransmittedServices": "-",
		"SubjectLogonId": "0x3e7",
		"SubjectDomainName": "ORGANIZATION",
		"TargetUserName": "RANDOMIZE",
		"LogonGuid": "{088F0999-4C49-4C79-ADF1-F2840EF7B1CE}",
		"IpPort": "0",
		"ElevatedToken": "%%1822",
		"VirtualAccount": "%%1822",
		"IpAddress": "RANDOMIZE",
		"SubjectUserName": "EC2AMAZ-AEGIACD$",
		"ImpersonationLevel": "%%1823",
		"TargetOutboundDomainName": "-",
		"TargetUserSid": "S-1-5-21-1282426543-1088070111-3804447329-1106",
		"KeyLength": "0",
		"LmPackageName": "-",
		"TargetOutboundUserName": "-",
		"ProcessName": "C:\\Windows\\System32\\svchost.exe",
		"LogonProcessName": "User32 ",
		"WorkstationName": "EC2AMAZ-AEGIACD",
		"TargetLogonId": "0x9e8c4c7",
		"LogonType": "10",
		"ProcessId": "0x48",
		"SubjectUserSid": "S-1-5-19",
		"TargetLinkedLogonId": "0x9e7c4d8",
		"AuthenticationPackageName": "Negotiate",
		"TargetDomainName": "ORGANIZATION",
		"RestrictedAdminMode": "%%1843"
	},
	"type": "wineventlog",
	"opcode": "Info",
	"thread_id": 6776,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"hostname": "EC2AMAZ-AEGIACD",
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD"
	},
	"activity_id": "{175BA43A-D733-0000-48A4-5B1733D7D401}",
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ - AEGIACD.FlySafe.internal",
	"log_name": "Security",
	"level": "Information",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"event_id_description": "An account was successfully logged on",
	"event_id": 4624,
	"task": "Logon",
	"meta": {
		"cloud": {
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "us-east-2",
			"availability_zone": "us-east-2a",
			"provider": "ec2"
		}
	}
}

logon_failed_4625_log = {
	"process_id": "596",
	"keywords": [
		"Audit Failure"
	],
	"logzio_codec": "plain",
	"record_number": "970554",
	"event_data": {
		"ProcessName": "-",
		"LmPackageName": "-",
		"KeyLength": "0",
		"ProcessId": "0x0",
		"SubjectLogonId": "0x0",
		"TargetUserSid": "S-1-0-0",
		"IpPort": "0",
		"TargetDomainName": "FlySafe",
		"Status": "0xc000006d",
		"SubjectUserSid": "S-1-0-0",
		"IpAddress": "1.1.1.1",
		"LogonType": "3",
		"AuthenticationPackageName": "NTLM",
		"WorkstationName": "ec2-54-144-39-189.compute-1.amazonaws.com",
		"LogonProcessName": "NtLmSsp ",
		"TargetUserName": "RANDOMIZE",
		"FailureReason": "%%2313",
		"SubjectUserName": "-",
		"SubjectDomainName": "-",
		"SubStatus": "0xc000006a",
		"TransmittedServices": "-"
	},
	"opcode": "Info",
	"type": "wineventlog",
	"thread_id": 6320,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"hostname": "EC2AMAZ-AEGIACD",
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ-AEGIACD.FlySafe.internal",
	"log_name": "Security",
	"level": "Information",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"tags": [
		"beats-5015"
	],
    "event_id_description": "An account failed to login to the system",
	"event_id": 4625,
	"task": "Logon",
	"meta": {
		"cloud": {
			"availability_zone": "eu-west-2b",
			"provider": "ec2",
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "eu-west-2b"
		}
	}
}

logzio_security = {
    "origin_feeds": [
        "dan.me.uk - Tor tracker"
    ],
    "origin_feeds_num": 1,
    "context": [
        "Malicious IP"
    ],
    "severity": 5,
    "ioc": {
        "malicious_ip": "69.146.146.75"
    }
}