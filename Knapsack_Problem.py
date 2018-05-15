from random import randint
import operator
import random
import queue
import copy
import pandas as pd
import numpy as np
import time
from itertools import chain, combinations


class Task:
    def __init__(self, key, v, p, s):
        self.__id = key
        self.__value = v
        self.__priority = 10 if p is 1 else 25 if p is 2 else 50
        self.__satisfaction = s
        if v is not 0 and s is not 0:
            self.__ratio = s / v

    def penalize(self):
        self.__satisfaction -= self.__satisfaction / self.__priority
        self.__ratio = self.__value / self.__satisfaction

    @property
    def value(self):
        return self.__value

    @property
    def priority(self):
        return 1 if self.__priority is 10 else 2 if self.__priority is 25 else 3

    @property
    def satisfaction(self):
        return self.__satisfaction

    @property
    def ratio(self):
        return self.__ratio

    @property
    def id(self):
        return self.__id

    @value.setter
    def value(self, v):
        self.__value = v

    @priority.setter
    def priority(self, p):
        self.__priority = 10 if p is 1 else 25 if p is 2 else 50

    @satisfaction.setter
    def satisfaction(self, s):
        self.__satisfaction = s

    def __str__(self):
        return "[value: {}, satisfaction: {}, ratio: {}]".format(self.__value, self.__satisfaction, self.__ratio)

    def __repr__(self):
        return self.__str__()


class Randomize:
    def __init__(self, amount):
        self.__amount = amount

    def generate_rand(self, upper_bound):
        count = 0
        tasks = list()
        while count < self.__amount:
            t = Task(count, randint(1, upper_bound), randint(1, 4), randint(1, upper_bound))
            tasks.append(t)
            count += 1
        return tasks

    def generate_weibull(self, scale, shape):
        count = 0
        tasks = list()
        while count < self.__amount:
            weight = random.weibullvariate(scale, shape)
            t = Task(count, weight, randint(1, 4), (weight * randint(1, scale)))
            tasks.append(t)
            count += 1
        return tasks


class Node:

    def __init__(self, task=None, level=None, bound=None):
        if task is not None:
            self._value = task.getValue()
            self._satisfaction = task.getSatisfaction()
        self._level = level
        self._bound = bound
        self.__task = task

    @property
    def value(self):
        return self._value

    @property
    def satisfaction(self):
        return self._satisfaction

    @property
    def level(self):
        return self._level

    @property
    def bound(self):
        return self._bound

    @property
    def task(self):
        return self.__task

    @satisfaction.setter
    def satisfaction(self, x):
        self._satisfaction = x

    @value.setter
    def value(self, x):
        self._value = x

    @level.setter
    def level(self, x):
        self._level = x

    @bound.setter
    def bound(self, x):
        self._bound = x

    @task.setter
    def task(self, x):
        self.__task = x

    def __str__(self):
        return "[value: {}, satisfaction: {}, level: {}]".format(self._value, self._satisfaction, self._level)

    def __repr__(self):
        return self.__str__()


class Result:

    def __init__(self, capacity, cap_fact, scale, shape, node_count):
        self.data = dict()
        self._capacity = capacity
        self._cap_factor = cap_fact
        self._scale = scale
        self._shape = shape
        self._node_count = node_count
        self.data["Node Amount"] = self._node_count
        self.data['Scale'] = self._scale
        self.data['Shape'] = self._shape
        self.data['Capacity'] = self._cap_factor

    def to_dict(self):
        return {
            'Node Amount': self._node_count,
            'Scale': self._scale,
            'Shape': self._shape,
            'Capacity': self._capacity,
            'Greedy Ratio': self._greedy_rat[0],
            'Greedy Ratio Time': self._greedy_rat[1],
            'Greedy Value': self._greedy_val[0],
            'Greedy Value Time': self._greedy_val[1],
            'Greedy Satisfaction': self._greedy_sat[0],
            'Greedy Satisfaction Time': self._greedy_sat[1],
            'Branch and Bound': self._branch_bound[0],
            'Branch and Bound Time': self._branch_bound[1],
            'Backtracking': self._backtrack[0],
            'Backtracking Time': self._backtrack[1],
            'JoshAI': self._joshAI[0],
            'JoshAI Time':  self._joshAI[1],
            'Backtracking For': self._backtracking_for[0],
            'Backtracking For Time': self._backtracking_for[1],
        }

    @property
    def capacity(self):
        return self._capacity

    @property
    def cap_factor(self):
        return self._cap_factor

    @property
    def scale(self):
        return self._scale

    @property
    def shape(self):
        return self._shape

    @property
    def node_count(self):
        return self._node_count


