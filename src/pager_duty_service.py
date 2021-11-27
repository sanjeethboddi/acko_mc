# interview@barraiser.com

# from module.firebase import FirebasePersistence

# from module.file_persistence import FilePersistence
from pickle import NONE
from flask import Flask, request
from service.notification_service import NotificationService
from module.file_persistence import FilePersistence
import json

app = Flask(__name__)


persistence_type = 'local'

# if persistence_type == 'firebase':
#     persistence = FirebasePersistence()
if persistence_type == 'local':
    persistance = FilePersistence("db_file")



@app.route('/create', methods=["POST"])
def create_team():
    input_json = request.get_json(force=True)
    persistance.save(input_json)
    return "200"

@app.route('/receive-alert/<teamId>')
def receive_alert(teamId):
    team = persistance.get_team(teamId)
    print(team)
    developer = team["developers"][0]["phone_number"]
    NotificationService.send_message("Sending Message",developer)
    return "200-Notification-Sent-to-"+str(developer)

    
app.run()