import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
// import './ProjectDetails.css';
// import './EventDetail.css';
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const NewsDetails = () => {
  const { id } = useParams();
  const [news, setNews] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/api/news/${id}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Новость не найдена');
        }
        return response.json();
      })
      .then(data => {
        setNews(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Ошибка при загрузке новости:', error);
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

  if (!news) {
    return <div>Новость не найдена</div>;
  }

  return (
    <section className="project-details">
      <Navbar />
      <div className="container">
        <h2>{news.title}</h2>
        <p><strong>Авторы:</strong> {news.authors.join(', ')}</p>
        <p><strong>Дата публикации:</strong> {news.publication_date}</p>
        <p><strong>Описание:</strong> {news.description}</p>
        <p><strong>Журнал:</strong> {news.magazine || "Не указан"}</p>
        <p><strong>Текст:</strong> {news.content}</p>
        {news.materials && (
          <p>
            <strong>Материалы:</strong>{" "}
            <a href={`/uploads/${news.materials}`} download>
              Скачать
            </a>
          </p>
        )}
      </div>
      <Footer />
    </section>
  );
};

export default NewsDetails;