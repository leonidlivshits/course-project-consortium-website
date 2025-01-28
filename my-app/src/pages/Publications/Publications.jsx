import React, { useEffect, useState } from "react";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const Publications = () => {
  const [publications, setPublications] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/publications')
      .then(response => response.json())
      .then(data => setPublications(data))
      .catch(error => console.error('Error fetching publications:', error));
  }, []);

  return (
    <div className="page">
      <Navbar />
      <h1>Публикации</h1>
      <div className="s-list">
        {publications.map((publication) => (
          <div key={publication.id} className="project">
            <h2>{publication.title}</h2>
            <p><strong>Авторы:</strong> {publication.authors.join(', ')}</p>
            <p><strong>Дата публикации:</strong> {publication.publication_date}</p>
            <p><strong>Журнал:</strong> {publication.magazine || "Не указан"}</p>
            <p><strong>Описание:</strong> {publication.annotation}</p>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default Publications;