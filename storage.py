import json
import os

from models import (
    Book, Magazine, ReferenceBook,
    StudentMember, ResearchStudent,
    FacultyMember, NotifiedMember
)

ITEM_TYPES = {
    "Book": Book,
    "Magazine": Magazine,
    "ReferenceBook": ReferenceBook
}

MEMBER_TYPES = {
    "StudentMember": StudentMember,
    "ResearchStudent": ResearchStudent,
    "FacultyMember": FacultyMember,
    "NotifiedMember": NotifiedMember
}