// const Projects = () => <div className="content"><h1>Проекты</h1></div>;
// export default Projects;

// import React from "react";

// import Navbar from "../../components/Navbar/Navbar";
// import Footer from "../../components/Footer/Footer";

// const Projects = () => {
//   return (
//     <div>
//       <Navbar />
//       <div className="page"> 
//       <h1>Проекты</h1>
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
      .then(response => response.json())
      .then(data => setProjects(data))
      .catch(error => console.error('Error fetching projects:', error));
  }, []);

  return (
    <div className="page">
      <Navbar />
      <h1>Проекты</h1>
      <div className="projects-list">
        {projects.map((project) => (
          <div key={project.id} className="project">
            <h2>{project.title}</h2>
            <p><strong>Авторы:</strong> {project.authors}</p>
            <p><strong>Дата публикации:</strong> {project.publication_date}</p>
            <p><strong>Описание:</strong> {project.description}</p>
            <p><strong>Текст:</strong> {project.content}</p>
            <p><strong>Материалы:</strong> {project.materials}</p>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default Projects;