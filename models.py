from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self._available = True

    @property
    def available(self):
        return self._available

    def mark_borrowed(self):
        if not self._available:
            raise ValueError("Item is already borrowed.")
        self._available = False

    def mark_returned(self):
        self._available = True

    @abstractmethod
    def loan_period_days(self):
        pass


class Book(LibraryItem):
    def loan_period_days(self):
        return 14


class Magazine(LibraryItem):
    def loan_period_days(self):
        return 7


class ReferenceBook(LibraryItem):
    def loan_period_days(self):
        return 0


class Member:
    def __init__(self, member_id, name, borrowing_limit=3):
        self.member_id = member_id
        self.name = name
        self.borrowing_limit = borrowing_limit
        self._active_loans = set()

    @property
    def active_loans(self):
        return frozenset(self._active_loans)

    def can_borrow(self):
        return len(self._active_loans) < self.borrowing_limit

    def add_loan(self, item_id):
        if not self.can_borrow():
            raise ValueError("Borrowing limit exceeded.")
        self._active_loans.add(item_id)

    def remove_loan(self, item_id):
        self._active_loans.discard(item_id)


class StudentMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, 3)


class ResearchStudent(StudentMember):
    def __init__(self, member_id, name):
        super().__init__(member_id, name)
        self.borrowing_limit = 5


class FacultyMember(Member):
    def __init__(self, member_id, name):
        super().__init__(member_id, name, 5)


class NotificationMixin:
    def send_notice(self, message):
        print(f"NOTIFICATION: {message}")


class NotifiedMember(Member, NotificationMixin):
    pass