

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
//         {news.map((news) => (
//           <div key={news.id} className="project">
//             <h2>{news.title}</h2>
//             <p><strong>Авторы:</strong> {news.authors}</p>
//             <p><strong>Дата публикации:</strong> {news.publication_date}</p>
//             <p><strong>Описание:</strong> {news.description}</p>
//             <p><strong>Журнал:</strong> {news.magazine}</p>
//             <p><strong>Текст:</strong> {news.content}</p>
//             <p><strong>Материалы:</strong> {news.materials}</p>
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
      .then(response => response.json())
      .then(data => setNews(data))
      .catch(error => console.error('Error fetching news:', error));
  }, []);

  return (
    <div className="page">
      <Navbar />
      <h1>Новости</h1>
      <div className="s-list">
        {news.map((newsItem) => (
          <div key={newsItem.id} className="project">
            <h2>{newsItem.title}</h2>
            <p><strong>Авторы:</strong> {newsItem.authors.join(', ')}</p>
            <p><strong>Дата публикации:</strong> {newsItem.publication_date}</p>
            <p><strong>Описание:</strong> {newsItem.description}</p>
            <p><strong>Журнал:</strong> {newsItem.magazine || "Не указан"}</p>
            <p><strong>Текст:</strong> {newsItem.content}</p>
            <p><strong>Материалы:</strong> {newsItem.materials}</p>
          </div>
        ))}
      </div>
      <Footer />
    </div>
  );
};

export default News;