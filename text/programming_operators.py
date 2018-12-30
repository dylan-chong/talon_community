from talon.voice import Context, Key

ctx = Context("programming_operators")

ctx.keymap({
    "(op equals | assign | equeft)": " = ",
    "(op (minus | subtract) | deminus)": " - ",
    "(op (plus | add) | deplush)": " + ",
    "(op (times | multiply) | duster)": " * ",
    "(op divide | divy)": " / ",
    "op mod": " % ",
    "[op] (minus | subtract) equals": " -= ",
    "[op] (plus | add) equals": " += ",
    "[op] (times | multiply) equals": " *= ",
    "[op] divide equals": " /= ",
    "[op] mod equals": " %= ",
    "(op | is) greater [than]": " > ",
    "(op | is) less [than]": " < ",
    "(op | is) equal": " == ",
    "(op | is) not equal": " != ",
    "(op | is) greater [than] or equal": " >= ",
    "(op | is) less [than] or equal": " <= ",
    "(op (power | exponent) | to the power [of])": " ** ",
    "op and": " && ",
    "op or": " || ",
    "[op] (logical | bitwise) and": " & ",
    "[op] (logical | bitwise) or": " | ",
    "(op | logical | bitwise) (ex | exclusive) or": " ^ ",
    "[(op | logical | bitwise)] (left shift | shift left)": " << ",
    "[(op | logical | bitwise)] (right shift | shift right)": " >> ",
    "(op | logical | bitwise) and equals": " &= ",
    "(op | logical | bitwise) or equals": " |= ",
    "(op | logical | bitwise) (ex | exclusive) or equals": " ^= ",
    "[(op | logical | bitwise)] (left shift | shift left) equals": " <<= ",
    "[(op | logical | bitwise)] (right shift | shift right) equals": " >>= ",
})
