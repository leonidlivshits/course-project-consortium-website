import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

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
