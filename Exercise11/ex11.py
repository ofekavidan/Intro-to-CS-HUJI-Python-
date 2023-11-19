#############################################################
# FILE : ex11.py
# WRITER : Ofek Avidan , ofek.avidan , 318879574
# EXERCISE : intro2cse exercise11 2021
# HELPED BY: Adi cogan (sh'at kabala), Lab support (especially - Yuval Cohen and Itai Valach)
# HELPED BY: https://bit.ly/3BDwAhd
#############################################################


import copy
import collections
import itertools
import operator




class Node:
    """Class we received when receiving the exercise"""

    def __init__(self, data, positive_child=None, negative_child=None):
        """Function we received when receiving the exercise"""
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child




class Record:
    """Class we received when receiving the exercise"""

    def __init__(self, illness, symptoms):
        """Function we received when receiving the exercise"""
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    """Function we received when receiving the exercise"""
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose(self, symptoms):
        temp = copy.deepcopy(self.root)
        temp2 = self.diagnose_helper(symptoms)
        self.root = temp
        return temp2


    def diagnose_helper(self, symptoms):
        if not self.root.positive_child and not self.root.negative_child:
            return self.root.data

        if self.root.data in symptoms:
            self.root = self.root.positive_child
            return self.diagnose(symptoms)
        else:
            self.root = self.root.negative_child
            return self.diagnose(symptoms)


    def calculate_success_rate(self, records):

        if not records:
            raise ValueError('Error, no records found in records')

        counter = 0
        success_counter = 0

        temp = copy.deepcopy(self.root)

        for record in records:
            self.root = temp
            counter += 1
            if self.diagnose(record.symptoms) == record.illness:
                success_counter += 1

        return success_counter / counter


    def all_illnesses(self):
        temp = copy.deepcopy(self.root)
        temp2 = self.all_illnesses_helper([])
        self.root = temp

        counts = collections.Counter(temp2)
        new_list = sorted(temp2, key=lambda x: -counts[x])

        new_k = []
        for elem in new_list:
            if elem not in new_k:
                new_k.append(elem)
        new_list = new_k

        return new_list

    def all_illnesses_helper(self, lst):
        if self.root.negative_child is None and self.root.positive_child is None:
            if self.root.data is not None:
                lst.append(self.root.data)
                return

        if self.root.positive_child is not None:
            temp = self.root
            self.root = self.root.positive_child
            self.all_illnesses_helper(lst)
            self.root = temp

        if self.root.negative_child is not None:
            temp = self.root
            self.root = self.root.negative_child
            self.all_illnesses_helper(lst)
            self.root = temp



        return lst


    def paths_to_illness(self, illness):
        temp = self.root
        temp2 = self.paths_to_illness_helper(illness, [])
        self.root = temp
        return temp2


    def paths_to_illness_helper(self, illness, partial):

        # took from Tirgul 8, just changes some little things from Subset Sum

        if self.root.positive_child is None and self.root.negative_child is None:
            res = []
            if self.root.data == illness:
                res.append(partial[:])

            return res


        solution_list = []

        temp = self.root
        if self.root.positive_child:
            self.root = self.root.positive_child
            partial.append(True)
            solution_list += self.paths_to_illness_helper(illness, partial)
            self.root = temp
            partial.pop()

        temp = self.root
        if self.root.negative_child:
            self.root = self.root.negative_child
            partial.append(False)
            solution_list += self.paths_to_illness_helper(illness, partial)
            self.root = temp
            partial.pop()

        return solution_list






    def minimize(self, remove_empty=False):
        # False part - happens either way:

        if remove_empty is False:
            self.root = self.minimize_helper_false(self.root)

        # True part - happens only if remove_empty = True

        if remove_empty:
            self.root = self.minimize_helper_true(self.root)
            self.root = self.minimize_helper_false(self.root)





    def minimize_helper_true(self, node):
        if is_leaf(node):
            return node



        node.positive_child = self.minimize_helper_true(node.positive_child)
        node.negative_child = self.minimize_helper_true(node.negative_child)

        if (node.positive_child.data is None):
            return node.negative_child

        if (node.negative_child.data is None):
            return node.positive_child


        return node


    def minimize_helper_false(self, node):
        # helped by Itai Valach from lab support
        if is_leaf(node):
            return node



        node.positive_child = self.minimize_helper_false(node.positive_child)
        node.negative_child = self.minimize_helper_false(node.negative_child)


        if(if_next_level_is_extra(node)):
            return node.positive_child

        return node





def if_next_level_is_extra(n):
    return identicalTrees(n.negative_child, n.positive_child)


def is_leaf(node):
    if node.positive_child is None and node.negative_child is None:
        return True

    return False



def build_tree(records, symptoms):

    if not symptoms and not records:
        return Diagnoser(Node(None))


    for record in records:
        if type(record) is not Record:
            raise TypeError("error, record not Record")

    node = Node(None, None, None)

    for symptom in symptoms:
        if type(symptom) != str:
            raise TypeError("there's symptom whos not really string")

    # if not symptoms:
    #     for record in records:
    #         for symptom in record.symptoms:
    #             if symptom not in symptoms:
    #                 symptoms.append(symptom)
    #     return Diagnoser(Node())


    build_tree_without_leaves(records, symptoms, node, 0, [], [])
    diagnoser3 = Diagnoser(node)

    return diagnoser3


def identicalTrees(a, b):

    # from geeksforgeeks

    # 1. Both empty
    if a is None and b is None:
        return True

    # 2. Both non-empty -> Compare them
    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.positive_child, b.positive_child) and
                identicalTrees(a.negative_child, b.negative_child))

    # 3. one empty, one not -- false
    return False


def most_frequent(lst):

    if not lst:
        return None

    counter = 0
    num = lst[0]

    for i in lst:
        curr_frequency = lst.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

def build_tree_without_leaves(records, symptoms, node, index, lst_true, lst_false):

    # helped by yuval cohen and amit kadosh from Lab Support


    if index == len(symptoms):
        flag = True
        lst = []
        for record in records:

            flag = True

            if type(record) != Record:
                raise TypeError("there's record whos not really record")

            for symptom in lst_true:
                if symptom not in record.symptoms:
                    flag = False

            for symptom in lst_false:
                if symptom in record.symptoms:
                    flag = False


            if flag:
                lst.append(record.illness)

        node.data = most_frequent(lst)
        return

    node.data = symptoms[index]


    node.positive_child = Node(None, None, None)
    build_tree_without_leaves(records, symptoms, node.positive_child, index + 1, lst_true+[symptoms[index]], lst_false)

    node.negative_child = Node(None, None, None)
    build_tree_without_leaves(records, symptoms, node.negative_child, index + 1, lst_true, lst_false+[symptoms[index]])






def optimal_tree(records, symptoms, depth):
    # helped by federico from Lab Support

    # value errors:
    if not (len(symptoms) >= depth >= 0):
        raise ValueError("the depth is invalid!")
    for symptom in symptoms:
        if symptoms.count(symptom) > 1:
            raise ValueError("duplicate symptom")


    # type errors:

    for symptom in symptoms:
        if type(symptom) != str:
            raise TypeError("all the symptoms should be strings")
    for record in records:
        if type(record) != Record:
            raise TypeError("record is not Record")



    combinations = itertools.combinations(symptoms, depth)

    dict1 = {} # key - buildtree of some combination , value - success rate

    for combination in combinations:
        key = build_tree(records, combination)
        dict1[key] = build_tree(records, combination).calculate_success_rate(records)


    maxdiagnoser = max(dict1.items(), key=operator.itemgetter(1))[0]
    return maxdiagnoser





