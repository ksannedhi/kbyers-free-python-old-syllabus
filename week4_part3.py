from pprint import pprint

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'
uptime5 = 'rtr2 uptime is 6 years, 18 weeks, 3 days, 8 hours, 23 minutes'

uptime_data = {}

for uptime in (uptime1, uptime2, uptime3, uptime4, uptime5):
    dev_name, up_time = uptime.split(" uptime is ")
    up_time_values = up_time.split(",")
    uptime_sec = 0
    for value in up_time_values:
        if "year" in value:
            num_years = int(value.split()[0])
            uptime_sec += num_years * 31536000
        if "week" in value:
            num_weeks = int(value.split()[0])
            uptime_sec += num_weeks * 604800
        if "day" in value:
            num_days = int(value.split()[0])
            uptime_sec += num_days * 86400
        if "hour" in value:
            num_hours = int(value.split()[0])
            uptime_sec += num_hours * 3600
        if "minute" in value:
            num_minutes = int(value.split()[0])
            uptime_sec += num_minutes * 60
    uptime_data[dev_name] = uptime_sec

pprint(uptime_data)
