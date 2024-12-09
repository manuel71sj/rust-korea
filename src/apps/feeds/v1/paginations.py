from rest_framework.pagination import CursorPagination


class FeedCursorPagination(CursorPagination):
    """피드 페이지네이션"""

    ordering = "-published_at"
    page_size = 10
