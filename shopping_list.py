shopping_list = []

def show_help():
    print("""
    Enter "SHOW" to show the list.
    Enter "DONE" to stop adding items.
    Enter "HELP" for this help.
    """)

def add_to_list(item):
    shopping_list.append(item)
    print("Item added to list. The list is currently {} items.".format(len(shopping_list)))

def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

show_help()

while True:
    print("What should we pick up at the store?")   
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue

    add_to_list(new_item)

show_list()