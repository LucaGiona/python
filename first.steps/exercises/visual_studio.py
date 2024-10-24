#Please write a program which asks the user which editor they are using. The program should keep on asking until the user types in Visual Studio Code.




while True:
    editor = input("Editor: ").strip()
    edit = editor.lower()
    
    if edit == "visual studio code":
        print("an excellent choice")
        break
    elif edit == "word" or edit == "notepad":
        print("awful")
    else:
        print("not good")
    