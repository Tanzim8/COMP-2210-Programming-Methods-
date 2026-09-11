games = []
def display_Games(games):
    for game in games:
        print(game["name"]+ "\n" + game["genre"] + "\n" + game["hours"] + "\n" + game["ratings"] )

def add_Games(games):
    game={}
    game["name"] = input("Enter game name: ")
    game["genre"] = input("Enter genre: ")
    game["hours"] = input("Enter hours played: ")
    game["ratings"] = input("Enter rating: ")
    while(len(game["name"])==0 or len(game["genre"])==0 or not game["hours"].isnumeric() or not game["ratings"].isnumeric() or int(game["ratings"])>10):
        game["name"] = input("Enter game name: ")
        game["genre"] = input("Enter genre: ")
        game["hours"] = input("Enter hours played: ")
        game["ratings"] = input("Enter rating: ")
    games.append(game)
