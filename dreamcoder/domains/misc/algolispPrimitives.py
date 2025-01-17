# napsPrimitives.py
from dreamcoder.program import Primitive, Program
from dreamcoder.grammar import Grammar
from dreamcoder.type import tlist, arrow, baseType  # , t0, t1, t2

# from functools import reduce


# Internal TYPES:
# NUMBER
# BOOLEAN
# NOTFUNCTYPE
# Type
# ANYTYPE

# types
tsymbol = baseType("symbol")
# PROGRAM = SYMBOL = constant | argument | function_call | function | lambda
tconstant = baseType("constant")
tfunction = baseType("function")

f = dict(
    [
        ("|||", "triple_or"),
        ("reduce", "reduce"),
        ("+", "+"),
        ("len", "len"),
        ("map", "map"),
        ("filter", "filter"),
        ("-", "-"),
        ("*", "*"),
        ("partial0", "partial0"),
        ("if", "if"),
        ("lambda1", "lambda1"),
        ("==", "eq"),
        ("range", "range"),
        ("digits", "digits"),
        ("slice", "slice"),
        ("reverse", "reverse"),
        ("lambda2", "lambda2"),
        ("deref", "deref"),
        ("partial1", "partial1"),
        ("/", "div"),
        ("<", "less_than"),
        (">", "greater_than"),
        ("min", "min"),
        ("combine", "combine"),
        ("head", "head"),
        ("is_prime", "is_prime"),
        ("false", "false"),
        ("||", "or"),
        ("10", "10"),
        ("self", "self"),
        ("max", "max"),
        ("sort", "sort"),
        ("%", "mod"),
        ("invoke1", "invoke1"),
        ("!", "bang"),
        ("square", "square"),
        ("str_concat", "str_concat"),
        ("strlen", "strlen"),
        ("<=", "leq"),
        ("int-deref", "int-deref"),
        ("str_split", "str_split"),
        ("str_index", "str_index"),
        ("floor", "floor"),
        ("sqrt", "sqrt"),
        ("str_min", "str_min"),
        ("&&", "AND"),
        ("is_sorted", "is_sorted"),
        ("str_max", "str_max"),
        (">=", "geq"),
    ]
)

fn_lookup = {**f}

c = dict(
    [
        ("0", "0"),
        ("a", "a"),
        ("arg1", "arg1"),
        ("1", "1"),
        ("b", "b"),
        ("2", "2"),
        ("c", "c"),
        ("arg2", "arg2"),
        ("d", "d"),
        ("false", "false"),
        ("10", "10"),
        ("self", "self"),
        ("1000000000", "1000000000"),
        ('""', "empty_str"),
        ("e", "e"),
        ("40", "40"),
        ("f", "f"),
        ('" "', "space"),
        ("g", "g"),
        ('"z"', "z"),
        ("true", "true"),
        ("h", "h"),
        ("i", "i"),
        ("j", "j"),
        ("k", "k"),
        ("l", "l"),
    ]
)

const_lookup = {**c}

primitive_lookup = {**const_lookup, **fn_lookup}
# Do i need arguments??


def _fn_call(f):
    # print("f", f)
    def inner(sx):
        # print("sx", sx)
        if not type(sx) == list:
            sx = [sx]
        return [f] + sx

    return lambda sx: inner(sx)


def algolispPrimitives():
    return (
        [
            Primitive("fn_call", arrow(tfunction, tlist(tsymbol), tsymbol), _fn_call),
            Primitive(
                "lambda1_call",
                arrow(tfunction, tlist(tsymbol), tsymbol),
                lambda f: lambda sx: ["lambda1", [f] + sx]
                if type(sx) == list
                else ["lambda1", [f] + [sx]],
            ),
            Primitive(
                "lambda2_call",
                arrow(tfunction, tlist(tsymbol), tsymbol),
                lambda f: lambda sx: ["lambda2", [f] + sx]
                if type(sx) == list
                else ["lambda2", [f] + [sx]],
            ),
            # symbol converters:
            # SYMBOL = constant | argument | function_call | function | lambda
            Primitive("symbol_constant", arrow(tconstant, tsymbol), lambda x: x),
            Primitive("symbol_function", arrow(tfunction, tsymbol), lambda x: x),
            # list converters
            Primitive(
                "list_init_symbol",
                arrow(tsymbol, tlist(tsymbol)),
                lambda symbol: [symbol],
            ),
            Primitive(
                "list_add_symbol",
                arrow(tsymbol, tlist(tsymbol), tlist(tsymbol)),
                lambda symbol: lambda symbols: symbols + [symbol]
                if type(symbols) == list
                else [symbols] + [symbol],
            ),
        ]
        + [
            # functions:
            Primitive(ec_name, tfunction, algo_name)
            for algo_name, ec_name in fn_lookup.items()
        ]
        + [
            # Constants
            Primitive(ec_name, tconstant, algo_name)
            for algo_name, ec_name in const_lookup.items()
        ]
    )


# for first pass, can just hard code vars and maps n stuff


def algolispProductions():
    return [(0.0, prim) for prim in algolispPrimitives()]


