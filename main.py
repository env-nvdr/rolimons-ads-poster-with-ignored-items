import random
import time
import os
import requests
import json
import sys
from rich import print

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

player_id = config["PlayerData"]["PlayerId"]
roli_verification = config["PlayerData"]["Roli_token"]
ignored_ids = set(config["ItemsIgnored"]["ItemsIds"])
available_tags = config["Trades"]["Tags"]
Waitmin = config["Trades"]["WaitTime"]["Min"]
Waitmax = config["Trades"]["WaitTime"]["Max"]

session = requests.Session()
session.cookies.update({"_RoliVerification": roli_verification})

def get_username(user_id: int) -> str:
    url = f"https://users.roblox.com/v1/users/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("name", "Unknown")
    except Exception as e:
        print(f"Failed to fetch username for ID {user_id}: {e}")
        return "Unknown"

def fetch_items() -> list[int]:
    while True:
        inventory = session.get(
            f"https://inventory.roblox.com/v1/users/{player_id}/assets/collectibles?limit=100"
        ).json()

        if data := inventory.get("data"):
            items = [i["assetId"] for i in data if i["assetId"] not in ignored_ids]

            if not items:
                print("[bold red]ERROR[/] All items are blocked — update your ItemsIgnored > ItemsIds list")
                time.sleep(60)
                continue

            return items if len(items) <= 4 else random.sample(items, 4)

        print("[bold red]ERROR[/] Error fetching inventory. Retrying in 1 minute")
        time.sleep(60)

def post_ad(item_ids: list[int]) -> None:
    random_tags = random.sample(available_tags, 4)

    for _ in range(3):
        try:
            req = session.post(
                "https://api.rolimons.com/tradeads/v1/createad",
                json={
                    "player_id": player_id,
                    "offer_item_ids": item_ids,
                    "request_item_ids": [],
                    "request_tags": random_tags
                }
            )
            res = req.json()

            if res.get("success"):
                print(f"[bold green]SUCCESS[/] Ad posted {item_ids} - {random_tags}")
                return
            else:
                print(f'[bold red]ERROR[/] Could not post ad (Reason: {res.get("message")})')
                break
        except Exception as e:
            print(f"[bold red]ERROR[/] Exception while posting ad: {e}")
            time.sleep(5)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Welcome, [bold blue] {get_username(player_id)} [/]!")
    while True:
        items = fetch_items()
        post_ad(items)

        random_time = random.randint(Waitmin, Waitmax)
        for remaining in range(random_time, 0, -1):
            print(f"Waiting {remaining} minutes before attempting to post another ad", end="\r")
            time.sleep(60)
        print(" " * 70, end="\r")

if __name__ == "__main__":
    if Waitmin < 15 :
        print(f'[bold red]ERROR[/] Waitmin should be 15 or higher, check your config.json.')
        sys.exit()
    main()