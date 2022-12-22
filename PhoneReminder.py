#Example: https://developers.google.com/hangouts/chat/quickstart/incoming-bot-python
############################# HANGOUTS WEBHOOK ##############################

#Example requests-login via windows-authentication:
#https://stackoverflow.com/questions/32305536/handling-windows-authentication-while-accessing-url-using-requests

import requests
import HangoutsBot
import pathlib
parrent_folder_path = pathlib.Path(__file__).parent.resolve()


class Asterisk():

    tagged_users = ''

    def __init__(self):

        #get credentials from file
        file_path = parrent_folder_path / "credentials.txt"
        f = open(file_path, "r")

        lines = f.readlines()
        for line in lines:
            if 'asterisk_url' in line:
                asterisk_url = line.split()[1]
                # print(asterisk_url)
            if 'asterisk_username' in line:
                asterisk_username = line.split()[1]
                # print(asterisk_username)
            if 'asterisk_password' in line:
                asterisk_password = line.split()[1]
                # print(asterisk_password)

        url = asterisk_url
        self.response = requests.get(asterisk_url, auth=(asterisk_username, asterisk_password))
        # print(self.response.content)

        status = self.response.content.splitlines()
        for item in status:
            # print(item)
            pass


    def check_phone_status(self):
        
        if b"9017/9017 OK" in self.response.content:
            print("9017: 3D Support is Online")
            #sendMsgToHangouts("PythonToHangouts")
        else:
            print("9017: 3D Support is Offline")


        if b"2010/2010 OK" in self.response.content:
            print("2010: AEC Support is Online")
        else:
            print("2010: AEC Support is Offline")


        if b"9020/9020 OK" in self.response.content:
            print("9020: nikolay.kusht is Online")
        else:
            print("9020: nikolay.kusht is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['nikolay.kusht'] + "\n"
            Asterisk.tagged_users += 'nikolay.kusht' + "\n"
            #sendMsgToHangouts("nikolay.kusht")



        if b"9031/9031 OK" in self.response.content:
            print("9031: slavcho.brusev is Online")
        else:
            print("9031: slavcho.brusev is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['slavcho.brusev'] + "\n"
            Asterisk.tagged_users += 'slavcho.brusev' + "\n"
            #sendMsgToHangouts("slavcho.brusev")

        if b"9032/9032 OK" in self.response.content:
            print("9032: zahari.ivanov is Online")
        else:
            print("9032: zahari.ivanov is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['zahari.ivanov'] + "\n"
            Asterisk.tagged_users += 'zahari.ivanov' + "\n"
            #sendMsgToHangouts("zahari.ivanov")
            
            
        # if b"9033/9033 OK" in self.response.content:
        #     print("9033: miroslav.ivanov is Online")
        # else:
        #     print("9033: miroslav.ivanov is Offline")
        #     Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['miroslav.ivanov'] + "\n"
        #     #sendMsgToHangouts("miroslav.ivanov")


        if b"9034/9034 OK" in self.response.content:
            print("9034: tashko.zashev is Online")
        else:
            print("9034: tashko.zashev is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['tashko.zashev'] + "\n"
            Asterisk.tagged_users += 'tashko.zashev' + "\n"
            #sendMsgToHangouts("tashko.zashev")
            

        if b"9035/9035 OK" in self.response.content:
            print("9035: 'martin.minev is Online")
        else:
            print("9035: 'martin.minev is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['martin.minev'] + "\n"
            Asterisk.tagged_users += 'martin.minev' + "\n"
            #sendMsgToHangouts("'martin.minev")


        if b"9036/9036 OK" in self.response.content:
            print("9036: zdravko.keremidchiev is Online")
        else:
            print("9036: zdravko.keremidchiev is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['zdravko.keremidchiev'] + "\n"
            Asterisk.tagged_users += 'zdravko.keremidchiev' + "\n"
            #sendMsgToHangouts("zdravko.keremidchiev")


        if b"9038/9038 OK" in self.response.content:
            print("9038: nikoleta.garkova is Online")
        else:
            print("9038: nikoleta.garkova is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['nikoleta.garkova'] + "\n"
            Asterisk.tagged_users += 'nikoleta.garkova' + "\n"
            #sendMsgToHangouts("nikoleta.garkova")


        if b"9039/9039 OK" in self.response.content:
            print("9039: tsvetomira.girginova is Online")
        else:
            print("9039: tsvetomira.girginova is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['tsvetomira.girginova'] + "\n"
            Asterisk.tagged_users += 'tsvetomira.girginova' + "\n"
            #sendMsgToHangouts("tsvetomira.girginova")
            

        
        if b"9040/9040 OK" in self.response.content:
            print("9040: svetlozar.draganov is Online")
        else:
            print("9040: svetlozar.draganov is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['svetlozar.draganov'] + "\n"
            #sendMsgToHangouts("")
            

        if b"9041/9041 OK" in self.response.content:
            print("9041: viktoria.dimitrova is Online")
        else:
            print("9041: viktoria.dimitrova is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['viktoria.dimitrova'] + "\n"
            Asterisk.tagged_users += 'viktoria.dimitrova' + "\n"
            #sendMsgToHangouts("viktoria.dimitrova")
            

        if b"9042/9042 OK" in self.response.content:
            print("9042: aleksandar.kasabov is Online")
        else:
            print("9042: aleksandar.kasabov is Offline")
            # Asterisk.tagged_users += HangoutsBot.instance.Support3DTeamUserIDs['aleksandar.kasabov'] + "\n"
            Asterisk.tagged_users += 'aleksandar.kasabov' + "\n"
            #sendMsgToHangouts("aleksandar.kasabov")

    def print_tagged_users(self):
        print(Asterisk.tagged_users)
  

asterisk = Asterisk()
asterisk.check_phone_status()
asterisk.print_tagged_users()


if asterisk.tagged_users:
    # person = "3D-Support-Room"
    person = 'PythonToHangouts'
    msg = "*PHONE REMINDER* \n" + asterisk.tagged_users + "_PLEASE LAUNCH PHONE APPS_"

    HangoutsBot.instance.send_message(person, msg)
    ##HangoutsBot.instance.send_message("PythonToHangouts","test msg")
    

