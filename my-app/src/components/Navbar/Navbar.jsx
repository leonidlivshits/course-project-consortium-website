// import React, { useState } from "react";
// import "./Navbar.css";

// const Navbar = () => {
//   const [isSearchOpen, setIsSearchOpen] = useState(false);
//   const [searchQuery, setSearchQuery] = useState("");
//   const [searchResults, setSearchResults] = useState(null);
//   const [error, setError] = useState(null);

//   // Открытие/закрытие поиска
//   const toggleSearch = () => {
//     setIsSearchOpen(!isSearchOpen);
//     setSearchResults(null);
//     setSearchQuery("");
//     setError(null);
//   };

//   // Обработчик поиска при изменении ввода
//   const handleSearchChange = async (e) => {
//     setSearchQuery(e.target.value);

//     if (e.target.value.trim().length > 2) {
//       await performSearch(e.target.value);
//     } else {
//       setSearchResults(null);
//     }
//   };

//   // Обработчик поиска по нажатию Enter
//   const handleSearchKeyPress = async (e) => {
//     if (e.key === "Enter" && searchQuery.trim().length > 2) {
//       await performSearch(searchQuery);
//     }
//   };

//   // Функция поиска
//   const performSearch = async (query) => {
//     try {
//       const response = await fetch(`http://127.0.0.1:5000/api/search?q=${encodeURIComponent(query)}`);
      
//       if (!response.ok) {
//         throw new Error(`Ошибка сервера: ${response.status}`);
//       }

//       const data = await response.json();
//       setSearchResults(data);
//       setError(null);
//     } catch (err) {
//       console.error("Ошибка при поиске:", err);
//       setError("Ошибка загрузки результатов поиска");
//     }
//   };

//   return (
//     <>
//       {/* Поисковая строка */}
//       <div className={`search-bar ${isSearchOpen ? "active" : ""}`} style={{ top: isSearchOpen ? "0" : "-100px" }}>
//         <input
//           type="text"
//           placeholder="Поиск..."
//           value={searchQuery}
//           onChange={handleSearchChange}
//           onKeyDown={handleSearchKeyPress}
//         />
//         <button className="close-search" onClick={toggleSearch}>
//           <img src="/cross.png" alt="Закрыть" />
//         </button>
//       </div>

//       {/* Результаты поиска */}
//       {error && <p className="error-message">{error}</p>}
//       {searchResults && (
//         <div className="search-results">
//           {Object.keys(searchResults).map((category) =>
//             searchResults[category].length > 0 ? (
//               <div key={category}>
//                 <h4>{category.toUpperCase()}</h4>
//                 <ul>
//                   {searchResults[category].map((item) => (
//                     <li key={item.id}>
//                       <a href={item.link || "#"}>{item.title || item.link}</a>
//                     </li>
//                   ))}
//                 </ul>
//               </div>
//             ) : null
//           )}
//         </div>
//       )}

//       {/* Навигация */}
//       <nav className="navbar">
//         <div className="navbar-container">
//           <a href="/" className="navbar-logo">
//             <img src="/hse_logo.png" alt="HSE Logo" />
//           </a>
//           <ul className="nav-menu">
//             <li className="nav-item">
//               <a href="/" className="nav-link">Главная</a>
//             </li>
//             <li className="nav-item">
//               <a href="/organisations" className="nav-link">Организации</a>
//             </li>
//             <li className="nav-item">
//               <a href="/publications" className="nav-link">Публикации</a>
//             </li>
//             <li className="nav-item">
//               <a href="/news" className="nav-link">Новости</a>
//             </li>
//             <li className="nav-item">
//               <a href="/projects" className="nav-link">Проекты</a>
//             </li>
//             <li className="nav-item">
//               <a href="/events" className="nav-link">События</a>
//             </li>
//           </ul>
//           <div className="search-icon" onClick={toggleSearch}>
//             <img src="/loopa.png" alt="Поиск" />
//           </div>
//         </div>
//       </nav>
//     </>
//   );
// };

// export default Navbar;





// import React, { useState } from "react";
// import { useNavigate } from "react-router-dom"; // Импортируем useNavigate
// import "./Navbar.css";

// const Navbar = () => {
//   const [isSearchOpen, setIsSearchOpen] = useState(false);
//   const [searchQuery, setSearchQuery] = useState("");
//   const [searchResults, setSearchResults] = useState(null);
//   const [error, setError] = useState(null);
//   const navigate = useNavigate(); // Используем хук для навигации

