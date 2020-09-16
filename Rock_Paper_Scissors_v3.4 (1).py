from random import randint
from enum import Enum

names = ['Jón', 'Sigurður', 'Guðmundur', 'Gunnar', 'Ólafur', 'Einar', 'Kristján', 'Magnús', 'Stefán', 'Jóhann', 'Björn', 'Arnar', 'Árni', 'Bjarni', 'Helgi', 'Halldór', 'Pétur', 'Daníel', 'Kristinn', 'Ragnar', 'Gísli', 'Þorsteinn', 'Guðjón', 'Aron', 'Sveinn', 'Róbert', 'Páll', 'Óskar', 'Birgir', 'Davíð', 'Andri', 'Alexander', 'Viktor', 'Bjarki', 'Tómas', 'Haukur', 'Jóhannes', 'Ágúst', 'Karl', 'Ásgeir', 'Brynjar', 'Benedikt', 'Haraldur', 'Atli', 'Kjartan', 'Sigurjón', 'Friðrik', 'Baldur', 'Þórður', 'Hilmar', 'Kristófer', 'Kári', 'Hörður', 'Rúnar', 'Jónas', 'Egill', 'Eiríkur', 'Sindri', 'Björgvin', 'Sævar', 'Guðni', 'Elvar', 'Hlynur', 'Sverrir', 'Örn', 'Ómar', 'Ari', 'Ísak', 'Ingvar', 'Jakob', 'Snorri', 'Dagur', 'Reynir', 'Ingólfur', 'Matthías', 'Ívar', 'Arnór', 'Anton', 'Hafsteinn', 'Birkir', 'Garðar', 'Þórarinn', 'Eyþór', 'Axel', 'Þórir', 'Grétar', 'Tryggvi', 'Emil', 'Steinar', 'Valdimar', 'Vilhjálmur', 'Mikael', 'Ingi', 'Hjalti', 'Hákon', 'Adam', 'Hermann', 'Hjörtur', 'Aðalsteinn', 'Gunnlaugur']
bot_list_two = []
winners = []


class Bot:
    def __init__(self,name,shoot):
        self.name = name
        self.shoot = shoot

total_bots = int(input('Enter number of games: '))
game_list = []

def create_games():
    for num in range(total_bots):
        bot_one = Bot(names[randint(0,99)],randint(1,3))
        bot_two = Bot(names[randint(0,99)],randint(1,3))
        for x in range(1):
            if bot_one.shoot == 1:
                bot_one_str = 'rock'
            elif bot_one.shoot == 2:
                bot_one_str = 'paper'
            else:
                bot_one_str = 'scissors'
        for x in range(1):
            if bot_two.shoot == 1:
                bot_two_str = 'rock'
            elif bot_two.shoot == 2:
                bot_two_str = 'paper'
            else:
                bot_two_str = 'scissors'
        bot_details = [bot_one.name, bot_one.shoot,bot_one_str,bot_two.name,bot_two.shoot,bot_two_str]
        game_list.append(bot_details)


def play_game():
    global game_list
    global winners
    while len(game_list) > 0:
        for game in game_list:
            if game[1] == game[4]:
                print(f'Bot {game[0]} plays {game[2]}')
                print(f'Bot {game[3]} plays {game[5]}')
                print('Draw!')
                bot_one = Bot(names[randint(0,99)],randint(1,3))
                bot_two = Bot(names[randint(0,99)],randint(1,3))
                for x in range(1):
                    if bot_one.shoot == 1:
                        bot_one_str = 'rock'
                    elif bot_one.shoot == 2:
                        bot_one_str = 'paper'
                    else:
                        bot_one_str = 'scissors'
                for x in range(1):
                    if bot_two.shoot == 1:
                        bot_two_str = 'rock'
                    elif bot_two.shoot == 2:
                        bot_two_str = 'paper'
                    else:
                        bot_two_str = 'scissors'
                game.pop(1)
                game.pop(1)
                game.pop(2)
                game.pop(2)
                game.insert(1,bot_one.shoot)
                game.insert(2,bot_one_str)
                game.append(bot_two.shoot)
                game.append(bot_two_str)
                play_game()
            elif game[1] == 1 and game[4] == 2:
                print(f'Bot {game[0]} plays {game[2]}')
                print(f'Bot {game[3]} plays {game[5]}')
                print(f'Bot {game[3]} wins!')
                del(game[0:3])
                winners.append(game[0])
                del(game[0:3])
                print(game_list)
                print(winners)
                games = [x for x in game_list if x != []]
                game_list = games
            elif game[1] == 1 and game[4] == 3:
                print(f'Bot {game[0]} plays {game[2]}')
                print(f'Bot {game[3]} plays {game[5]}')
                print(f'Bot {game[0]} wins!')
                del(game[3:6])
                winners.append(game[0])
                del(game[0:3])
                print(game_list)
                print(winners)
                games = [x for x in game_list if x != []]
                game_list = games
            elif game[1] == 2 and game[4] == 1:
                print(f'Bot {game[0]} plays {game[2]}')
                print(f'Bot {game[3]} plays {game[5]}')
                print(f'Bot {game[0]} wins!')
                del(game[3:6])
                winners.append(game[0])
                del(game[0:3])
                print(game_list)
                print(winners)
                games = [x for x in game_list if x != []]
                game_list = games
            elif game[1] == 2 and game[4] == 3:
                print(f'Bot {game[0]} plays {game[2]}')
                print(f'Bot {game[3]} plays {game[5]}')
                print(f'Bot {game[3]} wins!')
                del(game[0:3])
                winners.append(game[0])
                del(game[0:3])
                print(game_list)
                print(winners)
                games = [x for x in game_list if x != []]
                game_list = games
            elif game[1] == 3 and game[4] == 1:
                print(f'Bot {game[0]} plays {game[2]}')
                print(f'Bot {game[3]} plays {game[5]}')
                print(f'Bot {game[3]} wins!')
                del(game[0:3])
                winners.append(game[0])
                del(game[0:3])
                print(game_list)
                print(winners)
                games = [x for x in game_list if x != []]
                game_list = games
            elif game[1] == 3 and game[4] == 2:
                print(f'Bot {game[0]} plays {game[2]}')
                print(f'Bot {game[3]} plays {game[5]}')
                print(f'Bot {game[0]} wins!')
                del(game[3:6])
                winners.append(game[0])
                del(game[0:3])
                print(game_list)
                print(winners)
                games = [x for x in game_list if x != []]
                game_list = games
            break
    # if len(game_list) == 0:
    #     for winner in winners:
    #         print(winner)

