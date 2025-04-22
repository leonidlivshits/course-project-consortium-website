import React, { useContext, useEffect, useState } from "react";
import { LanguageContext } from "../../components/LanguageContext/LanguageContext";
import { useParams } from 'react-router-dom';
import '../Events/EventDetail.css';
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const PublicationDetails = () => {
  const { id } = useParams();
  const { language } = useContext(LanguageContext);
  const [publication, setPublications] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    //fetch(`http://127.0.0.1:5000/api/publications/${id}`)
    fetch(`${process.env.REACT_APP_API_URL}/publications/${id}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Публикация не найдена');
        }
        return response.json();
      })
      .then(data => {
        setPublications(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Ошибка при загрузке публикации:', error);
        setError(error.message);
        setLoading(false);
      });
  }, [id]);

  const formatAuthors = (authors) => {
    return authors.map(author => {
      const firstName = author[`first_name_${language}`] || author.first_name;
      const lastName = author[`last_name_${language}`] || author.last_name;
      return `${firstName} ${lastName}`;
    }).join(', ');
  };

  if (loading) {
    return <div>Загрузка...</div>;
  }

  if (error) {
    return <div>Ошибка: {error}</div>;
  }

  if (!publication) {
    return <div>Публикация не найдена</div>;
  }

  return (
    <section className="event-detail">
      <Navbar />
      <div className="container">
        <h2>{publication[`title_${language}`] || publication.title}</h2>
        <p><strong>{language === 'ru' ? 'Авторы: ' : 'Authors: '}</strong> {formatAuthors(publication.authors)}</p>
        <p><strong>{language === 'ru' ? 'Дата публикации: ' : 'Publication Date: '}</strong> 
        {new Date(publication.publication_date).toLocaleDateString(language === 'ru' ? 'ru-RU' : 'en-US')}
        </p>
        {publication.magazine && (
        <p><strong>{language === 'ru' ? 'Журнал: ' : 'Journal: '}</strong> 
        {publication.magazine[`name_${language}`] || publication.magazine.name }
        </p>
        )}
        <p><strong>{language === 'ru' ? 'Описание: ' : 'Abstract: '}</strong> 
        {publication[`annotation_${language}`] || publication.annotation}
        </p>
      </div>
      <Footer />
    </section>
  );
};

export default PublicationDetails;