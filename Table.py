from Pisici import Proposition
from itertools import count

def table_gen(p):
    p = Proposition(p)
    table = []

    #first row
    row = ["#"]
    for atom in p.atoms:
        row.append(atom)
    for subprop in p.all_subprops():
        row.append(str(subprop).replace("!","¬").replace("&", "∧").replace("|", "∨").replace("=", "≡").replace(">", "⇒"))
    table.append(row)

    #results
    for i,val in zip(count(1),p.values()):
        row = [i]
        row += val
        for subprop in p.all_subprops():
            values = {}
            for key,value in zip(p.atoms,val):
                values[key] = value
            row.append(subprop.eval(values))
        table.append(row)
    return table
