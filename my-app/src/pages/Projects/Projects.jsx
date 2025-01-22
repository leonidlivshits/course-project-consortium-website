// import React, { useEffect, useState } from "react";
// import "./Projects.css";
// import Navbar from "../../components/Navbar/Navbar";
// import Footer from "../../components/Footer/Footer";

// const Projects = () => {
//   const [projects, setProjects] = useState([]);

//   useEffect(() => {
//     fetch('http://127.0.0.1:5000/api/projects')
//       .then(response => response.json())
//       .then(data => setProjects(data))
//       .catch(error => console.error('Error fetching projects:', error));
//   }, []);

//   return (
//     <div className="page">
//       <Navbar />
//       <h1>Проекты</h1>
//       <div className="projects-list">
//         {projects.map((project) => (
//           <div key={project.id} className="project">
//             <h2>{project.title}</h2>
//             <p><strong>Авторы:</strong> {project.authors.join(', ')}</p>
//             <p><strong>Дата публикации:</strong> {project.publication_date}</p>
//             <p><strong>Описание:</strong> {project.description}</p>
//             <p><strong>Текст:</strong> {project.content}</p>
//             <p><strong>Материалы:</strong> {project.materials}</p>
//           </div>
//         ))}
//       </div>
//       <Footer />
//     </div>
//   );
// };

// export default Projects;
import React, { useEffect, useState } from "react";
import "./Projects.css";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const Projects = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/projects')
      .then((response) => response.json())
      .then((data) => setProjects(data))
      .catch((error) => console.error('Ошибка при загрузке проектов:', error));
  }, []);

  // Функция для определения типа файла
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
          <a href={fileUrl} download>
            Скачать PDF
          </a>
        );
      default:
        return (
          <a href={fileUrl} download>
            Скачать файл
          </a>
        );
    }
  };

  return (
    <div className="page">
      <Navbar />
      <h1>Проекты</h1>
      <div className="projects-list">
        {projects.map((project) => (
          <div key={project.id} className="project">
            <h2>{project.title}</h2>
            <p><strong>Авторы:</strong> {project.authors.join(', ')}</p>
            <p><strong>Дата публикации:</strong> {project.publication_date}</p>
            <p><strong>Описание:</strong> {project.description}</p>
            <p><strong>Текст:</strong> {project.content}</p>
            <p>
              <strong>Материалы:</strong>{" "}
              {project.materials ? renderFile(`http://127.0.0.1:5000${project.materials}`) : "Файл отсутствует"}
            </p>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default Projects;