from random import randint


def make_guess(guess, monkey_position, output_lines):
    output_string = 'Guessed ' + str(guess) + ' while monkey was in ' + str(monkey_position) + '. '
    succeeded = guess == monkey_position
    if succeeded:
        output_string += 'HIT!'
    else:
        output_string += 'Missed.'
    output_lines.append(output_string)
    return succeeded


def move(monkey_position, number_of_cars, output_lines):
    if monkey_position == 1:
        new_monkey_position = 2
    elif monkey_position == number_of_cars:
        new_monkey_position = number_of_cars - 1
    else:
        dir = randint(0, 1)
        if dir == 0:
            new_monkey_position = monkey_position + 1
        else:
            new_monkey_position = monkey_position - 1
    output_lines.append('Moved from ' + str(monkey_position) + ' to ' + str(new_monkey_position) + '.')
    return new_monkey_position


def print_buffer(output_lines):
    for i in range(2):
        output_lines.append('')

number_of_cars = 10
number_of_simulations = 20
output_lines = []

for i in range(number_of_simulations):
    output_lines.append('Running simulation number ' + str(i+1))
    succeeded = False
    monkey_position = randint(1, number_of_cars)
    output_lines.append('Monkey initial position: ' + str(monkey_position))
    for guess in range(2, 10):
        succeeded = make_guess(guess, monkey_position, output_lines)
        if succeeded:
            break
        monkey_position = move(monkey_position, number_of_cars, output_lines)
    if not succeeded:
        for guess in range(9, 1, -1):
            succeeded = make_guess(guess, monkey_position, output_lines)
            if succeeded:
                break
            monkey_position = move(monkey_position, number_of_cars, output_lines)

    print_buffer(output_lines)

with open('output.txt', 'w') as f:
    for line in output_lines:
        f.write(line + '\n')
