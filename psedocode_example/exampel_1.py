"""Using the pseudocode and link to a flow chart below, write a program that simulates a task list.
Start
    Make Bed
    Brush Teeth
     If Is Box Empty
        Open new Box
     Eat Breakfast
     Go to School
End
https://lucid.app/lucidchart/711bb30d-84d9-44aa-ba01-f4eb9238e7fb/edit?view_items=0czgPcRe0Aod%2CTgzgPzbWiw3U%2CGgzgR_Jsy2RN%2CQezgEl2TFUuq%2CfhzgcfN8eQWT%2Cdnzg4gA5wVBm&invitationId=inv_615a9ae5-42fa-4a3f-83c8-3d5c63963416
"""
import random
from time import sleep


def task(tasks_time: int = 100, tasks=None) -> None:
    """
    Given a list of instructions, execute them in a given time.
    :param tasks_time: Time to execute all instructions
    :type tasks_time: int
    :param tasks: List of instructions
    :type tasks: list[str]
    :return: None
    """
    if tasks is None:
        tasks = []
    try:
        step_time = tasks_time / len(tasks)
        for instruction in tasks:
            print(instruction)
            sleep(step_time)
    except ZeroDivisionError as zero_ex:
        print(f"{zero_ex}: You have to enter at least one task!")


def make_bed(time: int = 300) -> None:
    """
    Make bed in a given time.
    :param time: Time to make bed
    :type time: int
    :return: None
    """
    instructions: list[str] = ["Arrange pillows", "Fold blanket"]

    print("Start make bed")
    task(time, instructions)


def brush_teeth(time: int = 120) -> None:
    """
    Brush teeth in a given time.
    :param time: Time to brush teeth
    :type time: int
    :return: None
    """
    instructions: list[str] = ["Grab toothbrush", "Grab toothpaste",
                               "Put toothpaste on toothbrush",
                               "Bring toothbrush to teeth",
                                "Move brush side-to-side", "Rinse mouth"]
    print("Start brushing teeth")
    task(time, instructions)


def open_new_box(time: int = 30, container: int = 0, total_servings: int = 12) -> int:
    """
    Open a new box of cereal if the current box is empty.
    :param time: Time to open new box
    :type time: int
    :param container: quantity of cereal in the box
    :type container: int
    :param max: max cereal box serving quantity
    :type total_servings: int
    :return: quantity of cereal left in the box; if box is empty, return a box at full capacity
    """
    if container <= 0:
        print("Open new box")
        instructions = ["Tear tabs on a new box", "Pull plastic lining in box"]
        task(time, instructions)
        return total_servings
    task(1, [f"You don't need to open a new box yet. You. have {container} servings left."])
    return container


def eat_breakfast(time: int = 900, container: int = 1)-> int:
    """
    Eat breakfast in a given time.
    :param time: Time to eat breakfast
    :type time: int
    :param container: quantity of cereal in the box
    :type container: int
    :return: quantity of cereal left in the box
    """
    print("Eat breakfast")
    instructions = ["Grap a clean bowl", "Grab a box of cereal", "Grab a clean spoon",
                    "Grab milk from the fridge", "Reopen cereal box", "Pour cereal in bowl",
                    "Eat breakfast"]
    task(time, instructions)
    return container - 1


def go_to_school(time: int = 1500)-> None:
    """
    Prepare and travel to school in a given time.
    :param time: Time to spend commuting to school
    :type time: int
    :return: None
    """
    print("Go to school")
    instructions = ["Grab lunch", "Place lunch in school bag", "Strap bag to back",
                    "Got to bus stop", "Get on bus", "Get off bus", "Go to class"]
    task(time, instructions)


if __name__ == "__main__":
    make_bed(450) # make bed for 7.5 minutes
    brush_teeth(240) # brush teeth for 4 minutes

    MAX_CAPACITY = 16 # max cereal box serving quantity

    box = random.randint(0, MAX_CAPACITY) # give our cereal box a random start serving quantity

    # if box is empty open a new box
    if box <= 0:
        box = open_new_box(60, box) # open a new box in 1 minute

    box = eat_breakfast(900, box) # eat breakfast for 15 minutes
    go_to_school(950) # spend 15 minutes commuting to school
