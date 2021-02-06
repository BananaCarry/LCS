import Operations as op
from typing import Dict

def is_1_param_op(c):
    return c == '!'

def is_2_param_op(c):
    return c in "&|>="

def is_op(c):
    return is_1_param_op(c) or is_2_param_op(c)

def is_atom(n):
    return len(n) == 1 and n.isupper()

class Proposition:
    def __str__(self):
        def generate(prop):
            if is_atom(prop):
                return prop
            elif len(prop) == 2:
                return "(" + prop[0] + generate(prop[1]) + ")"
            elif len(prop) == 3:
                return "(" + generate(prop[0]) + prop[1] + generate(prop[2]) + ")"
        return generate(self.prop)

    def __init__(self,prop,atoms=None):
        self.prop = None

        if type(prop) == type(""):                                                                                      #Checking to find out the way to analyze the prop
            self.atoms = set()
            prop = prop.strip()
            if len(prop) == 1:
                self.prop = prop
                self.atoms.add(prop)
            else:
                it = iter(prop)
                next(it)                                                                                                #First parenthesis skipping
                def process(it):                                                                                        #Processing phase
                    result = []
                    while True:
                        c = next(it)
                        if c == '(':
                            result.append(process(it))
                        elif c == ')':
                            if len(result) == 2:
                                assert(is_1_param_op(result[0]))
                            elif len(result) == 3:
                                assert(is_2_param_op(result[1]))
                            return result
                        elif is_op(c):
                            result.append(c)
                        elif is_atom(c):
                            result.append(c)
                        elif c == ' ':
                            pass
                        elif c == '¬':
                            result.append('!')
                        elif c == '∧':
                            result.append('&')
                        elif c == '∨':
                            result.append('|')
                        elif c == '≡':
                            result.append('=')
                        elif c == '⇒':
                            result.append('>')
                        else:
                            raise ValueError(f"Invalid character: {c}")                                                 #In case it goes BOOM, stops nicely, hope nobody will read this text, lol
                self.prop = process(it)
        else:
            self.prop = prop

        if atoms is None:
            def calc_atom(prop):
                if is_atom(prop):
                    self.atoms.add(prop)
                elif len(prop) == 2:
                    calc_atom(prop[1])
                elif len(prop) == 3:
                    calc_atom(prop[0])
                    calc_atom(prop[2])
            calc_atom(self.prop)
            self.atoms = list(sorted(self.atoms))
        else:
            self.atoms = atoms

    def all_subprops(self):                                                                                              #If called, it shows the steps on linear style
        def generate(prop):
            if is_atom(prop):
                return
            elif len(prop) == 2:
                yield from generate(prop[1])
            elif len(prop) == 3:
                yield from generate(prop[0])
                yield from generate(prop[2])
            yield Proposition(prop, self.atoms)
        return generate(self.prop)

    def values(self):
        count = len(self.atoms)
        def generate(l):
            if len(l) == count:
                yield l
            else:
                for elem in [False, True]:
                    yield from generate(l + [elem])
        return generate([])

    def eval(self, values: Dict[str,bool]):
        def generate(p):
            if is_atom(p):
                return values[p]
            elif len(p) == 2:
                if p[0] == "!":
                    return op.negate(generate(p[1]))
            elif len(p) == 3:
                if p[1] == "&":
                    return op.conjuction(generate(p[0]), generate(p[2]))
                if p[1] == "|":
                    return op.disjunction(generate(p[0]), generate(p[2]))
                if p[1] == ">":
                    return op.implies(generate(p[0]), generate(p[2]))
                if p[1] == "=":
                    return op.equivalence(generate(p[0]), generate(p[2]))
        return generate(self.prop)