class ValidationTargetType(object):
    BLOCK = 'BLOCK'
    GRAPH = 'GRAPH'
    INPUT = 'INPUT'
    NODE = 'NODE'
    PARAMETER = 'PARAMETER'
    PROPERTY = 'PROPERTY'


class ValidationCode(object):
    IN_DEPENDENTS = 'IN_DEPENDENTS'
    MISSING_INPUT = 'MISSING_INPUT'
    MISSING_PARAMETER = 'MISSING_PARAMETER'
    INVALID_VALUE = 'INVALID_VALUE'
    MINIMUM_COUNT_MUST_NOT_BE_NEGATIVE = 'MINIMUM_COUNT_MUST_NOT_BE_NEGATIVE'
    MINIMUM_COUNT_MUST_BE_GREATER_THAN_MAXIMUM = 'MINIMUM_COUNT_MUST_BE_GREATER_THAN_MAXIMUM'
    MAXIMUM_COUNT_MUST_NOT_BE_ZERO = 'MAXIMUM_COUNT_MUST_NOT_BE_ZERO'
    DEPRECATED_NODE = 'DEPRECATED_NODE'
