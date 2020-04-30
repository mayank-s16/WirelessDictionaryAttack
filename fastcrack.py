import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-p", "--passphrase", dest = "passphrase", help = "Wordlist path")
    parser.add_option("-d", "--device", dest = "device", help = "Device ID")
    parser.add_option("-x", "--handshake", dest = "hccpax_file", help = "Handshake file with .hccapx extension")
    (options, arguments) = parser.parse_args()

    if not options.passphrase:
        parser.error("Please specify dictionary using -p option")
    elif not options.device:
        parser.error("Please specify Device ID using -d option")
    elif not options.hccpax_file:
        parser.error("Please specify hccpax file using -h option")
    return options

def run(device, hccpax_file, passphrase):
    subprocess.call("hashcat64.exe -m 2500 -d " + device + " " + hccpax_file + " " + passphrase, shell = True)

options = get_arguments()
run(options.device, options.hccpax_file, options.passphrase)