# Course Utilities
## Wyatt Evans (Iowa State University)

### ScopeCap (Command line oscilloscope capture utility for Keysight/Agilent instruments)
ScopeCap is a command line utility tested to be compatible with Windows 11 and Linux systems.
The utility automatically detects connected USB oscilloscopes, then depending on the detected OS, it queries the current image data from the oscilloscope, saving it to a specified output file.
Dependencies: Pyvisa, pyvisa-py, pyusb, libusb1
Steps:
- If on a Windows device, set the default program for opening python files to Python.
- (OPTIONAL) Add to PATH; on ISU lab computers, you can edit your account-specific PATH environment variable.
- From the directory of the python file (Or wherever you want to save the png if added to PATH), run scopecap (if in PATH) or ./scopecap.py, appending the desired output filename.
Example: scopecap output.png (puts output.png into current directory), ./scopecap.py $HOME/Pictures/scopecaptures/output.png


This program was implemented by the Iowa State University Electronics Technology Group for the lab utilities package "ETG Lab Tools" in 2026.

