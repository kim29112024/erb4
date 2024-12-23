import json
from listings.models import Listing
from realtors.models import Realtor

with open('listings.json') as f:
    listings_json = json.load(f)
for listing in listings_json:
    listing = Listing(
        realtor = listing['realtor'],
        title = listing['title'],
        address = listing['address'],
        street = listing['street'],
        district = listing['district'],
        description = listing['description'],
        price = listing['price'],
        bedrooms = listing['bedrooms'],
        bathrooms = listing['bathrooms'],
        clubhouse = listing['clubhouse'],
        sqft = listing['sqft'],
        estate_size = listing['estate_size'],
        is_published = listing['is_published'],
        list_date = listing['list_date'],
        photo_main = listing['photo_main'],
        photo_1 = listing['photo_1'],
        photo_2 = listing['photo_2'],
        photo_3 = listing['photo_3'],
        photo_4 = listing['photo_4'],
        photo_5 = listing['photo_5'],
        photo_6 = listing['photo_6']
    )
    listing.save()