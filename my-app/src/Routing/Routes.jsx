import Organisations from "../pages/Organisations/Organisations.jsx";
import Publications from "../pages/Publications/Publications.jsx";
import News from "../pages/News/News.jsx";
import Home from "../pages/Home/Home.jsx"
import Events from "../pages/Events/Events.jsx";
import NoPage from "../pages/NoPage/NoPage.jsx";
import EventDetail from "../pages/Events/EventDetail.jsx";
import Projects from "../pages/Projects/Projects.jsx";
import SearchResults from "../pages/SearchResult/SearchResult";
import NewsDetails from "../pages/News/NewsDetails";
import ProjectDetails from "../pages/Projects/ProjectDetails.jsx";
import PublicationDetails from "../pages/Publications/PublicationDetails.jsx";

import {
    MAIN_ROUTE,
    ORGANISATIONS_ROUTE,
    PUBLICATIONS_ROUTE,
    NEWS_ROUTE,
    NO_PAGE_ROUTE,
    PROJECTS_ROUTE,
    EVENTS_ROUTE,
    EVENT_DETAIL_ROUTE,
    SEARCH_RESULSTS_ROUTE,
    NEWS_DETAIL_ROUTE,
    PUBLICATION_DETAIL_ROUTE,
    PROJECT_DETAIL_ROUTE
} from "./const.js";
import NewsDetails from "../pages/News/NewsDetails.jsx";

export const publicRoutes = [
  {
    path: MAIN_ROUTE,
    Element: <Home />,
  },
  {
    path: ORGANISATIONS_ROUTE,
    Element: <Organisations />,
  },
  {
    path: PUBLICATIONS_ROUTE,
    Element: <Publications />,
  },
  {
    path: NEWS_ROUTE,
    Element: <News />,
  },
  {
    path: NO_PAGE_ROUTE,
    Element: <NoPage />,
  },
  {
    path: EVENTS_ROUTE,
    Element: <Events />,
  },
  {
    path: PROJECTS_ROUTE,
    Element: <Projects />,
  },
  {
    path: EVENT_DETAIL_ROUTE, // Новый маршрут для деталей событий
    Element: <EventDetail />,
  },
  {
    path: SEARCH_RESULSTS_ROUTE,
    Element: <SearchResults />,
  },
  {
    path: NEWS_DETAIL_ROUTE,
    Element: <NewsDetails />
  },
  {
    path: PUBLICATION_DETAIL_ROUTE,
    Element: <PublicationDetails />
  },
  {
    path: PROJECT_DETAIL_ROUTE,
    Element: <ProjectDetails />
  }
];
