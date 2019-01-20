prompt = ('\n Tell me something , and i will repeate it to u')
prompt += ('\n Enter "quit" to end\n')

message = " "

while(message != 'quit'):
    message = input(prompt)
    if message != 'quit':
        print(message)
    
