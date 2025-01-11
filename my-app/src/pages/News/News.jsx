// const News = () => <div className="content"><h1>Новости</h1></div>;
// export default News;

import React from "react";

import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const News = () => {
  return (
    <div>
      <Navbar />
      <div className="page"> 
      <h1>Новости</h1>
      </div>
      <Footer />
    </div>
  );
};

export default News;