# Get Started
### Modules Used
os, sys, csv, requests (may require `pip install requests` if not previously installed) ,dotenv ( may require `pip install python-dotenv` if not previously installed)

### API_KEY
In order to use the API, you'll need to generate an API key that will be associated with your user. You can do this through the Snipe-IT web interface, by going to your account dropdown in the top right and clicking on "Manage API Keys". (Source: https://snipe-it.readme.io/reference/generating-api-tokens)
![Alt text](/GET%20API%20KEY.png)

If wanting to modify the program here is the API Documentation as well: https://snipe-it.readme.io/reference/api-overview

### BASE_URL
The BASE_URL is can be found on the right of the active API keys in the same menu of 'Manage API Keys'. Note: The base URL Needs to have '/' at the end and not contain `<endpoint>` on the URL. (The URL snipe gives you ends with `<endpoint>`)

When you have both the `API_KEY` & `BASE_URL` make a `.env` file and make a variable for each. The program makes the environment variables usable automatically no need to worry about add them to your system.

# Check_in/Check_out
## status_id codes:
    1: in repair
    2: ready to deploy
    3: archived
    4: missing/lost/stolen
    5: disposed 

## Arguments for CSV
### If wanting to check out to asset use the following:
    |  asset_to_check_out  |  check_out_to   |
    |    AssetTag/####     |  AssetTag/####  |

### If wanting to check out to user use the following:
    |  asset_to_check_out  |  check_out_to  |
    |    AssetTag/####     |    username    |

### If wanting to check in use the following:
    |  asset_to_check_in  |    status_id     |
    |    AssetTag/####    |  status_id(1-5)  |

### Note on User Search
When doing the csv to check out to a user the `assigned_user` column needs to be filed out with the username of the user that will be checked out to not the name. (This is because of 2 reasons: IT team is duplicate so name search gives multiple results and in case only first name is inputed in field there might be multiple people with it so a unique username is easier to deal with multiple results from search.)

# Passing CSV File
    python snipe_update.py action /path/to/file.csv
To pass the file to the program put the file path as an argument when running the program. Like shown above. Action can either be `check_in`, `check_out_to_user` or `check_out_to_asset`.