print('Welcome to Mad Libs\n'
      'Answer the questions below, in order to create your story.')
name = input("Please enter a name: ")
noun = input("Please enter a plural noun: ")
number = input("Please enter a number: ")
body_part = input("Please enter a body part: ")
verb = input("Please enter a verb: ")

print(f'Your glorious story:\n'
      f'The famous explorer {name} had nearly given up a life-long quest to find\n'
      f'The Lost City of {noun} when one day, the {noun} found the explorer.\n'
      f'Surrounded by {number} {noun}, a tear came to {name}\'s {body_part}.\n'
      f'"After all this time, the quest was finally over. And then, the {noun}\n'
      f'promptly devoured {name}.\n'
      f'The moral of the story? Be careful what you {verb} for.')