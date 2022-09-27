import random

states = [
    {
        "name": "Alabama",
        "capital": "Montgomery"
    }, {
        "name": "Alaska",
        "capital": "Juneau"
    },
    # {
    #     "name": "Arizona",
    #     "capital": "Phoenix"
    # }, {
    #     "name": "Arkansas",
    #     "capital": "Little Rock"
    # }, {
    #     "name": "California",
    #     "capital": "Sacramento"
    # }, {
    #     "name": "Colorado",
    #     "capital": "Denver"
    # }, {
    #     "name": "Connecticut",
    #     "capital": "Hartford"
    # }, {
    #     "name": "Delaware",
    #     "capital": "Dover"
    # }, {
    #     "name": "Florida",
    #     "capital": "Tallahassee"
    # }, {
    #     "name": "Georgia",
    #     "capital": "Atlanta"
    # }, {
    #     "name": "Hawaii",
    #     "capital": "Honolulu"
    # }, {
    #     "name": "Idaho",
    #     "capital": "Boise"
    # }, {
    #     "name": "Illinois",
    #     "capital": "Springfield"
    # }, {
    #     "name": "Indiana",
    #     "capital": "Indianapolis"
    # }, {
    #     "name": "Iowa",
    #     "capital": "Des Moines"
    # }, {
    #     "name": "Kansas",
    #     "capital": "Topeka"
    # }, {
    #     "name": "Kentucky",
    #     "capital": "Frankfort"
    # }, {
    #     "name": "Louisiana",
    #     "capital": "Baton Rouge"
    # }, {
    #     "name": "Maine",
    #     "capital": "Augusta"
    # }, {
    #     "name": "Maryland",
    #     "capital": "Annapolis"
    # }, {
    #     "name": "Massachusetts",
    #     "capital": "Boston"
    # }, {
    #     "name": "Michigan",
    #     "capital": "Lansing"
    # }, {
    #     "name": "Minnesota",
    #     "capital": "St. Paul"
    # }, {
    #     "name": "Mississippi",
    #     "capital": "Jackson"
    # }, {
    #     "name": "Missouri",
    #     "capital": "Jefferson City"
    # }, {
    #     "name": "Montana",
    #     "capital": "Helena"
    # }, {
    #     "name": "Nebraska",
    #     "capital": "Lincoln"
    # }, {
    #     "name": "Nevada",
    #     "capital": "Carson City"
    # }, {
    #     "name": "New Hampshire",
    #     "capital": "Concord"
    # }, {
    #     "name": "New Jersey",
    #     "capital": "Trenton"
    # }, {
    #     "name": "New Mexico",
    #     "capital": "Santa Fe"
    # }, {
    #     "name": "New York",
    #     "capital": "Albany"
    # }, {
    #     "name": "North Carolina",
    #     "capital": "Raleigh"
    # }, {
    #     "name": "North Dakota",
    #     "capital": "Bismarck"
    # }, {
    #     "name": "Ohio",
    #     "capital": "Columbus"
    # }, {
    #     "name": "Oklahoma",
    #     "capital": "Oklahoma City"
    # }, {
    #     "name": "Oregon",
    #     "capital": "Salem"
    # }, {
    #     "name": "Pennsylvania",
    #     "capital": "Harrisburg"
    # }, {
    #     "name": "Rhode Island",
    #     "capital": "Providence"
    # }, {
    #     "name": "South Carolina",
    #     "capital": "Columbia"
    # }, {
    #     "name": "South Dakota",
    #     "capital": "Pierre"
    # }, {
    #     "name": "Tennessee",
    #     "capital": "Nashville"
    # }, {
    #     "name": "Texas",
    #     "capital": "Austin"
    # }, {
    #     "name": "Utah",
    #     "capital": "Salt Lake City"
    # }, {
    #     "name": "Vermont",
    #     "capital": "Montpelier"
    # }, {
    #     "name": "Virginia",
    #     "capital": "Richmond"
    # }, {
    #     "name": "Washington",
    #     "capital": "Olympia"
    # }, {
    #     "name": "West Virginia",
    #     "capital": "Charleston"
    # }, {
    #     "name": "Wisconsin",
    #     "capital": "Madison"
    # },
    {
        "name": "Wyoming",
        "capital": "Cheyenne"
    }]


# Create a method to add correct and incorrect keys to each dictionary in list
def add_attributes(states):
    # - Initialize new keys in the dictionaries that store the number of times a user gets a capital `correct` and the number of times the answer is `wrong`.
    for state in states:
        state['correct'] = 0
        state['incorrect'] = 0
    return states


def play_game(states):
    # - Provide a welcome message to introduce the player to the game.
    print('Welcome to STATE CAPS - Python Edition')

    # Keep track of play score current game
    right = 0
    wrong = 0

    for state in states:
        name = state['name']
        capital = state['capital']

        # - Through all 50 states, prompt the user to name the capital of the state.
        print(f'What is the capital of {name}?')
        answer = input()

        # - If the answer is correct, display a message saying so, and increment the `correct` key.
        if answer == capital:
            print(f'{answer} was correct')
            right += 1
            state['correct'] += 1
        # - If the answer is wrong, display a message saying so, and increment the `wrong` key.
        else:
            print(f'{answer} was incorrect! The capital of {name} is {capital}.')
            wrong += 1
            state['incorrect'] += 1

        # - After each prompt, display a message telling the reader how many times the state was answered correctly out of the total number of times answered.
        num_correct = state['correct']
        num_incorrect = state['incorrect']
        print(
            f'You\'ve gotten {name}\'s capital correct {num_correct} times out of {num_correct + num_incorrect}.')

    # End-of-game text
    print('================ GAME OVER! ================')
    print(f'FINAL SCORE: \n {right} Correct \n {wrong} Incorrect')
    print('Do you want to play again?')
    print('Respond with YES or NO')


def game_loop():
    # - Make sure the states don't appear in alphabetical order in the prompts. This will make the game a bit more challenging for the user.
    random.shuffle(states)
    play_game(states)

    playing = True

    while playing:
        # - Once the user has gone through all 50 states, ask them if they'd like to play again.
        response = input()

        if response.upper() == 'YES' or response.upper() == 'Y':
            # Start a new game
            play_game(
                sorted(states, key=lambda state: state['incorrect'], reverse=True))
        else:
            playing = False
            return print('Thanks for playing!')


# Add correct and incorrect to each state
add_attributes(states)
# Start game by invoking game_loop
game_loop()
