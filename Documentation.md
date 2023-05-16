# Get Started
In order to use the API, you'll need to generate an API key that will be associated with your user. You can do this through the Snipe-IT web interface, by going to your account dropdown in the top right and clicking on "Manage API Keys". (Source: https://snipe-it.readme.io/reference/generating-api-tokens)
![Alt text](/GET%20API%20KEY.png)

If wanting to modify the program here is the API Documentation as well: https://snipe-it.readme.io/reference/api-overview

# Check in/Check out
## status_id codes:
    1: in repair
    2: ready to deploy
    3: archived
    4: missing/lost/stolen
    5: disposed 

## Arguments for CSV
### If wanting to check out to asset use the following:\
    |  asset_to_check_out  |   assign_type    |  check_out_to   |\
    |    AssetTag/####     |  'user','asset'  |  AssetTag/####  |

### If wanting to check out to user use the following:\
    |  asset_to_check_out  |   assign_type    |  check_out_to  |\
    |    AssetTag/####     |  'user','asset'  |    username    |

### If wanting to check in use the following:\
    |  asset_to_check_in  |    status_id     |\
    |    AssetTag/####    |  status_id(1-5)  |

### Notes on user search
When doing the csv to check out to a user the `assigned_user` column needs to be filed out with the username of the user that will be checked out to not the name. (This is because of 2 reasons: IT team is duplicate so name search gives multiple results and in case only first name is inputed in field there might be multiple people with it so a unique username is easier to deal with multiple results from search.)