//   // Открытие/закрытие поиска
//   const toggleSearch = () => {
//     console.log("Тоггл поиска. Сейчас:", isSearchOpen);
//     setIsSearchOpen(!isSearchOpen);
//     setSearchResults(null);
//     setSearchQuery("");
//     setError(null);
//   };

//   // Обработчик изменения ввода
//   const handleSearchChange = async (e) => {
//     setSearchQuery(e.target.value);
//     console.log("Изменение ввода, текущее значение:", e.target.value);

//     if (e.target.value.trim().length > 2) {
//       await performSearch(e.target.value);
//     } else {
//       setSearchResults(null);
//     }
//   };

//   // Обработчик нажатия Enter
//   const handleSearchKeyPress = async (e) => {
//     if (e.key === "Enter" && searchQuery.trim().length > 2) {
//       console.log("Enter нажат. Перенаправление на страницу поиска...");
//       navigate(`/search?query=${encodeURIComponent(searchQuery)}`);
//     }
//   };

//   // Функция поиска
//   const performSearch = async (query) => {
//     console.log("Запрос поиска отправлен:", query);
//     try {
//       const response = await fetch(`http://127.0.0.1:5000/api/search?q=${encodeURIComponent(query)}`);
      
//       if (!response.ok) {
//         throw new Error(`Ошибка сервера: ${response.status}`);
//       }

//       const data = await response.json();
//       console.log("Результаты поиска:", data);

//       setSearchResults(data);
//       setError(null);
//     } catch (err) {
//       console.error("Ошибка при поиске:", err);
//       setError("Ошибка загрузки результатов поиска");
//     }
//   };

//   return (
//     <>
//       {/* Поисковая строка */}
//       <div className={`search-bar ${isSearchOpen ? "active" : ""}`} style={{ top: isSearchOpen ? "0" : "-100px" }}>
//         <input
//           type="text"
//           placeholder="Поиск..."
//           value={searchQuery}
//           onChange={handleSearchChange}
//           onKeyDown={handleSearchKeyPress}
//         />
//         <button className="close-search" onClick={toggleSearch}>
//           <img src="/cross.png" alt="Закрыть" />
//         </button>
//       </div>

//       {/* Результаты поиска */}
//       {error && <p className="error-message">{error}</p>}
//       {searchResults && (
//         <div className="search-results">
//           {Object.keys(searchResults).map((category) =>
//             searchResults[category].length > 0 ? (
//               <div key={category}>
//                 <h4>{category.toUpperCase()}</h4>
//                 <ul>
//                   {searchResults[category].map((item) => (
//                     <li key={item.id}>
//                       <a href={item.link || "#"}>{item.title || item.link}</a>
//                     </li>
//                   ))}
//                 </ul>
//               </div>
//             ) : null
//           )}
//         </div>
//       )}
//       {/* Навигация */}
//       <nav className="navbar">
//         <div className="navbar-container">
//           <a href="/" className="navbar-logo">
//             <img src="/hse_logo.png" alt="HSE Logo" />
//           </a>
//           <ul className="nav-menu">
//             <li className="nav-item">
//               <a href="/" className="nav-link">Главная</a>
//             </li>
//             <li className="nav-item">
//               <a href="/organisations" className="nav-link">Организации</a>
//             </li>
//             <li className="nav-item">
//               <a href="/publications" className="nav-link">Публикации</a>
//             </li>
//             <li className="nav-item">
//               <a href="/news" className="nav-link">Новости</a>
//             </li>
//             <li className="nav-item">
//               <a href="/projects" className="nav-link">Проекты</a>
//             </li>
//             <li className="nav-item">
//               <a href="/events" className="nav-link">События</a>
//             </li>
//           </ul>
//           <div className="search-icon" onClick={toggleSearch}>
//             <img src="/loopa.png" alt="Поиск" />
//           </div>
//         </div>
//       </nav>
//     </>
//   );
// };

// export default Navbar;










// import React, { useState } from "react";
// import { useNavigate } from "react-router-dom";
// import "./Navbar.css";

// const Navbar = () => {
//   const [searchQuery, setSearchQuery] = useState("");
//   const [searchResults, setSearchResults] = useState(null);
//   const [error, setError] = useState(null);
//   const navigate = useNavigate();

