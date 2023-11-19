import random
answers = ['It is certain', 'As I see it, yes', 'Reply hazy, try again', '''Don't count on it''',
           'It is decidedly so', 'Most likely', 'Ask again later', 'My reply is no',
           'Without a doubt', 'Outlook good', 'Better not tell you now', 'My sources say no'
           'Yes definitely', 'Yes', 'Cannot predict now', 'Outlook not so good',
           'You may rely on it', 'Signs point to yes', 'Concentrate and ask again', 'Very doubtful']
print('Hello, World, I am a magic ball and I know the answer to any of your questions.')
name = input('What is your name? ')
print(f'Hello, {name}')
again = 'y'
while again.lower() == 'y':
    question = input("Ask me your question: ")
    print(random.choice(answers))
    again = input('Do you want to ask one more questions? (y - yes, n - no): ')
    
    if not again == 'y':
        print('Come back if you have questions!')