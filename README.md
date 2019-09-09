# yadisclinkgen
Script generates direct file links (for your website integration) using https://getfile.dokpub.com/yandex service. This script uses preliminarily prepared Yandex.Disc public links to your files.

## REQUIREMENTS: 
_shared_ files located in a _shared_ Yandex.Disc folder
## HOW TO USE:
1. Create **input.txt** in a current folder and paste a link to a file (1 link per line)
2. Run the script
* To test whether generated links are valid, execute the script with ***--test*** option:
```
python yadisclinkgen.py --test
```
or
```
python yadisclinkgen.py -t
```
3. Direct file links stored in output.txt
