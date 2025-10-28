from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console
from rich.prompt import Prompt

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "You walk left. " + event

def right_path(event):
    return "You walk right. " + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')
    console = Console()

    print("[sandy_brown]You wake up in a dark forest.[/sandy_brown] \n[sandy_brown]You can go left or right.[/sandy_brown]")
    #print("")
    while True:
        #choice = input("Which direction do you choose? \n(left/right/exit): ")
        #choice = choice.strip().lower()
        choice = Prompt.ask("[bold u dark_green]Which direction do you choose?[/bold u dark_green] [bold italic dark_green](left/right/exit): [/bold italic dark_green]")
        if choice == 'exit':
            print("[bold gold1]Goodbye Adventurer![/bold gold1]")
            break
        
        print(step(choice, events))
