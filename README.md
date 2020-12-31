# integration-exercise
Integration of public senator info XML (via HTTP) to console print of JSON info.

Data source: https://www.senate.gov/general/contact_information/senators_cfm.xml

Setup
----------
0. Pre-reqs: you have Python 3 and Chrome.
1. Clone this repo or download the files as a zip.
<br>1.1 If zip, uncompress the files.
2. From the directory where these files now live, from the command line run `python -m pip install -r requirements.txt` (or `python3 -m pip install -r requirements.txt` if you have multiple versions of python in your env. I recommend a clean venv with only python3)
3. Run `python extract.py` . As mentioned at #2, if you have multiple python versions, run `python3 extract.py`. (Again, I recommend a clean venv)
<br>
Requirements.txt file includes following module dependencies:<br>
<ul>
	<li>selenium</li>
	<li>webdriver_manager</li>
</ul>

Run
----------
`python extract.py` to run

Caveats
----------
<ul>
<li>This is a first working version created in ~3 hours, as requested. In the interest of time, this script uses selenium to work around access issues on the senate.gov site met when using 'requests' or 'urllib' modules. It requires Chrome in order to run the Chrome driver. This essentially like taking a nuke to an ant, but for the home computer this was sufficient for the task.</li>

<li>The initial request outlined the following JSON format for each member in the XML: <br>
```json
{
    "firstName": <first name>,
    "lastName": <last name>,
    "fullName": <full name>,
    "chartId": <bioguide_id>,
    "mobile": <phone>, 
    "address": [
    {
    	"street": <street>,
	"city": <city>,
        "state": <state>,
        "zip": <zip>
    ]
}
```
  
Given the open curly brace within the address array and no closing curly brace, I would clarify with the requestor whether they wanted an object or array for the address, and whether they wanted the array to be of objects for each field, or allow for multiple address objects but in priority order (in the array). Again, in the interest of time, I created an array for the address field with objects for each field, given that the data only has one address per member. Format is as follows:
<br>
```json
{
    "member0": 
    {
    	"firstName": "Lamar",
	"lastName": "Alexander",
	"fullName": "Lamar Alexander",
	"chartId": "A000360",
	"mobile": "(202) 224-4944",
	"address": 
	[
	    {
	    	"street": "455 Dirksen Senate Office Building"
	    }, 
	    {
	    	"city": "Washington"
	    }, 
	    {
	        "state": "DC"
	    }, 
	    {
	    	"zip": "20510"
	    }
	]
    },
    ...
    "member99": 
    {
    ...
    }
}
``` 
</li>
  
<li>With the "member0" key following suit from member0 to member99.</li>
  

