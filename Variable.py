__author__ = 'ryuzakinho'


class Variable(object):
    """
    This class represents a logical variable used in the SAT problem
    it has the following attributes:
    variable_number : int
    variable_value : int
    clauses_containing_the_variable : array of clause numbers
    """

    def __init__(self, variable_number):
        """
        :param variable_number: int
        """
        self.variable_number = variable_number
        self.variable_value = None

    @staticmethod
    def where_is_the_variable(clause_list, variable_number):
        """
        This is a static method that returns a list containing information about a variable position
        in a clause list.
        The returned list consists of a tuple in like this (clause index, variable index
        in the clause variables list)
        :param clause_list:
        :param variable_number:
        :return:
        """
        variable_position = list()
        clause_list_index = 0
        for clause in clause_list:
            clause_variables_index = 0
            for variable in clause:
                if (variable == variable_number) or ((-1 * variable) == variable_number):
                    variable_position.append((clause_list_index, clause_variables_index))
                clause_variables_index += 1
            clause_list_index += 1
        return variable_position
