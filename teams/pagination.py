from rest_framework.pagination import PageNumberPagination


class PlayersPagination(PageNumberPagination):
    page_size = 26
    page_size_query_param = 'page_size'
    max_page_size = 26