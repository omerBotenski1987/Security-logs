# security-demo-sender
Source for the demo-sender docker

The files in this repository are taken from the logzio/logs-generator repository. 


In order to send security enriched logs run:

python send_demo_data.py {LISTENER} {ACCOUNT-TOKEN} {hh:mm:ss}

for example:
python send_demo_data.py http://listener.logz.io:8070 sometoken 06:40:00

* we need the last parameter because the original script is built to send logs over a time period of 24 hours. because we don't want to wait all that time we can enter a specific time period to tell the script we want it to consider the current time to be the time we entered. that way, if we enter a time that the script needs to send logs in, he will send them right away (in each time frame the script sends logs every X minutes/seconds. so keep in mind that in order to send logs right away you need to find a timeframe that sends logs every 1 second, otherwise you will need to wait the whole time period).

more detailed information about the script can be found here: https://github.com/logzio/logs-generator/tree/master
