# An answer to task 7-20 in beginning Python


def hard_deadline_schedule(tasks, remove_gaps=False):
    """ Finds the most profitable schedule of a list of unit sized tasks. If a task can't be performed within its
    deadline, it will not be included in the schedule.

    :param tasks: An unsorted sequence of (profit, deadline) tuples. All tasks take one time unit of work to complete.
    :param remove_gaps: If True, any time slot occupied by None will be removed and subsequent tasks pushed forward.
    :return: An array representing the optimal schedule.
    """

    latest = _latest_deadline(tasks)            # In order to allocate the best schedule

    schedule = [None for i in range(latest)]

    sorted_tasks = sorted(tasks)

    while sorted_tasks:
        task_in_question = sorted_tasks.pop()
        deadline = task_in_question[1]

        for i in range(deadline-1, -1, -1):
            if schedule[i] is None:
                schedule[i] = task_in_question
                break

    if remove_gaps:
        schedule = [task for task in schedule if task is not None]

    return schedule

def _latest_deadline(tasks):
    """Finds the latest deadline from an unsorted sequence of tasks

    :param tasks: A sequence of (profit, deadline) tuples.
    :return: The maximum deadline.
    """
    return max(tasks, key=lambda x: (x[1]))[1]


def _latest_test(tasks):
    print(_latest_deadline(tasks))


def _schedule_test(tasks):
    return hard_deadline_schedule(tasks, True)


if __name__ == "__main__":
    t = [(18, 4), (17, 4), (16, 3), (20, 2), (3, 1)]
    _latest_test(t)
    print(_schedule_test(t))


