#!/usr/bin/env python3

# Read names and CPU status in S7 PLC's and save them in a txt file

import snap7.client as s7
from search import lookup
import sys
import optparse

def main():
    parser = optparse.OptionParser('Use: ' + sys.argv[0] +
                                   ' -c country -t city -p page search\
                                    -o output file')
    parser.add_option('-c', dest='coption', type='string',
                      help='Country to locate PLCs')
    parser.add_option('-t', dest='toption', type='string',
                      help='City to locate PLCs')
    parser.add_option('-o', dest='foption', type='string',
                      help='File to return data')
    parser.add_option('-p', dest='poption', type='int',
                      help='Page number of SHODAN search')
    (options, args) = parser.parse_args()
    if options.foption == None:
        print(parser.usage)
        exit(0)
    else:
        file_name = options.foption
    try:
        f_out = open(file_name, 'wb')
    except:
        print("Unable to save file: ", file_name)
        exit(0)
    if options.poption == None:
        page_s = 1
    else:
        page_s = options.poption

    plcs = lookup(country=options.coption, city=options.toption, page=page_s)
    for plc_c in plcs.results:
        # For each PLC
        try:
            plc = s7.Client()
            plc.connect(plc_c.ip,0,0)
            state = plc.get_cpu_state()
            info = plc.get_cpu_info()
            name = info.ModuleName.decode('utf8')
            cpu = info.ModuleTypeName.decode('utf8')
            plc.disconnect()
            cadena = plc_c.ip + '||' + name + '||' + cpu + '||' + state + '\n'
            print(cadena)
            f_out.write(cadena.encode('utf8'))
        except:
            pass
    f_out.close()

if __name__ == '__main__':
    main()
