from rest_framework.pagination import LimitOffsetPagination

class StructurePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100