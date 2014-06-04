Country Distances
=================

A simple script for computing distances between countries.  This queries 
[Geonames](http://www.geonames.org) to get a list of the most populous city 
in each country.  Then it uses the [geopy](http://github.com/geopy/geopy) 
library to compute the [Vincenty distance](https://en.wikipedia.org/wiki/Vincenty's_formulae) 
between each city.

For our puposes the most populous city was a reasonable proxy for the "location" 
of a country.  Another reasonable approach would be to use the geopgraphic centroid, 
but we didn't do that.

Installation
------------

This uses Python 2.7, so you need to install a few libraries first:
```
pip install requests
pip install geopy
pip install iso3166
```

Next copy `settings.cfg.template` to `settings.cfg` and put your Geonames username in there. 
You need a username to use their API, and uou can [sign up for one for free](http://www.geonames.org/login) 
(don't forget to enable API access on your preference page)

Running
-------

Simply run:
```
python get-biggest-cities.py
```
and it will generate a `distances.csv` file with the results.  These are keyed by each 
country's iso3166-alpha3 code.  The results are in Kilometers.
