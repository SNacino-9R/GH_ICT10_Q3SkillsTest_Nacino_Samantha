from pyscript import document

def create_account(event):

    user = document.getElementById("username").value
    pwd = document.getElementById("password").value
    message = document.getElementById("output")

   
    message.innerHTML = ""

  
    if len(user) < 7:
        message.innerHTML = "Username must be at least 7 characters."
        return

  
    if len(pwd) < 10:
        message.innerHTML = "Password must be at least 10 characters long."
        return

    letter_found = False
    number_found = False

  
    for ch in pwd:
        if ch.isalpha():
            letter_found = True
        if ch.isdigit():
            number_found = True

    if letter_found == False:
        message.innerHTML = "Password needs at least one letter."
        return

    if number_found == False:
        message.innerHTML = "Password needs at least one number."
        return

    message.innerHTML = "Account successfully created!"
