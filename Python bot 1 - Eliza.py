# global variables
bot_template = "BOT : {0}"
user_template = "USER : {0}"
name = "Greg"
weather = "cloudy"

# import libraries
import random
import time
import re

# define a dictionary with the predifined responses
responses = {
    "what's your name?" : ["my name is {0}".format(name),
                           "they call me {0}".format(name),
                           "I go by {0}".format(name)],
    "what's today's weather?": ["the weather is {0}".format(weather),
                                "it is {0} today".format(weather),
                                "it is {0} today. You should look for sunny places!".format(weather)],
    #"default" : ["default message"],
    'question': ["I don't know :(", 'you tell me!'],
    'statement': ['tell me more!', 'why do you think that?',
                  'how long have you felt this way?',
                  'I find that extremely interesting',
                  'can you back that up?',
                  'oh wow!',':)'],
    'I want (.*)': ['What would it mean if you got {0}',
                    'Why do you want {0}',
                    "What's stopping you from getting {0}"],
    'do you remember (.*)': ['Did you think I would forget {0}',
                             "Why haven't you been able to forget {0}",
                             'What about {0}', 'Yes .. and?'],
    'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
    'if (.*)': ["Do you really think it's likely that {0}",
                'Do you wish that {0}',
                'What do you think about {0}',
                'Really--if {0}']
    }

#define a function that responds to a user's message: respond

def match_rule(responses, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, values in responses.items():

        # Create a match object
        match = re.search(pattern, message)
        if match is not None:

            # Choose a random response
            response = random.choice(values)
            if '{0}' in response:
                phrase = match.group(1)

    # Return the response and phrase
    return response, phrase


def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)

    return message


def respond(message):

    response, phrase = match_rule(responses, message)

    if '{0}' in response:
        phrase = replace_pronouns(phrase)
        bot_message = response.format(phrase)

    # concatenate the user's message to the end of a standart bot response
    elif message in responses:
        bot_message = random.choice(responses[message])
    elif message.endswith("?"):
        bot_message = random.choice(responses["question"])
    else: 
        bot_message = random.choice(responses["statement"])
    return bot_message



def send_message(message):
    # print user_template incling the user_message
    print(user_template.format(message))

    #get the bot's response to the message
    response = respond(message)
    time.sleep(1.0)

    # print the bot template including the bot's response
    print(bot_template.format(response))





