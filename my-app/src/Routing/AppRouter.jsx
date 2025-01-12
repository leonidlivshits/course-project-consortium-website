import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import Home from "../pages/Home/Home";
import Events from "../pages/Events/Events";
import EventDetails from "../pages/Events/EventDetail";
import News from "../pages/News/News";
import Publications from "../pages/Publications/Publications";
import NoPage from "../pages/NoPage/NoPage";
import Projects from "../pages/Projects/Projects";
import OrganisationsPage from "../pages/Organisations/OrganisationsPage";

import { publicRoutes } from "./Routes";

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/events" element={<Events />} />
      <Route path="/events/:id" element={<EventDetails />} />
      <Route path="/organisations" element={<OrganisationsPage />} />
      <Route path="/news" element={<News />} />
      <Route path="/publications" element={<Publications />} />
      <Route path="/projects" element={<Projects />} />
      {/* {publicRoutes.map(({ path, Element }) => {
        return <Route key={path} path={path} element={Element} />;
      })} */}
      <Route path="/notFound" element={<NoPage />} />
      <Route path="*" element={<Navigate to="/notFound" />} />
    </Routes>
  );
};

export default AppRouter;
