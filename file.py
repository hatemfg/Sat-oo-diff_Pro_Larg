__author__ = 'ryuzakinho'
import re
import copy
from Variable import Variable


class File(object):
    """
    This class represents a cnf file whith the following attributes:
    opening_type : str
    filneame : str
    """
    opening_type = 'r'

    def __init__(self, filename):
        """
        :param filename: str
        """
        self.filename = filename

    @property
    def get_file_info(self):
        """
        gets filename and opening types to gather information about cnf.
        :rtype : dict
        """
        clause_length = None
        with open(self.filename, self.opening_type) as f_handler:
            for line in f_handler:
                line = line.lstrip()
                find = re.search("clause length\s*=\s*([0-9]+)", line)
                if find is not None:
                    clause_length = find.group(1)
                    continue
                find = re.search("\s*p cnf ([0-9]+)\s*([0-9]+)", line)
                if find is not None:
                    nbr_variable = find.group(1)
                    nbr_clause = find.group(2)
                    return {"nbr_clause": int(nbr_clause), "nbr_variable": int(nbr_variable),
                            "clause_length": int(clause_length)}

    @property
    def get_clause_info(self):
        """
        This method opens a cnf file and gathers data about clauses (clause number, variables).
        It returns a list giving information about clauses.
        :rtype : list
        """
        list_clause = list()
        buffer_clause = list()
        with open(self.filename, self.opening_type) as file_handler:
            clause_length = self.get_file_info['clause_length']
            for line in file_handler:
                line.lstrip()  # We get rid of blanks at the beginning of the line
                find = re.search("([-]?[0-9]+)\s*([-]?[0-9]+)\s*([-]?[0-9]+)\s*0", line)
                if find is not None:
                    for i in range(1, clause_length + 1):
                        variable = find.group(i)
                        buffer_clause.append(int(variable))
                    list_clause.append(copy.deepcopy(buffer_clause))
                    del buffer_clause[:]
        return list_clause
