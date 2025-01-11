// Footer.jsx
import React from 'react';
import './Footer.css';

const Footer = () => {
    return (
        <footer className="footer">
            <div className="footer-container">
                <div className="footer-section">
                    <h2>Кардиогенетика</h2>
                    <p>Ваш надежный источник информации о кардиогенетике. Мы здесь, чтобы помочь вам разобраться в сложных вопросах!</p>
                    {/* <a href="#" className="btn-primary">Узнать больше</a> */}
                </div>
                <div className="footer-section">
                    <ul>
                        <li>Публикации</li>
                        <li>Новости</li>
                        <li>События</li>
                        <li>Организации</li>
                        <li>Контакты</li>
                    </ul>
                </div>
                <div className="footer-section">
                    <ul>
                        <li>Поиск</li>
                        <li>Проекты</li>
                        <li>Фильтрация</li>
                        <li>Поддержка</li>
                        <li>О нас</li>
                    </ul>
                </div>
            </div>
            {/* <div className="footer-socials">
                <p>Следите за нами в соцсетях</p>
                <div>
                    <a href="#"><i className="socicon-facebook"></i></a>
                    <a href="#"><i className="socicon-instagram"></i></a>
                    <a href="#"><i className="socicon-tiktok"></i></a>
                    <a href="#"><i className="socicon-linkedin"></i></a>
                </div>
            </div> */}
            <div className="footer-bottom">
                <p>© 2024 Кардиогенетика. Все права защищены.</p>
            </div>
        </footer>
    );
};

export default Footer;
