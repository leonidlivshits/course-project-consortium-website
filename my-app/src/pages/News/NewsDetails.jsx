import React, { useContext, useEffect, useState } from "react";
import { LanguageContext } from "../../components/LanguageContext/LanguageContext";
import { useParams } from 'react-router-dom';
import '../Events/EventDetail.css';
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const NewsDetails = () => {
  const { id } = useParams();
  const { language } = useContext(LanguageContext);
  const [news, setNews] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // fetch(`http://127.0.0.1:5000/api/news/${id}`)
    fetch(`${process.env.REACT_APP_API_URL}/news/${id}`)
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

    const formatAuthors = (authors) => {
      return authors.map(author => {
        const firstName = author[`first_name_${language}`] || author.first_name;
        const lastName = author[`last_name_${language}`] || author.last_name;
        return `${firstName} ${lastName}`;
      }).join(', ');
    };
  
    const getFileType = (fileName) => {
      const extension = fileName.split(".").pop().toLowerCase();
      if (["jpg", "jpeg", "png", "gif"].includes(extension)) {
        return "image";
      } else if (["mp3", "wav"].includes(extension)) {
        return "audio";
      } else if (extension === "pdf") {
        return "pdf";
      } else {
        return "unknown";
      }
    };
  
    const renderFile = (fileUrl) => {
      const fileType = getFileType(fileUrl);
  
      switch (fileType) {
        case "image":
          return <img src={fileUrl} alt="Материалы" style={{ maxWidth: "100%", height: "auto" }} />;
        case "audio":
          return (
            <audio controls>
              <source src={fileUrl} type={`audio/${fileUrl.split(".").pop()}`} />
              Ваш браузер не поддерживает аудио.
            </audio>
          );
        case "pdf":
          return (
            <Link to={fileUrl} download>
              Скачать PDF
            </Link>
          );
        default:
          return (
            <Link to={fileUrl} download>
              Скачать файл
            </Link>
          );
      }
    };
  

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
    <section className="event-detail">
      <Navbar />
      <div className="container">
      <h2>{news[`title_${language}`] || news.title}</h2>
      <p><strong>{language === 'ru' ? 'Авторы: ' : 'Authors: '}</strong> {formatAuthors(news.authors)}</p>
      <p><strong>{language === 'ru' ? 'Дата публикации: ' : 'Publication Date: '}</strong> 
        {new Date(news.publication_date).toLocaleDateString(language === 'ru' ? 'ru-RU' : 'en-US')}
      </p>
      <p><strong>{language === 'ru' ? 'Описание: ' : 'Abstract: '}</strong> 
        {news[`description_${language}`] || news.description}
      </p>
      <p>
      {news.magazine && (
        <p><strong>{language === 'ru' ? 'Журнал: ' : 'Journal: '}</strong> 
          {news.magazine[`name_${language}`] || news.magazine.name}
        </p>
      )}
      </p>
      <p><strong>{language === 'ru' ? 'Текст: ' : 'Text: '}</strong> 
        {news[`content_${language}`] || news.content}
      </p>
      <p>
        <strong>{language === 'ru' ? 'Материалы: ' : 'Materials: '}</strong>{" "}
        {news.materials ? renderFile(`${process.env.REACT_APP_API_URL}${encodeURIComponent(news.materials)}`) : language === 'ru' ? 'Файл отсутствует' : 'No file'}
      </p>
      </div>
      <Footer />
    </section>
  );
};

export default NewsDetails;