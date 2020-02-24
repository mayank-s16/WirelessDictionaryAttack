import optparse
import subprocess

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-r", "--restore", dest = "restore", help = "Existing session name")
    parser.add_option("-m", "--mac", dest = "mac", help ="BSSID of access point")
    parser.add_option("-c", "--capfile", dest ="capfile", help ="Handshake file in .cap format")

    (options, arguments) = parser.parse_args()
    if not options.restore:
        parser.error("Please specify existing session using -r or --restore option")
    elif not options.mac:
        parser.error("Please specify the BSSID of access point using -m or --mac option")
    elif not options.capfile:
        parser.error("Please specify cap file location using -c or --capfile option")
    return options

def run(restore, mac, capfile):
    john_command = "john --restore=" +restore
    piping_symbol = "|"
    aircrack_command = "aircrack-ng -w - -b " + mac + " "+capfile
    subprocess.call(john_command + " " + piping_symbol + " " + aircrack_command, shell = True)

options = get_arguments()
run(options.restore, options.mac, options.capfile)

