# Rolimons Auto Ad Poster

This script automatically posts trade ads to [Rolimons](https://www.rolimons.com/) using your Roblox collectibles. It fetches eligible items from your inventory and rotates them in trade ads with randomized tags and delays.


## Features

- Fetches collectibles from your Roblox inventory  
- Ignores items specified in the config  
- Posts ads with randomized tags from your list  
- Waits a random time between ad posts  
- Automatically retries if inventory or ad post fails  


## Requirements

Install required Python libraries:

```bash
pip install -r requirements.txt
```

## Config

```json
{
    "PlayerData":
    {
        "PlayerId": 1231231,
        "Roli_token": "token here"
    },

    "Trades":
    {
        "Tags":["any", "demand", "robux", "upgrade", "downgrade"],
        "WaitTime":
        {
            "Min": 15,
            "Max": 19
        }
    },

    "ItemsIgnored":
    {
        "ItemsIds":[123123123]
    }
}
```

```PlayerData.PlayerId```: Your Roblox user ID

```PlayerData.Roli_token```: Your _RoliVerification cookie from rolimons.com

```Trades.Tags: List of tags``` that will be randomly attached to trade ads

```Trades.WaitTime.Min / Max```: Delay range (in minutes) between each ad post

```ItemsIgnored.ItemsIds```: List of asset IDs to ignore when posting ads

## How to Use

- Make sure config.json is filled correctly
- Install dependencies
- Run the script:

```bash
python3 main.py
```
- or 
```bash
python main.py
```

## How It Works
- Loads your inventory and filters out ignored items
- Randomly picks up to 4 items to post in a trade ad
- Selects 4 random tags from your list
- Posts the ad to Rolimons
- Waits a random amount of time before repeating

## Disclaimer
- This tool is for educational purposes only.
- Using automated tools on Rolimons or Roblox may violate their terms of service.
- Use at your own risk.

## Original code 
    https://github.com/truffle-shuffle/rolimons-ad-poster
