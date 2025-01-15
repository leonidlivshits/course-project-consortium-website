import React from "react";

import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const Home = () => {
  return (
    <div>
      <Navbar />
      <div className="page"> 
      <h1>Добро пожаловать на сайт</h1>
      </div>
      <Footer />
    </div>
  );
};

export default Home;