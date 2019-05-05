### Special instructions for __Digitale Hovedstrømninger__

The TEI-encoded texts of Brandes' __Hovedstrømninger__ can be quite easily 
imported and indexed for concordance, KWIC, co-occurrence and time-series 
searching and visualization with Philologic 4.6.

This forked repository differs from the stock Philologic 4.6 software only by 
the presence of the `corpora/brandes/` folder, which contains the configuration
files and very slightly modified versions of the TEI-encoded 
__Hovedstrømninger__ texts (see below) that should be used to provision the 
site, and in two minor code edits necessary to extend the Philologic 
dictionary-word lookup functionality (accessed by highlighting a word in the 
concordance or KWIC views and then pressing "d") to use the 1700-1950 Danish 
historical dictionary.

## Modified installation

To make use of the dictionary-lookup modifications (see above), it is advised
to clone this repository and then follow the standard installation instructions
from the [documentation](https://artfl-project.github.io/PhiloLogic4/).
As an alternative, one simply could install the the stock 4.6 version and then
manually apply the code changes from this commit.

**Install notes:** The installation instructions and system requirements are
the same as for the stock Python3 Philologic 4.6 software. The most common 
complications tend to arise from the use of the `#!/usr/bin/env python3`
initial line in the Python scripts, which older systems may not support, in
which case a global search-and replace may be necessary to replace it with
the direct path to the system's Python3 executable. Also, some extra work to
install and configure all of the necessary Python libraries and Apache modules
may be needed, especially on unsupported systems like Mac OS.

**Post-install:** As stated in the instructions, the 
`/etc/philologic/philologic4.cfg` file should be updated with the proper
settings for the server and site. 

## Modified database (text) loading and configuration steps

The XML files in `corpora/brandes/` have been modified slightly via the
addition of a `<year>` tag, which supplies the database loader with the
information needed to populate the time-series search facet. Specifically,
this tag resides at `<teiHeader><fileDesc><sourceDesc><bibl><year>` (although
other locations are also acceptable).

To load these files into the Philologic4 installation, cd to the
`corpora/brandes/` folder and run
`$ philolad philoload4 -l load_config.py brandes ./*.xml

After the files have been loaded, be sure to copy the `web_config.cfg` file
from `corpora/brandes/` to the `data/` folder in the main Philologic site
install folder; by default this will be something like 
`/var/www/html/philologic/brandes/data/'. The site should now be ready for use.

===========

![alt text](www/app/assets/img/philo.png) 4.6

===========


PhiloLogic is an XML database/search engine/web app that is designed
for the particular difficulties of TEI XML.  For a more theoretical
description, you can refer to [our research publications](http://http://jtei.revues.org/817) or [our blog](http://artfl.blogspot.com).

**_The master branch refers to the new Python3 version of PhiloLogic. For the old Python2 version, refer to here:_**
_https://github.com/ARTFL-Project/PhiloLogic4/tree/PhiloLogic4.5_

### See [documentation](https://artfl-project.github.io/PhiloLogic4/)

### IMPORTANT ###
* PhiloLogic4.6 will only work on Unix-based systems (Linux, *BSD) though MacOS is not supported and guaranteed to work.
* PhiloLogic4.6 will only run on the Apache Webserver
* PhiloLogic4.6 needs to run on Python 3.6 and up. For a Python 2 version, use the [latest PhiloLogic 4.5 release](https://github.com/ARTFL-Project/PhiloLogic4/releases/tag/v4.5.9).
* The PhiloLogic4.6 Web App will only work on recent versions of web browsers: Chrome, Firefox, Safari, Opera, Edge. No support for Internet Explorer.
