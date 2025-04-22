import React, { useContext, useEffect, useState } from "react";
import "./Projects.css";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";
import { Link } from "react-router-dom";
import { LanguageContext } from "../../components/LanguageContext/LanguageContext";

const Projects = () => {
  const { language } = useContext(LanguageContext);
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    // fetch('http://127.0.0.1:5000/api/projects')
    fetch(`${process.env.REACT_APP_API_URL}/projects`)
      .then((response) => response.json())
      .then((data) => setProjects(data))
      .catch((error) => console.error('Ошибка при загрузке проектов:', error));
  }, []);

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
           {language === 'ru' ? 'Скачать файл' : 'Download file'}
          </Link>
        );
    }
  };

  return (
    <div className="page">
      <Navbar />
      <h1>{language === 'ru' ? 'Проекты' : 'Projects'}</h1>
      <div className="projects-list">
        {projects.map((project) => (
          <div key={project.id} className="project">
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
            <Link 
              to={`/projects/${project.id}`} 
              state={project} 
              className="project-link"
            >
              {language === 'ru' ? 'Подробнее' : 'Read more'}
            </Link>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default Projects;