//   // Обработчик изменения ввода
//   const handleSearchChange = async (e) => {
//     const query = e.target.value;
//     setSearchQuery(query);

//     if (query.trim().length > 2) {
//       await performSearch(query);
//     } else {
//       setSearchResults(null);
//     }
//   };

//   // Обработчик нажатия Enter -> переход на SearchResults.jsx
//   const handleSearchKeyPress = (e) => {
//     if (e.key === "Enter" && searchQuery.trim().length > 2) {
//       navigate(`/search?query=${encodeURIComponent(searchQuery)}`);
//     }
//   };

//   // Функция поиска (регистронезависимый)
//   const performSearch = async (query) => {
//     try {
//       const response = await fetch(
//         `http://127.0.0.1:5000/api/search?q=${encodeURIComponent(query.toLowerCase())}`
//       );

//       if (!response.ok) {
//         throw new Error(`Ошибка сервера: ${response.status}`);
//       }

//       const data = await response.json();
//       setSearchResults(data);
//       setError(null);
//     } catch (err) {
//       setError("Ошибка загрузки результатов поиска");
//     }
//   };

//   return (
//     <>
//       {/* Поисковая строка */}
//       <div className="search-bar">
//         <input
//           type="text"
//           placeholder="Поиск..."
//           value={searchQuery}
//           onChange={handleSearchChange}
//           onKeyDown={handleSearchKeyPress}
//         />
//       </div>

//       {/* Навигация */}
//       <nav className="navbar">
//         <div className="navbar-container">
//           <a href="/" className="navbar-logo">
//             <img src="/hse_logo.png" alt="HSE Logo" />
//           </a>
//           <ul className="nav-menu">
//             <li className="nav-item"><a href="/" className="nav-link">Главная</a></li>
//             <li className="nav-item"><a href="/organisations" className="nav-link">Организации</a></li>
//             <li className="nav-item"><a href="/publications" className="nav-link">Публикации</a></li>
//             <li className="nav-item"><a href="/news" className="nav-link">Новости</a></li>
//             <li className="nav-item"><a href="/projects" className="nav-link">Проекты</a></li>
//             <li className="nav-item"><a href="/events" className="nav-link">События</a></li>
//           </ul>
//         </div>
//       </nav>
//     </>
//   );
// };

// export default Navbar;







// import React, { useState } from "react";
// import { useNavigate } from "react-router-dom"; // Импортируем useNavigate
// import "./Navbar.css";

// const Navbar = () => {
//   const [isSearchOpen, setIsSearchOpen] = useState(false);
//   const [searchQuery, setSearchQuery] = useState("");
//   const navigate = useNavigate(); // Используем хук для навигации

//   // Открытие/закрытие поиска
//   const toggleSearch = () => {
//     console.log("Тоггл поиска. Сейчас:", isSearchOpen);
//     setIsSearchOpen(!isSearchOpen);
//     setSearchQuery("");
//   };

//   // Обработчик изменения ввода
//   const handleSearchChange = (e) => {
//     setSearchQuery(e.target.value);
//     console.log("Изменение ввода, текущее значение:", e.target.value);
//   };

//   // Обработчик нажатия Enter
//   const handleSearchKeyPress = (e) => {
//     if (e.key === "Enter" && searchQuery.trim().length > 2) {
//       console.log("Enter нажат. Перенаправление на страницу поиска...");
//       navigate(`/search?query=${encodeURIComponent(searchQuery)}`);
//     }
//   };

//   return (
//     <>
//       {/* Поисковая строка */}
//       <div className={`search-bar ${isSearchOpen ? "active" : ""}`} style={{ top: isSearchOpen ? "0" : "-100px" }}>
//         <input
//           type="text"
//           placeholder="Поиск..."
//           value={searchQuery}
//           onChange={handleSearchChange}
//           onKeyDown={handleSearchKeyPress}
//         />
//         <button className="close-search" onClick={toggleSearch}>
//           <img src="/cross.png" alt="Закрыть" />
//         </button>
//       </div>

