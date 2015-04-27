Python-BTCMarkets
=================

Python toolkit/scripts for accessing the btcmarkets.net RESTful API.


Licensing
---------

This code is freely available under the terms of the GNU General Public License version 3, or any later version.  If you find it useful, please consider a Bitcoin donation to 1EUHUZXEA1QKqrHLjAtJj65BaXg1jwE1gm.

If you wish to use my code in a library or other application and the GPL is unsuitable for that purpose, I will consider multi-licensing it under the LGPL or one of the BSD variants (a modified 3-clause is the most likely).  Some other licenses may be considered, please contact me directly to discuss those terms.  Bribing me with BTC is quite acceptable.


Requirements
------------

This code is written for Python 3.2 and above, but developed with Python 3.4.  There is a reasonable chance it will also work with Python 2.7.

The [Requests](http://docs.python-requests.org/en/latest/) module is required to run this code.


Project Status
--------------

Anonymous connections (i.e. the tickers) work without any real issues.  API calls requiring authentication presently do not work as the current API expects POST requests to list variables in an explicit order, whereas Python does not assign an explicit order when constructing a POST URL from dict/JSON data.  This adversely affects the output of the digital signature on the authentication request and subsequently causes the authentication step to fail.



