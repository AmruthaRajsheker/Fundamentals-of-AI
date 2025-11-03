# ExpNo:10 Implementation of Classical Planning Algorithm
### Name: Amrutha Rajsheker
### Register Number: 212222110003

## Aim:
To implement classical planning algorithm

## Algorithm or Steps Involved:
- Define the initial state
- Define the goal state
- Define the actions
- Find a plan to reach the goal state
- Print the plan

## Example - 1
```
initial_state = {'A': 'Table', 'B': 'Table'}
goal_state = {'A': 'B', 'B': 'Table'}

actions = {
    'move_A_to_B': {'precondition': {'A': 'Table', 'B': 'Table'}, 'effect': {'A': 'B'}},
    'move_B_to_Table': {'precondition': {'A': 'Table', 'B': 'B'}, 'effect': {'B': 'Table'}}
}

plan = find_plan(initial_state, goal_state, actions)
print(plan)
```
## Output:
```
['move_A_to_B']
```
## Example - 2
```
initial_state = {'A': 'Table', 'B': 'Table', 'C': 'Table'}
goal_state = {'A': 'B', 'B': 'C', 'C': 'Table'}

actions = {
    'move_A_to_B': {'precondition': {'A': 'Table', 'B': 'Table'}, 'effect': {'A': 'B'}},
    'move_B_to_C': {'precondition': {'A': 'B', 'B': 'Table', 'C': 'Table'}, 'effect': {'B': 'C'}},
    'move_C_to_Table': {'precondition': {'A': 'B', 'B': 'C', 'C': 'C'}, 'effect': {'C': 'Table'}}
}

plan = find_plan(initial_state, goal_state, actions)
print(plan)
```
## Output:
```
['move_A_to_B', 'move_B_to_C']
```
## Program:
```
def is_goal_state(current_state, goal_state):
    # Return True if all key-value pairs in goal_state match current_state
    return all(current_state.get(key) == value for key, value in goal_state.items())

def apply_action(current_state, action_effect):
    new_state = current_state.copy()
    new_state.update(action_effect)
    return new_state

def is_applicable(current_state, precondition):
    return all(current_state.get(key) == value for key, value in precondition.items())

def find_plan(initial_state, goal_state, actions):
    queue = [(initial_state, [])]
    visited_states = set()

    while queue:
        current_state, partial_plan = queue.pop(0)

        if is_goal_state(current_state, goal_state):
            return partial_plan

        if tuple(current_state.items()) in visited_states:
            continue

        visited_states.add(tuple(current_state.items()))

        for action in actions:
            if is_applicable(current_state, actions[action]['precondition']):
                next_state = apply_action(current_state, actions[action]['effect'])
                queue.append((next_state, partial_plan + [action]))

    print("No plan exists.")
    return None

# Example usage
initial_state = {'A': 'Table', 'B': 'Table', 'C': 'Table'}
goal_state = {'A': 'B', 'B': 'C', 'C': 'Table'}

actions = {
    'move_A_to_B': {'precondition': {'A': 'Table', 'B': 'Table'}, 'effect': {'A': 'B'}},
    'move_B_to_C': {'precondition': {'A': 'B', 'B': 'Table', 'C': 'Table'}, 'effect': {'B': 'C'}},
    'move_C_to_Table': {'precondition': {'A': 'B', 'B': 'C', 'C': 'C'}, 'effect': {'C': 'Table'}}
}

plan = find_plan(initial_state, goal_state, actions)
print("Plan:", plan)
```
## Output:
![image](https://github.com/user-attachments/assets/a7f6f738-f8a5-4689-a7da-916c378b44c8)

## Result:
Therefore, Classical Planning Algorithm is implemetated successfully.
