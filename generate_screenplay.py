import re


def clean_actor_in_given(actor_in_given: str):
    return extract_keyword_in_delimiter(actor_in_given.split("GIVEN")[1])


def extract_keyword_in_delimiter(decorated_keyword: str):
    if decorated_keyword.strip() == "<Actor>":
        return "Actor"
    elif decorated_keyword == """ <Ability>
                    > """:
        return "Ability"
    else:
        raise Exception("could not extract the keyword")
    # pattern = "^.*<(.*)>.*$"
    # result = re.match(pattern, decorated_keyword)
    # return result.group(0)


def clean_ability_in_given(ability_in_given):
    return extract_keyword_in_delimiter(ability_in_given)


def clean_task_in_when(task_in_when: str):
    return "Task"


def clean_parameter_in_when(param_in_when: str):
    return "Parameters"


def generate_screenplay(my_scene: str) -> dict:
    """
    > GIVEN <Actor> who can <Ability…>
    > WHEN <Actor> does <Task(Parameters)>
    > THEN <Actor> checks <Question> is <Assertion… on Answer>
    > THANKS TO <element> FOUND ON <screen>
    :param my_scene:
    :return:
    """
    screen_play_generated_parts = {
        "actors": [],
        "facts": [],
        "tasks": [],
        "questions": [],
        "elements": [],
        "screens": [],
        "abilities": [],
        "actions": []
    }
    if my_scene is None or my_scene == "":
        return screen_play_generated_parts

    given_whenthen = my_scene.split("WHEN")
    given_part = given_whenthen[0]
    whenthen_part = given_whenthen[1].split("THEN")
    when_part = whenthen_part[0]
    then_part = whenthen_part[1]

    given_parts = given_part.split("who can")
    screen_play_generated_parts["actors"].append(clean_actor_in_given(given_parts[0]))
    screen_play_generated_parts["abilities"].append(clean_ability_in_given(given_parts[1]))
    does_parts = when_part.split("does")
    task = does_parts[1].split("<")
    screen_play_generated_parts["actions"].append(
        {"do": clean_task_in_when(task[1]), "direct object": clean_parameter_in_when(task[2])}
    )
    return screen_play_generated_parts


#
# def generate_screenplay2(my_scene: str) -> dict:
#     """
#
# > GIVEN <Actor> who can <Ability…>
# > WHEN <Actor> does <Task(Parameters)>
# > THEN <Actor> checks <Question> is <Assertion… on Answer>
# > THANKS TO <element> FOUND ON <screen>
#     :param my_scene:
#     :return:
#     """
#     screen_play_generated_parts = {}
#     screen_play_parts = my_scene.split("WHEN")
#     given_part = screen_play_parts[0]
#     when_part = screen_play_parts[1]
#     print(given_part)
#     given_parts = given_part.split("who can")
#     actors = given_parts[0]
#     facts = given_parts[1]
#     print(when_part)
#     screen_play_generated_parts[actors]
#     return screen_play_generated_parts


if __name__ == '__main__':
    my_scene = """
GIVEN <Jack> who can <browse the web> and <call HTTP APIs>
WHEN <Jack> does <walk into> <The Sheep's Head Pub>
    AND does <order> <999 beers>
    THEN <Jack> checks <the bill's total amount> <is 999 × 2.59 EUR>
"""
    generate_screenplay(my_scene)
