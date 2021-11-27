from service.pager_duty_service import PagerDutyService

service = PagerDutyService("file")
team1 = {"team1": {"name": "claims"}, "developers": [{"name": "someone", "phone_number":
"9999999999"}, {"name": "somebody", "phone_number": "9111111111"}]}


service.create_team(team1)

service.receive_alert()