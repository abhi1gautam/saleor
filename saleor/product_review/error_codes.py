from enum import Enum


class ProductReviewErrorCode(str, Enum):
    GRAPHQL_ERROR = "graphql_error"
    INVALID = "invalid"
    NOT_FOUND = "not_found"
    REQUIRED = "required"
    UNIQUE = "unique"
    ALREADY_REVIEWED = "already_reviewed"