//       {/* Навигация */}
//       <nav className="navbar">
//         <div className="navbar-container">
//           <a href="/" className="navbar-logo">
//             <img src="/hse_logo.png" alt="HSE Logo" />
//           </a>
//           <ul className="nav-menu">
//             <li className="nav-item">
//               <a href="/" className="nav-link">Главная</a>
//             </li>
//             <li className="nav-item">
//               <a href="/organisations" className="nav-link">Организации</a>
//             </li>
//             <li className="nav-item">
//               <a href="/publications" className="nav-link">Публикации</a>
//             </li>
//             <li className="nav-item">
//               <a href="/news" className="nav-link">Новости</a>
//             </li>
//             <li className="nav-item">
//               <a href="/projects" className="nav-link">Проекты</a>
//             </li>
//             <li className="nav-item">
//               <a href="/events" className="nav-link">События</a>
//             </li>
//           </ul>
//           <div className="search-icon" onClick={toggleSearch}>
//             <img src="/loopa.png" alt="Поиск" />
//           </div>
//         </div>
//       </nav>
//     </>
//   );
// };

// export default Navbar;





import React, { useState } from "react";
import { useNavigate } from "react-router-dom"; // Импортируем useNavigate
import "./Navbar.css";

const Navbar = () => {
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate(); // Используем хук для навигации

  // Открытие/закрытие поиска
  const toggleSearch = () => {
    console.log("Тоггл поиска. Сейчас:", isSearchOpen);
    setIsSearchOpen(!isSearchOpen);
    setSearchResults(null);
    setSearchQuery("");
    setError(null);
  };

  // Обработчик изменения ввода
  const handleSearchChange = async (e) => {
    const value = e.target.value.trim();
    setSearchQuery(value);
    console.log("Изменение ввода, текущее значение:", value);

    if (value.length > 2) {
      await performSearch(value);
    } else {
      setSearchResults(null);
    }
  };

  // Обработчик нажатия Enter
  const handleSearchKeyPress = async (e) => {
    if (e.key === "Enter" && searchQuery.trim().length > 2) {
      console.log("Enter нажат. Перенаправление на страницу поиска...");
      navigate(`/search?query=${encodeURIComponent(searchQuery)}`);
    }
  };

  // Функция поиска
  const performSearch = async (query) => {
    console.log(" Отправка запроса:", query);

    try {
      const response = await fetch(`http://127.0.0.1:5000/api/search?q=${encodeURIComponent(query)}`);
      
      console.log("Ответ от сервера (статус):", response.status);
      
      if (!response.ok) {
        throw new Error(`Ошибка сервера: ${response.status}`);
      }

      const data = await response.json();
      console.log("Данные с сервера:", data);

      setSearchResults(data);
      setError(null);
    } catch (err) {
      console.error("Ошибка при поиске:", err);
      setError("Ошибка загрузки результатов поиска");
    }
  };

  return (
    <>
      {/* Поисковая строка */}
      <div className={`search-bar ${isSearchOpen ? "active" : ""}`} style={{ top: isSearchOpen ? "0" : "-100px" }}>
        <input
          type="text"
          placeholder="Поиск..."
          value={searchQuery}
          onChange={handleSearchChange}
          onKeyDown={handleSearchKeyPress}
        />
        <button className="close-search" onClick={toggleSearch}>
          <img src="/cross.png" alt="Закрыть" />
        </button>
      </div>

      {/* Результаты поиска */}
      {error && <p className="error-message">{error}</p>}
      {searchResults && (
        <div className="search-results">
          {Object.keys(searchResults).map((category) =>
            searchResults[category].length > 0 ? (
              <div key={category}>
                <h4>{category.toUpperCase()}</h4>
                <ul>
                  {searchResults[category].map((item) => (
                    <li key={item.id}>
                      <a href={item.link || "#"}>{item.title || item.name}</a>
                    </li>
                  ))}
                </ul>
              </div>
            ) : null
          )}
        </div>
      )}
      {/* Навигация */}
      <nav className="navbar">
        <div className="navbar-container">
          <a href="/" className="navbar-logo">
            <img src="/hse_logo.png" alt="HSE Logo" />
          </a>
          <ul className="nav-menu">
            <li className="nav-item"><a href="/" className="nav-link">Главная</a></li>
            <li className="nav-item"><a href="/organisations" className="nav-link">Организации</a></li>
            <li className="nav-item"><a href="/publications" className="nav-link">Публикации</a></li>
            <li className="nav-item"><a href="/news" className="nav-link">Новости</a></li>
            <li className="nav-item"><a href="/projects" className="nav-link">Проекты</a></li>
            <li className="nav-item"><a href="/events" className="nav-link">События</a></li>
          </ul>
          <div className="search-icon" onClick={toggleSearch}>
            <img src="/loopa.png" alt="Поиск" />
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
