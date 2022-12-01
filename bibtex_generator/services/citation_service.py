class Citation_service:
    def __init__(self, name, title, published, author):
        self.name = name
        self.title = title
        self.published = published
        self.author = author

    def get_values(self):
        result = db.session.execute(
            "SELECT citation_name, title, published, author FROM citations")
        citations = result.fetchall()
        return citations