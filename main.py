import json
import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Any

# exercise: add an enum for greeting type and a timestamp to the json and see how you would parse it into the data class!


class InvalidActionTypeError(RuntimeError):
    """Error generated if invalid action type is given."""


@dataclass(eq=True)
class GreetingAction:
    id: int
    user_id: int
    should_greet: bool
    greeting_type: int


def greet(d: GreetingAction) -> str:
    if d.greeting_type == 1:
        return "hello"
    elif d.greeting_type == 2:
        return "howdy"
    elif d.greeting_type == 3:
        return "bongiorno"
    else:
        raise InvalidActionTypeError


def load_data(data: List[Dict[str, Any]]) -> List[GreetingAction]:
    greets: List[GreetingAction] = []
    for d in data:
        g: GreetingAction = GreetingAction(
            int(d["id"]),
            int(d["user_id"]),
            bool(d["should_greet"]),
            int(d["greeting_type"]),
        )
        greets.append(g)
    return greets


def process_data(data: List[GreetingAction]) -> None:
    for d in data:
        if d.should_greet:
            print(greet(d))


def main():
    data = load_data(json.loads(json_data))
    process_data(data)


json_data = """
    [
        {
            "id": 1000,
            "should_greet": false,
            "user_id": 1,
            "greeting_type": 3
        },
        {
            "id": 1000,
            "should_greet": true,
            "user_id": 5,
            "greeting_type": 1
        }
    ]
    """


main()
