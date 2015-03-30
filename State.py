__author__ = 'ryuzakinho'
from Variable import Variable
import copy


class State(object):
    """
    This class is a state. It contains all the elements of tree's state.
    """

    def __init__(self, *args):
        """
        This constructor is used starting from the second level of the search tre.
        :param variable:
        :param truth_assignement:
        :param already_assigned_variables:
        """
        if len(args) == 4:
            self.variable = Variable(args[0])
            self.variable.variable_value = args[1]
            self.already_assigned_variables = args[2]
            self.unsat_clause_list = copy.deepcopy(args[3])
        elif len(args) == 1:
            self.variable = None
            self.already_assigned_variables = list()
            self.unsat_clause_list = copy.deepcopy(args[0])
        else:
             print "Wrong number of arguments"
