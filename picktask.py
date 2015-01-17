#!/usr/bin/env python3

import os
import random
import sys


TODO_PATH = 'todo_temp'
CURRENT_TASK_PATH = 'task_temp'

COMMENT_MARKER = '#'


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'done':
        os.remove(CURRENT_TASK_PATH)
    else:
        current_task = read_current_task()
        if (current_task == ''):
            current_task = pick_new_task()
        print('Chosen task:', current_task)


def read_current_task():
    try:
        return open(CURRENT_TASK_PATH).read().strip()
    except IOError:
        return ''


def pick_new_task():
    lines = [line.strip() for line in open(TODO_PATH).readlines()]
    potential_tasks = [line for line in lines if len(line) > 0 and line[0] != COMMENT_MARKER]
    current_task = random.choice(potential_tasks)
    open(CURRENT_TASK_PATH, 'w').write(current_task)
    return current_task


if __name__ == '__main__':
    main()