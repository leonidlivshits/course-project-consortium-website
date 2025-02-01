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
def serialize_events(event : Event):
    return {
            'id': event.id,
            'title': event.title,
            'date': event.date,
            'time': event.time,
            'location': event.location,
            'description': event.description
        }
def serialize_projects(project : Project):
    return {
            'id': project.id,
            'title': project.title,
            'authors': [serialize_author(author) 
                        for author in project.authors],
            'publication_date': project.publication_date,
            'description': project.description,
            'content': project.content,
            'materials': f"/uploads/{project.materials}"
        }
def serialize_publications(publication : Publications):
    return {
            'id': publication.id,
            'title': publication.title,
            'authors': [serialize_author(author) 
                        for author in publication.authors],
            'publication_date': publication.publication_date,
            'magazine': publication.magazine.name if publication.magazine else None,
            'annotation': publication.annotation
        }
def serialize_organisations(organisation : Organisation):
    return {
            'id': organisation.id,
            'image': organisation.image,
            'link': organisation.link
        }