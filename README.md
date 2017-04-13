# s7-experiments
PLC Siemens S7 experiments using exposed devices and SNAP7

## Files:

### search.py 
Contains functions for devices searching using 
S7 Siemens communication protocol through SHODAN API (User required)

Configuration : Edit this file in order to use your API Key from SHODAN

### PLC_Names.py
Using SHODAN and SNAP7 lookup for PLC Names, CPU states and
type CPU's.

Use: 

<code>PLC_Names -c country -t city -p page search -o output file</code>
