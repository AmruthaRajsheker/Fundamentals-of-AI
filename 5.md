# ExpNo 5 : Implement Simple Hill Climbing Algorithm

#### Name: Sowmya V
#### Register Number:  212222110045

### Aim:
Implement Simple Hill Climbing Algorithm and Generate a String by Mutating a Single Character at each iteration 

### Theory: 
Hill climbing is a variant of Generate and test in which feedback from test procedure is used to help the generator decide which direction to move in search space.
Feedback is provided in terms of heuristic function

### Algorithm:
- Evaluate the initial state.If it is a goal state then return it and quit. Otherwise, continue with initial state as current state.
- Loop until a solution is found or there are no new operators left to be applied in current state:
- Select an operator that has not yet been applied to the current state and apply it to produce a new state
Evaluate the new state:
 1. if it is a goal state, then return it and quit
 2. if it is not a goal state but better than current state then make new state as current state
 3. if it is not better than current state then continue in the loop

### Steps Applied:
1. Step-1
   - Generate Random String of the length equal to the given String
2. Step-2
   - Mutate the randomized string each character at a time
3. Step-3
   - Evaluate the fitness function or Heuristic Function
4. Step-4
   - Lopp Step -2 and Step-3  until we achieve the score to be Zero to achieve Global Minima.

### Program:
```
import random
import string

def generate_random_solution(answer):
    l = len(answer)
    return [random.choice(string.printable) for _ in range(l)]

def evaluate(solution, answer):
    print("Current solution:", "".join(solution))
    target = list(answer)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff

def mutate_solution(solution):
    ind = random.randint(0, len(solution) - 1)
    solution[ind] = random.choice(string.printable)
    return solution

def SimpleHillClimbing():
    answer = "Artificial Intelligence"
    best = generate_random_solution(answer)
    best_score = evaluate(best, answer)
    max_iterations = 1000
    iterations = 0
    while True:
        print("Score:", best_score, "Solution:", "".join(best))
        if best_score == 0:
            break
        if iterations >= max_iterations:
            print("Max iterations reached.")
            break
        new_solution = mutate_solution(list(best))
        score = evaluate(new_solution, answer)
        if score < best_score:
            best = new_solution
            best_score = score
        iterations += 1

SimpleHillClimbing()

```
### Sample Input:
Artificial Intelligence

### Output:
![image](https://github.com/user-attachments/assets/32732454-2687-4892-ad6c-ef7644115cd1)

### Result:
Thus the Simple hill climbing algorithm has been executed successfully.
