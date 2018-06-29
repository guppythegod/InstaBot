from instapy import instapy

class InstapyClient:
    def __init__(self, username, password, niches, comments, comment_percentage, like_percentage):
        self.username  = username
        self.password = password
        self.niches = niches
        self.like_percentage = like_percentage
        session = instapy(username=self.username,password=self.password,nogui=True)
        session.login()
        session.set_do_comments(True, percentage=comment_percentage)
        session.set_comments(comments)
        session.set_do_like(enabled=True, percentage=self.like_percentage)
    
    def like():
        session.like_by_tags(self.niche, amount=500)
        
    def follow():
        pass
    