from app import db

paper_author = db.Table(
    "paper_author",
    db.Column("authorId", db.String(), db.ForeignKey('author.id'), primary_key=True),
    db.Column("paperId", db.String(), db.ForeignKey('paper.id'), primary_key=True),
)
