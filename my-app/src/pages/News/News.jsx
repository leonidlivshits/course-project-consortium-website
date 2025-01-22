// import React, { useEffect, useState } from "react";
// import "./News.css";
// import Navbar from "../../components/Navbar/Navbar";
// import Footer from "../../components/Footer/Footer";

// const News = () => {
//   const [news, setNews] = useState([]);

//   useEffect(() => {
//     fetch('http://127.0.0.1:5000/api/news')
//       .then(response => response.json())
//       .then(data => setNews(data))
//       .catch(error => console.error('Error fetching news:', error));
//   }, []);

//   return (
//     <div className="page">
//       <Navbar />
//       <h1>Новости</h1>
//       <div className="s-list">
//         {news.map((newsItem) => (
//           <div key={newsItem.id} className="project">
//             <h2>{newsItem.title}</h2>
//             <p><strong>Авторы:</strong> {newsItem.authors.join(', ')}</p>
//             <p><strong>Дата публикации:</strong> {newsItem.publication_date}</p>
//             <p><strong>Описание:</strong> {newsItem.description}</p>
//             <p><strong>Журнал:</strong> {newsItem.magazine || "Не указан"}</p>
//             <p><strong>Текст:</strong> {newsItem.content}</p>
//             <p><strong>Материалы:</strong> {newsItem.materials}</p>
//           </div>
//         ))}
//       </div>
//       <Footer />
//     </div>
//   );
// };

// export default News;

import React, { useEffect, useState } from "react";
import "./News.css";
import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const News = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/news')
      .then((response) => response.json())
      .then((data) => setNews(data))
      .catch((error) => console.error('Ошибка при загрузке новостей:', error));
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
      <h1>Новости</h1>
      <div className="projects-list">
        {news.map((news) => (
          <div key={news.id} className="project">
            <h2>{news.title}</h2>
            <p><strong>Авторы:</strong> {news.authors.join(', ')}</p>
            <p><strong>Дата публикации:</strong> {news.publication_date}</p>
            <p><strong>Описание:</strong> {news.description}</p>
            <p><strong>Журнал:</strong> {news.magazine || "Не указан"}</p>
            <p><strong>Текст:</strong> {news.content}</p>
            <p>
              <strong>Материалы:</strong>{" "}
              {news.materials ? renderFile(`http://127.0.0.1:5000${news.materials}`) : "Файл отсутствует"}
            </p>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default News;