// const Projects = () => <div className="content"><h1>Проекты</h1></div>;
// export default Projects;

import React from "react";

import Navbar from "../../components/Navbar/Navbar";
import Footer from "../../components/Footer/Footer";

const Projects = () => {
  return (
    <div>
      <Navbar />
      <div className="page"> 
      <h1>Проекты</h1>
      </div>
      <Footer />
    </div>
  );
};

export default Projects;