def sort(tasks):
    tasks = {x.id: x for x in tasks}
    tasks = {x.id: x for x in sorted(tasks.values(), key=operator.attrgetter("ratio"), reverse=True)}
    return list(tasks.values())


def greedy(tasks, capacity, method=0):
    var = ""
    reverse = True
    if method is 0:  # Ratio
        var = "ratio"
    elif method is 1:  # Value
        var = "satisfaction"
    else:  # Satisfaction
        var = "value"
        reverse = False

    finished_list = dict()
    tasks = {x.id: x for x in tasks}
    for task in sorted(tasks.values(), key=operator.attrgetter(var), reverse=reverse):
        if task.value <= capacity:
            finished_list[task.id] = task
            capacity -= task.value
            tasks.pop(task.id)
        if capacity is 0:
            break

    return sum(x.satisfaction for x in finished_list.values())


def bound(node, cap, tasks):
    if node.value >= cap:
        return 0
    sat = node.satisfaction
    t_weight = node.value
    lvl = node.level+1
    while lvl < len(tasks) and (t_weight + tasks[lvl].value <= cap):
        t_weight += tasks[lvl].value
        sat += tasks[lvl].satisfaction
        lvl += 1
    if lvl < len(tasks):
        sat += ((cap - t_weight)*(tasks[lvl].satisfaction/tasks[lvl].value))
    return sat


def branch_and_bound(tasks, capacity):
    tasks = sort(tasks)
    max_satisfaction = 0
    q = queue.Queue()
    u = Node()
    v = Node()
    u.level = -1
    u.value = 0
    u.satisfaction = 0
    q.put(u)
    while not q.empty():
        u = q.get()
        v.level = u.level + 1
        v.satisfaction = u.satisfaction + tasks[v.level].satisfaction
        v.value = u.value + tasks[v.level].value
        if v.value <= capacity and v.satisfaction > max_satisfaction:
            max_satisfaction = v.satisfaction
        v.bound = bound(v, capacity, tasks)
        if v.bound > max_satisfaction:
            q.put(copy.deepcopy(v))
        v.satisfaction = u.satisfaction
        v.value = u.value
        v.bound = bound(v, capacity, tasks)
        if v.bound > max_satisfaction:
            q.put(copy.deepcopy(v))
    return max_satisfaction


def launch_backtrack_rec(tasks, cap):
    u = Node()
    u.level = -1
    u.value = 0
    u.satisfaction = 0
    return backtrack_rec(tasks, cap, u, 0)


def backtrack_rec(tasks, cap, opt, max):
    if opt.level + 1 is len(tasks):
        if opt.value <= cap and opt.satisfaction > max:
            max = opt.satisfaction
    else:
        u = copy.deepcopy(opt)
        opt.level += 1
        opt.value = opt.value + tasks[opt.level].value
        opt.satisfaction = opt.satisfaction + tasks[opt.level].satisfaction
        if opt.value <= cap and opt.satisfaction > max:
            max = opt.satisfaction
        if opt.value <= cap:
            max = backtrack_rec(tasks, cap, copy.deepcopy(opt), max)
        opt.value = u.value
        opt.satisfaction = u.satisfaction
        if opt.value <= cap:
            max = backtrack_rec(tasks, cap, copy.deepcopy(opt), max)
    return max


def backtracking(tasks, capacity):
    tasks = sort(tasks)
    max_satisfaction = 0
    q = queue.Queue()
    u = Node()
    v = Node()
    u.level = -1
    u.value = 0
    u.satisfaction = 0
    q.put(u)
    while not q.empty():
        u = q.get()
        v.level = u.level + 1
        v.satisfaction = u.satisfaction + tasks[v.level].satisfaction
        v.value = u.value + tasks[v.level].value

        if v.value <= capacity and v.satisfaction > max_satisfaction:
            max_satisfaction = v.satisfaction

        if v.level != len(tasks)-1:
            if v.value <= capacity:
                q.put(copy.deepcopy(v))

            v.satisfaction = u.satisfaction
            v.value = u.value

            if v.value <= capacity:
                q.put(copy.deepcopy(v))
    return max_satisfaction


def getlen(array):
    return len(array)


