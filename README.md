# integration-exercise
Integration of public senator info XML (via HTTP) to console print of JSON info.

Data source: https://www.senate.gov/general/contact_information/senators_cfm.xml

Setup
----------
Clone this repo for extract.py file
<br>
Requirements.txt file includes following module dependencies:
`selenium
webdriver_manager
xml
json`

Run
----------
`python extract.py` to run

Caveats
----------
This is a first working version created in ~3 hours, as requested. In the interest of time, this script uses selenium to work around access issues on the senate.gov site met when using 'requests' or 'urllib' modules. It requires Chrome in order to run the Chrome driver. This essentially like taking a nuke to an ant, but for the home computer this was sufficient for the task.

The initial request outlined the following JSON format for each member in the XML: <br>
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
  
  With the "member0" key following suit from member0 to member99.
  

