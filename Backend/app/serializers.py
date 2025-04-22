from datetime import time, date
from .models import db, Contact, Event, Project, News, Publications, Organisation, Magazine, Author



def serialize_author(author: Author):
    return {
        'id': author.id,
        'first_name': author.first_name,
        'first_name_en': author.first_name_en,
        'middle_name': author.middle_name,
        'middle_name_en': author.middle_name_en,
        'last_name': author.last_name,
        'last_name_en': author.last_name_en
    }

def serialize_news(news: News):
    return {
        'id': news.id,
        'title': news.title,
        'title_en': news.title_en,
        'authors': [serialize_author(author) for author in news.authors],
        'publication_date': news.publication_date,
        'description': news.description,
        'description_en': news.description_en,
        'magazine': {
            'name': news.magazine.name,
            'name_en': news.magazine.name_en
        } if news.magazine else None,
        'content': news.content,
        'content_en' : news.content_en,
        'materials': f"/uploads/{news.materials}" if news.materials else None
    }

def serialize_events(event: Event):
    return {
        'id': event.id,
        'title': event.title,
        'title_en': event.title_en,
        'publication_date': event.publication_date,
        'location': event.location,
        'description': event.description,
        'description_en': event.description_en
    }

def serialize_projects(project: Project):
    return {
        'id': project.id,
        'title': project.title,
        'title_en': project.title_en,
        'authors': [serialize_author(author) for author in project.authors],
        'publication_date': project.publication_date,
        'description': project.description,
        'description_en': project.description_en,
        'content': project.content,
        'content_en': project.content_en,
        'materials': f"/uploads/{project.materials}" if project.materials else None
    }

def serialize_publications(publication: Publications):
    return {
        'id': publication.id,
        'title': publication.title,
        'title_en': publication.title_en,
        'authors': [serialize_author(author) for author in publication.authors],
        'publication_date': publication.publication_date,
        'magazine': {
            'name': publication.magazine.name,
            'name_en': publication.magazine.name_en
        } if publication.magazine else None,
        'annotation': publication.annotation,
        'annotation_en': publication.annotation_en
    }

def serialize_organisations(organisation: Organisation):
    return {
        'id': organisation.id,
        'image': organisation.image,
        'link': organisation.link
    }

def serialize_magazine(magazine: Magazine):
    return {
        'id': magazine.id,
        'name': magazine.name,
        'name_en': magazine.name_en
    }