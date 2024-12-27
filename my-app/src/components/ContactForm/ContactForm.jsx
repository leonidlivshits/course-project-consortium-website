import React, { useState } from 'react';
import './ContactForm.css'

const ContactForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    company: '',
    message: '',
  });

  const [status, setStatus] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('sending');

    try {
      const response = await fetch('/api/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setStatus('success');
        setFormData({ name: '', email: '', phone: '', company: '', message: '' });
      } else {
        setStatus('error');
      }
    } catch (error) {
      setStatus('error');
    }
  };

  return (
    <section className="contact-form-section">
      <div className="container">
        <div className="row">
          <div className="col-lg-6 form-wrapper">
            <h2>Свяжитесь с нами</h2>
            <p>Мы всегда рады вашим вопросам и предложениям. Напишите нам, и мы ответим в кратчайшие сроки!</p>
            <form onSubmit={handleSubmit} className="contact-form">
              <input
                type="text"
                name="name"
                placeholder="Имя"
                value={formData.name}
                onChange={handleChange}
                required
              />
              <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                required
              />
              <input
                type="text"
                name="phone"
                placeholder="Телефон"
                value={formData.phone}
                onChange={handleChange}
                required
              />
              <input
                type="text"
                name="company"
                placeholder="Компания"
                value={formData.company}
                onChange={handleChange}
              />
              <textarea
                name="message"
                placeholder="Сообщение"
                value={formData.message}
                onChange={handleChange}
                required
              ></textarea>
              <button type="submit" className="btn-submit">Отправить</button>
            </form>
            {status === 'success' && <p className="success">Сообщение отправлено!</p>}
            {status === 'error' && <p className="error">Ошибка при отправке. Попробуйте позже.</p>}
          </div>
          <div className="col-lg-6">
            <h3>Наш адрес</h3>
            <p>Russian Federation</p>
            <p>info@cardiogenetics.ru</p>
            <p>+7 123 456 7890</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactForm;
