# start with creating class and dictionary

# Good start. Next step would be making it repetitive so I can add multiple users and query multiple people. How do that?

# DAVID: x is a bad name: this should be something more meaniful like command_text, or user_prompt_text
# DAVID:  secondly as file size gets bigger try searching for x lol
command = "Please enter an instruction "

# DAVID:  Good data structure choice
phone_book = {"kelly": 4725692, "lore": 542652}



while True:
    print(command)
    user_prompt_text = input()
    new_list = user_prompt_text.split()
    user_prompt_text = new_list[0]
    name = new_list[1]
    if user_prompt_text == "add":
        name = new_list[1]
        number = new_list[2]
        phone_book[name] = number
        print("This has been added \n")
    elif user_prompt_text == "query":
        name = ""
        number = 0
        name = new_list[1]
        new_number = phone_book.get(name)
        print(name, new_number)
    elif user_prompt_text == "query":
        name = ""
        number = 0
        number = new_list[2]
        phone_book[number] = name
        print(name, number)