def main_loop():
    create_games()
    play_game()


main_loop()
# def create_bots():
#     for num in range(int(Bots.total_bots/2)):
#         bot_one = names[randint(0,99)]
#         bot_two = names[randint(0,99)]
#         shoot_one = randint(1,3)
#         shoot_two = randint(1,3)
#         shoot_one_str = ''
#         shoot_two_str = ''
#         bot_list_two.append([bot_one])
#         bot_list_two.append([bot_two])
    #     for shoot in range(shoot_one):
    #         if shoot == 1:
    #             shoot_one_str = 'rock'
    #         elif shoot == 2:
    #             shoot_one_str = 'paper'
    #         else:
    #             shoot_one_str = 'scissors'
    #     for shoot in range(shoot_two):
    #         if shoot == 1:
    #             shoot_two_str = 'rock'
    #         elif shoot == 2:
    #             shoot_two_str = 'paper'
    #         else:
    #             shoot_two_str = 'scissors'
    #     print(f'\nbot {bot_one} plays {shoot_one_str}')
    #     print(f'bot {bot_two} plays {shoot_two_str}\n')
    #     if shoot_one == shoot_two:
    #         print('Draw!')
    #     elif shoot_one == 1 and shoot_two == 2:
    #         print(f'bot {bot_two} wins!')
    #         winners.append(bot_two)
    #     elif shoot_one == 1 and shoot_two == 3:
    #         print(f'bot {bot_one} wins!')
    #         winners.append(bot_one)
    #     elif shoot_one == 2 and shoot_two == 1:
    #         print(f'bot {bot_one} wins!')
    #         winners.append(bot_one)
    #     elif shoot_one == 2 and shoot_two == 3:
    #         print(f'bot {bot_two} wins!')
    #         winners.append(bot_two)
    #     elif shoot_one == 3 and shoot_two == 1:
    #         print(f'bot {bot_two} wins!')
    #         winners.append(bot_two)
    #     elif shoot_one == 3 and shoot_two == 2:
    #         print(f'bot {bot_one} wins!')
    #         winners.append(bot_one)
    # for winner in bot_list_two:
    #     if winner not in winners:
    #         bot_list_two.remove(winner)


# def game():
#     for shoot in range(Bots.shoot_one):
#         if shoot == 1:
#             Bots.shoot_one_str = 'rock'
#         elif shoot == 2:
#             Bots.shoot_one_str = 'paper'
#         else:
#             Bots.shoot_one_str = 'scissors'
#     print(f'\nbot {Bots.bot_one} plays {Bots.shoot_one_str}')
#     print(f'bot {Bots.bot_two} plays {Bots.shoot_two_str}\n')
#     if Bots.shoot_one == Bots.shoot_two:
#         print('Draw!')
#     elif Bots.shoot_one == 1 and Bots.shoot_two == 2:
#         print(f'bot {Bots.bot_two} wins!')
#         winners.append(Bots.bot_two)
#     elif Bots.shoot_one == 1 and Bots.shoot_two == 3:
#         print(f'bot {Bots.bot_one} wins!')
#         winners.append(Bots.bot_one)
#     elif Bots.shoot_one == 2 and Bots.shoot_two == 1:
#         print(f'bot {Bots.bot_one} wins!')
#         winners.append(Bots.bot_one)
#     elif Bots.shoot_one == 2 and Bots.shoot_two == 3:
#         print(f'bot {Bots.bot_two} wins!')
#         winners.append(Bots.bot_two)
#     elif Bots.shoot_one == 3 and Bots.shoot_two == 1:
#         print(f'bot {Bots.bot_two} wins!')
#         winners.append(Bots.bot_two)
#     elif Bots.shoot_one == 3 and Bots.shoot_two == 2:
#         print(f'bot {Bots.bot_one} wins!')
#         winners.append(Bots.bot_one)
#     for winner in bot_list_two:
#         if winner not in winners:
#             bot_list_two.remove(winner)




# def new_round():
#     print('=========================================================')
#     for bot_one,bot_two in zip(bot_list_two[0::2], bot_list_two[1::2]):
#         shoot_one = randint(1,3)
#         shoot_two = randint(1,3)
#         print(bot_one,shoot_one,bot_two,shoot_two)


# game()
# new_round()