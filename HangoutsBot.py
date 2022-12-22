from httplib2 import Http
from json import dumps
import requests

print("HangoutsBot imported")

#Example: https://developers.google.com/hangouts/chat/quickstart/incoming-bot-python
############################# HANGOUTS WEBHOOK ##############################


class HangoutsBot():

    #https://stackoverflow.com/questions/49439731/how-can-a-webhook-identify-user-ids
    Support3DTeamUserIDs = {'aleksandar.hadzhiev':'<users/105272443620590577621>',
                            'aleksandar.kasabov': '<users/116333548985285669379>',
                            'hristo.dimitrov':'<users/109833245242865843122>',
                            'martin.minev':'<users/113456293186318364039>',
                            'miroslav.ivanov': '<users/103372390219944596099>',
                            'nikolay.kusht':'<users/105163962452475145485>',
                            'nikoleta.garkova':'<users/104858849319908772173>',
                            'slavcho.brusev':'<users/115831071845174297654>',
                            'svetlozar.draganov':'<users/111789657070533885204>',
                            'tashko.zashev':'<users/103477451417875256728>',
                            'tsvetomira.girginova':'<users/102400157664256842257>',
                            'viktoria.dimitrova':'<users/114844540734016996195>',
                            'zahari.ivanov':'<users/101941789208682303621>',
                            'zdravko.keremidchiev':'<users/117450412146284728109>'}


    Support3DTeam = {'aleksandar.hadzhiev':'https://chat.googleapis.com/v1/spaces/wOqoTAAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=KrusRPuei0cydOgra3chUc_EcVxSSDaq5mVNS7I2eAA%3D',
                    'aleksandar.kasabov': 'https://chat.googleapis.com/v1/spaces/4WZpygAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=rOmWBvi0JtHA4WBNIOl4VxwlsakK3ARwZ80W1tgyF3g%3D',
                    'hristo.dimitrov':'https://chat.googleapis.com/v1/spaces/kSiCNAAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=tPvDj6ftui3-F0oxiHFycXVHHCSevN0qfzOZjhITdt8%3D',
                    'martin.minev':'https://chat.googleapis.com/v1/spaces/r9y31AAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=jIVIUvxiV9sdLJRrAaMhyTplbsWNJBae2SBD-_uZxSM%3D',
                    'miroslav.ivanov': 'https://chat.googleapis.com/v1/spaces/2si1NAAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=onEQ666bJiOFVrSrGPbCx3vwl_3QeYeZ2C3mXaWQMPA%3D',
                    'nikolay.kusht':'https://chat.googleapis.com/v1/spaces/667mNAAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=GU7NWkNzC23Q0jRlOBSAHHd2VemJDyJarh9A-rJ3Yms%3D',
                    'nikoleta.garkova':'https://chat.googleapis.com/v1/spaces/ukA0BgAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=DQTQLLtL9iiQWKLhfCoH376dorbknYBbtmH0Y-SlCDI%3D',
                    'slavcho.brusev':'https://chat.googleapis.com/v1/spaces/iCiXbAAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=TxVUJOofqfdXYSZ4FXDjsYk4O-HOrdCUqCso8casKTQ%3D',
                    'tashko.zashev':'https://chat.googleapis.com/v1/spaces/5JhjNAAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=w4rxYODF0JJOXBuMmfTvwpFCYX9xLLkZ65Ii4bavkSA%3D',
                    'tsvetomira.girginova':'https://chat.googleapis.com/v1/spaces/rPWNBgAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=TlJksfkjXRrNO1pForzz2H2Lgi-OZ3xe9qw0_FR7OwQ%3D',
                    'viktoria.dimitrova':'https://chat.googleapis.com/v1/spaces/2-nx_AAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=LWYE0kyll7yOMVJQ2GlcGupI6SHN4TVlr73W7oK3SZ4%3D',
                    'zahari.ivanov':'https://chat.googleapis.com/v1/spaces/tk53XAAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=H1yfAsmlJKaOiP_B95N7_d4vRKjA1GY9aNYA6Xg8Uqc%3D',
                    'zdravko.keremidchiev':'https://chat.googleapis.com/v1/spaces/lxEH1AAAAAE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=uD8nwL_SoTq2sIpF4JmaM-hSFfO4W-UDbih1R7i2V2o%3D',
                    '3D-Support-Room':'https://chat.googleapis.com/v1/spaces/AAAAaBs3S14/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=I_ro74_GpJQxDNYfI6-es32iXLuBR1x0jUegmLFM14Y%3D',
                    'PythonToHangouts':'https://chat.googleapis.com/v1/spaces/AAAANzSkXVM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=rTK-IVzBssAVdPgUED30qEHadcvCHjPJ-wS5C9mFw8Q%3D'
                    }

    def __init__(self):
        # print(HangoutsBot.Support3DTeam)
        pass


    def send_message(self, person, msg):

        print(person, msg)
        #webhook URL, you can get this from room > configure webhooks
        #3D Support Icon: http://ftp.chaosgroup.com/support/screenshots/3D_Support_Icon_128x128.jpg


        url = HangoutsBot.Support3DTeam[person]
        
        bot_message = {
            'text' : msg}

        message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

        http_obj = Http()

        response = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )

        print(response)


instance = HangoutsBot()


##if __name__ == '__main__':
##
##    hangouts_bot = HangoutsBot()
##    hangouts_bot.send_message("PythonToHangouts", "this is a test message")
##    
  
