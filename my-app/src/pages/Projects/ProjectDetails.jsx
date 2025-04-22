import React, { useContext, useEffect, useState } from "react";
import { LanguageContext } from "../../components/LanguageContext/LanguageContext";
import { useParams } from 'react-router-dom';
import '../Events/EventDetail.css';
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";

const ProjectDetails = () => {
  const { id } = useParams(); // Извлекаем id из URL
  const { language } = useContext(LanguageContext);
  const [project, setProject] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/projects/${id}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Проект не найден');
        }
        return response.json();
      })
      .then(data => {
        setProject(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Ошибка при загрузке проекта:', error);
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

  if (!project) {
    return <div>Проект не найден</div>;
  }

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
  
    const formatAuthors = (authors) => {
      return authors.map(author => {
        const firstName = author[`first_name_${language}`] || author.first_name;
        const lastName = author[`last_name_${language}`] || author.last_name;
        return `${firstName} ${lastName}`;
      }).join(', ');
    };
  
    // Функция для отображения файла в зависимости от его типа
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
  

  return (
    <section className="event-detail">
      <Navbar />
      <div className="container">
      <h2>{project[`title_${language}`] || project.title}</h2>
      <p><strong>{language === 'ru' ? 'Авторы: ' : 'Authors: '}</strong> {formatAuthors(project.authors)}</p>
      <p><strong>{language === 'ru' ? 'Дата публикации: ' : 'Publication Date: '}</strong> 
        {new Date(project.publication_date).toLocaleDateString(language === 'ru' ? 'ru-RU' : 'en-US')}
      </p>
      <p><strong>{language === 'ru' ? 'Описание: ' : 'Abstract: '}</strong> 
        {project[`description_${language}`] || project.description}
      </p>
      <p><strong>{language === 'ru' ? 'Текст: ' : 'Text: '}</strong> 
        {project[`content_${language}`] || project.content}
      </p>
      <p>
        <strong>{language === 'ru' ? 'Материалы: ' : 'Materials: '}</strong>{" "}
          {project.materials ? renderFile(`${process.env.REACT_APP_API_URL}/${project.materials}`) : "Файл отсутствует"}
      </p>
      </div>
      <Footer />
    </section>
  );
};

export default ProjectDetails;