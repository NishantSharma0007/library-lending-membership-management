from datetime import date, timedelta


class LibraryManager:
    library_name = "My Python Library"
    max_active_loans_default = 3
    FINE_PER_DAY = 5

    def __init__(self):
        self.items = {}
        self.members = {}
        self.loans = {}

    @classmethod
    def set_policy(cls, limit):
        if limit < 1:
            raise ValueError("Limit must be at least 1.")
        cls.max_active_loans_default = limit

    @staticmethod
    def calculate_fine(overdue_days):
        return max(0, overdue_days) * LibraryManager.FINE_PER_DAY

    def register_item(self, item):
        if item.item_id in self.items:
            raise ValueError("Item ID already exists.")
        self.items[item.item_id] = item

    def register_member(self, member):
        if member.member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member.member_id] = member

    def borrow_item(self, member_id, item_id):
        if member_id not in self.members:
            raise ValueError("Member not found.")

        if item_id not in self.items:
            raise ValueError("Item not found.")

        member = self.members[member_id]
        item = self.items[item_id]

        if not item.available:
            raise ValueError("Item is not available.")

        if item.loan_period_days() <= 0:
            raise ValueError("This item cannot be borrowed.")

        if not member.can_borrow():
            raise ValueError("Borrowing limit exceeded.")

        issue_date = date.today()
        due_date = issue_date + timedelta(
            days=item.loan_period_days()
        )

        item.mark_borrowed()
        member.add_loan(item_id)

        self.loans[item_id] = {
            "member_id": member_id,
            "issue_date": issue_date.isoformat(),
            "due_date": due_date.isoformat()
        }

        if isinstance(member, NotificationMixin):
            member.send_notice(f"Item {item_id} borrowed successfully.")

        print("Borrow successful!")
        print("Due date:", due_date)

    def return_item(self, item_id):
        if item_id not in self.loans:
            raise ValueError("No active loan found.")

        loan = self.loans[item_id]
        due_date = date.fromisoformat(loan["due_date"])
        overdue_days = max(0, (date.today() - due_date).days)
        fine = self.calculate_fine(overdue_days)

        member = self.members[loan["member_id"]]
        member.remove_loan(item_id)
        self.items[item_id].mark_returned()

        del self.loans[item_id]

        print("Item returned successfully!")
        print("Overdue days:", overdue_days)
        print("Fine: Rs.", fine)

    def show_reports(self):
        print("\n--- ALL ITEMS ---")
        for item in self.items.values():
            print(item.item_id, item.title,
                  "Available:", item.available)

        print("\n--- AVAILABLE ITEMS ---")
        for item in self.items.values():
            if item.available:
                print(item.item_id, item.title)

        print("\n--- ACTIVE LOANS ---")
        for item_id, loan in self.loans.items():
            print(item_id, loan["member_id"],
                  "Due:", loan["due_date"])

        print("\n--- OVERDUE LOANS ---")
        today = date.today()
        for item_id, loan in self.loans.items():
            due = date.fromisoformat(loan["due_date"])
            if due < today:
                print(item_id, "Overdue by",
                      (today - due).days, "days")

        print("\n--- MEMBERS ---")
        for member in self.members.values():
            print(member.member_id, member.name,
                  "Borrowed:", len(member.active_loans))