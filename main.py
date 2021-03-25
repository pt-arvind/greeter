import json


def greet(d):
  if d['greeting_type'] == 1:
    return 'hello'
  elif d['greeting_type'] == 2:
    return 'howdy'
  elif d['greeting_type'] == 3:
    return 'bongiorno'
  else:
    raise Exception


def process_data(data):
  for d in data:
    if d["should_greet"]:
      print(greet(d))
  

input = json.loads(
    """
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
)

def main():
  process_data(input)

main()