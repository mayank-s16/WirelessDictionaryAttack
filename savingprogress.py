import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-s","--session", dest="session", help="Session name")
    parser.add_option("-p", "--passphrase", dest = "passphrase", help = "Wordlist path")
    parser.add_option("-m", "--mac", dest = "mac", help = "BSSID of access point")
    parser.add_option("-c", "--capfile", dest = "capfile", help = "Handshake file with .cap extension")
    (options, arguments) = parser.parse_args()

    if not options.session:
        parser.error("Please specify session name using -s or --session option")
    elif not options.passphrase:
        parser.error("Please specify wordlist file using -p or --passphrase option")
    elif not options.mac:
        parser.error("Please specify BSSID of access point")
    elif not options.capfile:
        parser.error("Please specify captured handshake file")

    return options

def run(session, passphrase, mac, capfile):
    john_command = "john --wordlist="+passphrase+" --stdout --session="+session
    piping_symbol = "|"
    aircrack_command = "aircrack-ng -w - -b "+mac+" "+capfile
    subprocess.call(john_command+" "+piping_symbol+" "+aircrack_command, shell = True)

options = get_arguments()
run(options.session, options.passphrase, options.mac, options.capfile)
