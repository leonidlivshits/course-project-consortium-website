import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
// import './ProjectDetails.css';
// import './EventDetail.css';
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const PublicationDetails = () => {
  const { id } = useParams();
  const [publication, setPublications] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/publications/${id}`)
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
    <section className="project-details">
      <Navbar />
      <div className="container">
        <h2>{publication.title}</h2>
        <p><strong>Авторы:</strong> {publication.authors.join(', ')}</p>
        <p><strong>Дата публикации:</strong> {publication.publication_date}</p>
        <p><strong>Журнал:</strong> {publication.magazine || "Не указан"}</p>
        <p><strong>Описание:</strong> {publication.annotation}</p>
      </div>
      <Footer />
    </section>
  );
};

export default PublicationDetails;