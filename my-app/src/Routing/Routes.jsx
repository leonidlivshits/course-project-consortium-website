import About from "../pages/Organisations/OrganisationsPage.jsx";
import Publications from "../pages/Publications/Publications.jsx";
import News from "../pages/News/News.jsx";
import Home from "../pages/Home/Home.jsx"
import Events from "../pages/Events/Events.jsx";
import NoPage from "../pages/NoPage/NoPage.jsx";
import EventDetail from "../pages/Events/EventDetail.jsx";

import {
    MAIN_ROUTE,
    ORGANISATIONS_ROUTE,
    PUBLICATIONS_ROUTE,
    NEWS_ROUTE,
    NO_PAGE_ROUTE,
    PROJECTS_ROUTE,
    EVENTS_ROUTE,
    EVENT_DETAIL_ROUTE
} from "./const.js";

export const publicRoutes = [
  {
    path: MAIN_ROUTE,
    Element: <Home />,
  },
  {
    path: ORGANISATIONS_ROUTE,
    Element: <About />,
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
    path: EVENT_DETAIL_ROUTE, // Новый маршрут для деталей событий
    Element: <EventDetail />,
  },
];
