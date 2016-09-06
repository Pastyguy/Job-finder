import os

## Price

# The minimum rent you want to pay per month.
MIN_PRICE = 1500

# The maximum rent you want to pay per month.
MAX_PRICE = 2000

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["eby", "sfc", "sby", "nby"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "petaluma": [
        [-122.683334, 38.205147],
        [-122.567355,38.298796],
    ],
    "seb": [
        [-122.848103, 38.383861],
        [-122.806802, 38.413065],
    ],
    "santa_rosa": [
        [-122.859421,38.356734],
        [-122.573025,38.529367],
    ],
    "rohnert_park": [
        [-122.755051,38.312299],
        [-122.65274,38.371809],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["santa rosa","santarosa", "sebastopol", "rohnert park", "cotati", "petaluma"]
##["berkeley north", "berkeley", "rockridge", "adams point", "oakland lake merritt", "cow hollow", "piedmont", "pac hts", "pacific heights", "lower haight", "inner sunset", "outer sunset", "presidio", "palo alto", "richmond / seacliff", "haight ashbury", "alameda", "twin peaks", "noe valley", "bernal heights", "glen park", "sunset", "mission district", "potrero hill", "dogpatch"]


## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "oakland_19th_bart": [37.8118051,-122.2720873]
	##,
    ##"macarthur_bart": [37.8265657,-122.2686705],
    ##"rockridge_bart": [37.841286,-122.2566329],
    ##"downtown_berkeley_bart": [37.8629541,-122.276594],
    ##"north_berkeley_bart": [37.8713411,-122.2849758]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'jjj'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#jobs"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass