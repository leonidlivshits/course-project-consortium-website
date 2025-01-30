from .models import db, Contact, Event, Project, News, Publications, Organisation, Magazine, Author

def serialize_author(author : Author):
    
    return f"{author.last_name} {get_initials(author)}"

def get_initials(author : Author):
    return f"{author.first_name[0]}.{author.middle_name[0] if author.middle_name else ''}"

def serialize_news(news : News):
    return {
            'id': news.id,
            'title': news.title,
            'authors': [serialize_author(author) 
                        for author in news.authors],
            'publication_date': news.publication_date,
            'description': news.description,
            'magazine': news.magazine.name if news.magazine else None,
            'content': news.content,
            'materials': f"/uploads/{news.materials}" 
        }
    