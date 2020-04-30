import optparse
import subprocess

def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-l", "--minimum", dest = "minimum", help = "Minimum length")
    parser.add_option("-m", "--maximum", dest = "maximum", help ="Maximum length")
    parser.add_option("-c", "--charset", dest ="charset", help ="Character Set")
    parser.add_option("-b", "--bssid", dest ="bssid", help ="BSSID of Target")
    parser.add_option("-f", "--file", dest ="file", help ="Handshake file")

    (options, arguments) = parser.parse_args()
    if not options.minimum:
        parser.error("Please specify Minimum length using -l or --minimum option")
    elif not options.maximum:
        parser.error("Please specify Maximum length using -m or --maximum option")
    elif not options.charset:
        parser.error("Please specify character set using -c or --charset option")
    elif not options.bssid:
        parser.error("Please specify BSSID of target using -b or --bssid option")
    elif not options.file:
        parser.error("Please specify handshake file using -f or --file option")

    return options

def run(minimum, maximum, charset, bssid, file):
    crunch_command = "crunch " + minimum + " " + maximum + " " + charset
    piping_symbol = "|"
    aircrack_command = "aircrack-ng -b " + bssid + " -w - " + file
    subprocess.call(crunch_command + " " + piping_symbol + " " + aircrack_command, shell = True) 
    
options = get_arguments()
run(options.minimum, options.maximum, options.charset, options.bssid, options.file)