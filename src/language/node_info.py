"""Define node and data types used in parser and ast generator

While generating ast and visitors we need to lookup for base data types,
nmodl blocks defining variables, nmodl constructs that define variables
etc. These all data types are defined in this file.

\todo : Other way is to add extra attributes to YAML language definitions.
YAML will  become more verbose but advantage would be that the YAML will be
self sufficien, single definition file instead of hard-coded names here.
We should properties like is_enum, data_type, is_symbol, is_global etc.
"""

# yapf: disable
BASE_TYPES = ["short",
              "int",
              "float",
              "double",
              "std::string",
              "BinaryOp",
              "UnaryOp",
              "ReactionOp",
              "FirstLastType",
              "QueueType",
              "BAType",
              "UnitStateType"]

# base types which are enums
ENUM_BASE_TYPES = ["BinaryOp",
                   "UnaryOp",
                   "ReactionOp",
                   "FirstLastType",
                   "QueueType",
                   "BAType",
                   "UnitStateType"]

# data types and then their return types
DATA_TYPES = {"Boolean": "bool",
              "Integer": "int",
              "Float": "float",
              "Double": "double",
              "String": "std::string",
              "BinaryOperator": "BinaryOp",
              "UnaryOperator": "UnaryOp",
              "ReactionOperator": "ReactionOp",
              "UnitState": "UnitStateType",
              "BABlockType": "BAType",
              "QueueExpressionType": "QueueType",
              "FirstLastTypeIndex": "FirstLastType"}

# nodes which will go into symbol table
SYMBOL_VAR_TYPES = ["LocalVar",
                    "ParamAssign",
                    "Argument",
                    "DependentDef",
                    "UnitDef",
                    "FactorDef",
                    "RangeVar",
                    "ReadIonVar",
                    "WriteIonVar",
                    "NonspeCurVar",
                    "ElectrodeCurVar",
                    "SectionVar",
                    "GlobalVar",
                    "PointerVar",
                    "BbcorePointerVar",
                    "ExternVar",
                    "PrimeName"]

# block nodes which will go into symbol table
SYMBOL_BLOCK_TYPES = ["FunctionBlock",
                      "ProcedureBlock",
                      "DerivativeBlock",
                      "LinearBlock",
                      "NonLinearBlock",
                      "DiscreteBlock",
                      "PartialBlock",
                      "KineticBlock",
                      "FunctionTableBlock"]

# blocks defining global variables
GLOBAL_BLOCKS = ["NeuronBlock",
                 "ParamBlock",
                 "UnitBlock",
                 "StepBlock",
                 "IndependentBlock",
                 "DependentBlock",
                 "StateBlock",
                 "ConstantBlock"]

# when translating back to nmodl, we need print each statement
# to new line. Those nodes are are used from this list.
STATEMENT_TYPES=["Statement",
                 "IndependentDef",
                 "DependentDef",
                 "ParamAssign",
                 "ConstantStatement"]

# data types which have token as an argument to the constructor
LEXER_DATA_TYPES = ["Name",
                    "PrimeName",
                    "Integer",
                    "Double",
                    "String",
                    "FactorDef"]

# while printing symbol table we needed setToken() method for StatementBlock and
# hence need to add this
ADDITIONAL_TOKEN_BLOCKS = ["StatementBlock"]

# for printing NMODL, we need to know which nodes are block types.
# TODO: NEURON block is removed because it has internal statement block
# and we don't want to print extra brace block for NMODL
# We are removing NeuronBlock because it has statement block which
# prints braces already.
BLOCK_TYPES = (GLOBAL_BLOCKS + ADDITIONAL_TOKEN_BLOCKS)
BLOCK_TYPES.remove("NeuronBlock")

# Note that these are nodes which are not of type pointer in AST.
# This also means that they can't be optional because they will appear
# as value type in AST.
PTR_EXCLUDE_TYPES = ["BinaryOperator", "UnaryOperator", "ReactionOperator"]

# these node names are explicitly added because they are used in ast/visitor
# printer classes. In otder to avoid hardcoding in the printer functions, they
# are defined here.
PROGRAM_BLOCK = "Program"
BASE_BLOCK = "Block"
PRIME_NAME_NODE = "PrimeName"
STRING_NODE = "String"
NUMBER_NODE = "Number"
IDENTIFIER_NODE = "Identifier"
NAME_NODE = "Name"
BOOLEAN_NODE = "Boolean"
INTEGER_NODE = "Integer"
REACTION_STATEMENT_NODE = "ReactionStatement"
CONSERVE_NODE = "Conserve"
EXPRESSION_NODE = "Expression"
BINARY_EXPRESSION_NODE = "BinaryExpression"
UNARY_EXPRESSION_NODE = "UnaryExpression"
VERBATIM_NODE = "Verbatim"
COMMENT_NODE = "Comment"
INDEPENDENTDEF_NODE = "IndependentDef"
STATEMENT_BLOCK_NODE = "StatementBlock"
UNIT_BLOCK = "UnitBlock"

# name of variable in prime node which represent order of derivative
ORDER_VAR_NAME = "order"
REACT_VAR_NAME = "react"
REACT2_VAR_NAME = "react2"
SWEEP_VAR_NAME = "sweep"

# yapf: enable