algolisp_input_vocab = [
    "<S>",
    "</S>",
    "<UNK>",
    "|||",
    "(",
    ")",
    "a",
    "b",
    "of",
    "the",
    "0",
    ",",
    "arg1",
    "c",
    "and",
    "1",
    "reduce",
    "+",
    "int[]",
    "in",
    "given",
    "numbers",
    "int",
    "is",
    "len",
    "map",
    "digits",
    "d",
    "number",
    "array",
    "-",
    "filter",
    "to",
    "range",
    "are",
    "*",
    "partial0",
    "2",
    "if",
    "reverse",
    "that",
    "elements",
    "lambda1",
    "==",
    "an",
    "arg2",
    "values",
    "slice",
    "element",
    "lambda2",
    "deref",
    "you",
    "partial1",
    "e",
    "find",
    "your",
    "task",
    "compute",
    "among",
    "from",
    "consider",
    "first",
    "than",
    "value",
    "/",
    "what",
    "arrays",
    "with",
    "<",
    "length",
    ">",
    "be",
    "min",
    "end",
    "sum",
    "one",
    "head",
    "f",
    "by",
    "combine",
    "segment",
    "coordinates",
    "not",
    "string",
    "is_prime",
    "false",
    "||",
    "at",
    "10",
    "half",
    "position",
    "self",
    "subsequence",
    "after",
    "such",
    "max",
    "prime",
    "sort",
    "let",
    "%",
    "longest",
    "inclusive",
    "which",
    "invoke1",
    "1000000000",
    "all",
    "positions",
    "!",
    "square",
    "its",
    "has",
    "reversed",
    "another",
    "less",
    "each",
    '""',
    "order",
    "largest",
    "maximum",
    "g",
    "last",
    "smallest",
    "times",
    "strictly",
    "40",
    "smaller",
    "indexes",
    "str_concat",
    "strlen",
    "two",
    "starting",
    "<=",
    "on",
    "greater",
    "how",
    "many",
    "int-deref",
    "prefix",
    "bigger",
    "only",
    "str_split",
    '" "',
    "str_index",
    "can",
    "plus",
    "squared",
    "product",
    "strings",
    "floor",
    "sqrt",
    "before",
    "it",
    "concatenation",
    "index",
    "as",
    "define",
    "multiplied",
    "biggest",
    "rounded",
    "down",
    "string[]",
    "equal",
    "integer",
    "also",
    "based",
    "sorting",
    "replace",
    "becomes",
    "single",
    "digit",
    "characters",
    "keeping",
    "including",
    "h",
    "larger",
    "written",
    "divisible",
    "previous",
    "subarray",
    "mininum",
    "second",
    "middle",
    "same",
    "th",
    "median",
    "till",
    "integers",
    "sequence",
    "for",
    "indices",
    "between",
    "when",
    "doubled",
    "ending",
    "even",
    "multiply",
    "squares",
    "fibonacci",
    "exclusive",
    "odd",
    "keep",
    "whether",
    "minimum",
    "except",
    "letters",
    "appearing",
    "letter",
    "consecutive",
    "character",
    "factorial",
    "chosen",
    "start",
    "begin",
    "themselves",
    '"z"',
    "str_min",
    "remove",
    "present",
    "exist",
    "appear",
    "starts",
    "i",
    "located",
    "true",
    "&&",
    "found",
    "discarding",
    "is_sorted",
    "removing",
    "do",
    "increasing",
    "exceed",
    "ascending",
    "difference",
    "decremented",
    "existing",
    "alphabetically",
    "words",
    "added",
    "incremented",
    "backwards",
    "individual",
    "lexicographically",
    "separate",
    "abbreviation",
    "str_max",
    "increment",
    "consisting",
    "equals",
    "having",
    "discard",
    "descending",
    "decreasing",
    "sorted",
    "being",
    "where",
    "right",
    "there",
    "ordinal",
    "have",
    "s",
    "going",
    "'",
    "add",
    "space",
    "decrement",
    "those",
    "whitespaces",
    "spaces",
    "subtract",
    "remaining",
    "following",
    "or",
    "out",
    "ordered",
    "minimal",
    "itself",
    "symmetric",
    "read",
    "increases",
    "word",
    "immidiately",
    "excluding",
    "j",
    "omitting",
    "reads",
    "maximal",
    ">=",
    "compare",
    "form",
    "absent",
    "missing",
    "cannot",
    "whose",
    "count",
    "lowest",
    "both",
    "ends",
    "beginning",
    "left",
    "mean",
    "average",
    "obtained",
    "writing",
    "result",
    "joining",
    "together",
    "increase",
    "highest",
    "comparing",
    "forms",
    "avg",
    "outside",
    "positive",
    "summed",
    "belonging",
    "lexicographical",
    "rest",
    "belong",
    "inclucing",
    "lexical",
    "alphabetical",
    "dictionary",
    "k",
    "negative",
    "lexicographic",
    "represents",
    "delete",
    "non",
    "l",
    "erase",
    "m",
    "comes",
    "up",
    "comparison",
    "during",
    "'s value is the largest inclusive, which is strictly less than maximum element in numbers from 1 to the element in `a` which'",
    "'s value is the biggest (inclusive), which is strictly less than maximum element of range from 1 to the element in `a` which'",
    "'s value is the highest, which is strictly less than maximum element among sequence of digits of the element in `a` which'",
]


if __name__ == "__main__":
    # g = Grammar.uniform(deepcoderPrimitives())

    g = Grammar.fromProductions(algolispProductions(), logVariable=0.9)

    # p=Program.parse("(lambda (fn_call filter (list_add_symbol (lambda1_call == (list_add_symbol 1 (list_init_symbol (fn_call mod ( list_add_symbol 2 (list_init_symbol arg1)) ))) ) (list_init_symbol $0)) )")
    p = Program.parse(
        "(lambda (fn_call filter (list_add_symbol (lambda1_call eq (list_add_symbol (symbol_constant 1) (list_init_symbol (fn_call mod ( list_add_symbol (symbol_constant 2) (list_init_symbol (symbol_constant arg1))) ))) ) (list_init_symbol (symbol_constant $0)))))"
    )

    print(p)

    # tree = p.evaluate(["a"])
    tree = p.evaluate([])
    print(tree("a"))

#