def joshsway(tasks, capacity):
    permutations = sorted({tuple([tasks[y] for y in range(len(tasks)) if x & (1 << y)]) for x in range(2**len(tasks))}, key=getlen)
    permutations = [(x, sum(y.satisfaction for y in x)) for x in permutations if sum(y.value for y in x) <= capacity]
    result = max(permutations, key=lambda item: item[1])
    return result[1]


def joshv2(tasks, capacity):
    li = []
    for x in range(2**len(tasks)):
        xy = []
        flag = True
        xy_val_sum = 0
        xy_sat_sum = 0
        for y in range(len(tasks)):
            if x & (1 << y):
                if xy_val_sum <= capacity and tasks[y].value <= capacity:
                    xy.append(tasks[y])
                    xy_val_sum += tasks[y].value
                    xy_sat_sum += tasks[y].satisfaction
                else:
                    flag = False
                    break
        if flag is True:
            li.append((xy, xy_sat_sum))
    result = max(li, key=lambda item: item[1])
    return result[1]


def benchmark(node_counts, scale, shapes, cap):
    results = []
    for x in range(0, 4):
        for x in node_counts:  # An array with the amount of tests to run each with the amount of nodes in each test
            data = Randomize(x)
            for y in shapes:  # An array again running the test x times each with a different shape
                tasks = data.generate_weibull(scale, y)
                for z in cap:  # An array with the amount of tests to run each with a different capacity
                    powercell = (sum(x.value for x in tasks) / 100 * z)
                    result = Result(powercell, z, scale, y, x)
                    start = time.clock()
                    result.data["Greedy Ratio"] = greedy(tasks, powercell)
                    result.data["Greedy Ratio Time"] = time.clock() - start
                    start = time.clock()
                    result.data["Greedy Value"] = greedy(tasks, powercell, method=2)
                    result.data["Greedy Value Time"] = time.clock() - start
                    start = time.clock()
                    result.data["Greedy Satisfaction"] = greedy(tasks, powercell, method=1)
                    result.data["Greedy Satisfaction Time"] = time.clock() - start
                    start = time.clock()
                    result.data["Branch and Bound"] = branch_and_bound(tasks, powercell)
                    result.data["Branch and Bound Time"] = time.clock() - start
                    """
                    if x < 22:
                        start = time.clock()
                        result.data["Backtracking"] = launch_backtrack_rec(tasks, powercell)
                        result.data["Backtracking Time"] = time.clock() - start
                        start = time.clock()
                        result.data["Create_Test"] = joshsway(tasks, powercell)
                        result.data["Create_Test_Time"] = time.clock() - start
                        start = time.clock()
                        result.data["Backtracking For"] = backtracking(tasks, powercell)
                        result.data["Backtracking For Time"] = time.clock() - start
                    else:
                        result.backtrack = ["--", "--"]
                        result.joshAI = ["--", "--"]
                        result.backtracking_for = ["--", "--"]
                    """
                    results.append(result)
                print("Complete for shape: {}".format(y))
            print("Complete for node: {}".format(x))
    return results


def benchmarkJosh(node_counts, scale, shapes, cap):
    results = []
    for x in node_counts:  # An array with the amount of tests to run each with the amount of nodes in each test
        data = Randomize(x)
        for y in shapes:  # An array again running the test x times each with a different shape
            tasks = data.generate_weibull(scale, y)
            for z in cap:  # An array with the amount of tests to run each with a different capacity
                powercell = (sum(x.value for x in tasks) / 100 * z)
                result = Result(powercell, z, scale, y, x)
                start = time.clock()
                result.data["Create_Test"] = joshsway(tasks, powercell)
                result.data["Create_Test_Time"] = time.clock() - start
                start = time.clock()
                result.data["Backtracking For"] = joshv2(tasks, powercell)
                result.data["Backtracking For Time"] = time.clock() - start
                results.append(result)
            print("Complete for shape: {}".format(y))
        print("Complete for node: {}".format(x))
    return results


def format_results(results):
    print("Writing results to file")
    df = pd.DataFrame.from_records([x.data for x in results])
    writer = pd.ExcelWriter('Results.xlsx')
    df.to_excel(writer, 'Sheet1')
    writer.save()


def main():
    #  format_results(benchmark(range(5, 30), 1000, [0.5, 1.5, 5], [70, 50, 30]))
    format_results(benchmark([50], 1000, [0.5, 1.5, 5], [30]))
    #  format_results(benchmarkJosh(range(3, 21), 1000, [0.5, 1.5, 5], [70, 50, 30]))


main()
