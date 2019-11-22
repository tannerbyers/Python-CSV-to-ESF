# Python CSV-to-ESF

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/tannerbyers/Python-CSV-to-ESF)

Python CSV-to-ESF is a simple, quick, offline, Python powered CSV to XML format generator for ESF files.

### Requirements
[Python 3](https://www.python.org/downloads/) is all that is needed to run.

### Installation & Running

```sh
$ git clone https://github.com/tannerbyers/Python-CSV-to-ESF
$ cd Python-CSV-to-ESF
```
Now you must add your Error code and Snip level to the EditsinCSV.csv file 

Sample Information: 

| Error Code | Snip Level |
|------------|------------|
| 0x393939ec | 2          |
| 0x393939ed | 4          |
|            |            |

Now run the below command: 
```
$ python main.py
```

#### ESF File Output (XML format)
![Screenshot of Result in Notepad++](https://i.ibb.co/CVsKZBv/screenshot.png)

### Todos

 - Create GUI
 - Add Encoding attribute to xml tag
 - Add Options (Remove all Snip.lvl)

