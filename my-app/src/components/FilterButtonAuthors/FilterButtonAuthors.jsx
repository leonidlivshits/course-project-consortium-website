import React, {useContext, useState, useEffect } from 'react';
import './FilterButtonAuthors.css';
import { LanguageContext } from "../../components/LanguageContext/LanguageContext";


const AuthorFilter = ({ onApply }) => {
  const { language } = useContext(LanguageContext);
  const [isOpen, setIsOpen] = useState(false);
  const [selectedAuthors, setSelectedAuthors] = useState([]);
  const [authors, setAuthors] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/authors`)
      .then(res => res.json())
      .then(data => setAuthors(data))
      .catch(console.error);
  }, []);

  const toggleDropdown = () => setIsOpen(!isOpen);

  const handleCheckboxChange = (authorId) => {
    setSelectedAuthors(prev => prev.includes(authorId) ? prev.filter(id => id !== authorId) : [...prev, authorId]
    );
  };

  return (
    <div className="author-filter">
      <button className="filter-button" onClick={toggleDropdown}>{language === 'ru' ? 'Авторы' : 'Authors'}</button>
      
      {isOpen && (
        <div className="dropdown-content">
          {authors.map(author => (
            <label 
              key={author.id} 
              className="filter-item">
              <input
                type="checkbox"
                checked={selectedAuthors.includes(author.id)}
                onChange={() => handleCheckboxChange(author.id)}/>
              <span className="author-name">
                {author.last_name} {author.first_name} {author.middle_name}
              </span>
              <span className="count">{author.news_count}</span>
            </label>
          ))}
          
          <button 
            className="apply-button"
            onClick={() => {
              onApply(selectedAuthors);
              setIsOpen(false);
            }}>
            {language === 'ru' ? 'Применить' : 'Apply'}
          </button>
        </div>
      )}
    </div>
  );
};

export default AuthorFilter;