import React, {useContext, useState } from "react";
import './SortButton.css'; 
import '../../components/FilterButtonAuthors/FilterButtonAuthors.css';
import { LanguageContext } from "../../components/LanguageContext/LanguageContext";


const SortButton = ({ onSort }) => {
  const { language } = useContext(LanguageContext);
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  const handleSort = (sortType) => {
    onSort(sortType);
    setIsOpen(false);
  };

  return (
    <div className="dropdown">
      <button className="dropbtn" onClick={toggleDropdown}>
        {language === 'ru' ? 'Отсортировать' : 'Sort'}
      </button>
      {isOpen && (
        <div className="dropdown-content">
          <button  className="apply-button" onClick={() => handleSort('alphabetical')}>{language === 'ru' ? 'По алфавиту (А - Я)' : 'Alphabetical (A - Z)'}</button>
          <button  className="apply-button" onClick={() => handleSort('reverse_alphabetical')}>{language === 'ru' ? 'По алфавиту (Я - А)' : 'Alphabetical (Z - A)'}</button>
          <button  className="apply-button" onClick={() => handleSort('date_asc')}>{language === 'ru' ? 'По дате (стар - нов)' : 'Date (old - new)'}</button>
          <button  className="apply-button" onClick={() => handleSort('date_desc')}>{language === 'ru' ? 'По дате (нов - стар)' : 'Date (new - old)'}</button>
        </div>
      )}
    </div>
  );
};

export default SortButton;