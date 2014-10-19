API Error Codes
===============

This is a list of received errors and an attempt to document what they are or what they might mean.

```json
{"success":false,"errorCode":1,"errorMessage":"Authentication failed."}
```

Error:  1
Type:	Authentication failure
Notes:	Deliberately produced with a browser.


```json
{"success":false,"errorCode":5,"errorMessage":" error occured while trying to get balance."}
```

Error:  5
Type:	unknown
Notes:	Implies that authentication method works, but something else broke.

