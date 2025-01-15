--
-- PostgreSQL database dump
--

-- Dumped from database version 13.18 (Debian 13.18-1.pgdg120+1)
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
-- SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: cardio_user
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO cardio_user;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: contact; Type: TABLE; Schema: public; Owner: cardio_user
--

CREATE TABLE public.contact (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    email character varying(120) NOT NULL,
    phone character varying(20) NOT NULL,
    company character varying(100),
    message text NOT NULL
);


ALTER TABLE public.contact OWNER TO cardio_user;

--
-- Name: contact_id_seq; Type: SEQUENCE; Schema: public; Owner: cardio_user
--

CREATE SEQUENCE public.contact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contact_id_seq OWNER TO cardio_user;

--
-- Name: contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cardio_user
--

ALTER SEQUENCE public.contact_id_seq OWNED BY public.contact.id;


--
-- Name: event; Type: TABLE; Schema: public; Owner: cardio_user
--

CREATE TABLE public.event (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    date character varying(50) NOT NULL,
    "time" character varying(50) NOT NULL,
    location character varying(100) NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.event OWNER TO cardio_user;

--
-- Name: event_id_seq; Type: SEQUENCE; Schema: public; Owner: cardio_user
--

CREATE SEQUENCE public.event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.event_id_seq OWNER TO cardio_user;

--
-- Name: event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cardio_user
--

ALTER SEQUENCE public.event_id_seq OWNED BY public.event.id;


--
-- Name: project; Type: TABLE; Schema: public; Owner: cardio_user
--

CREATE TABLE public.project (
    id integer NOT NULL,
    title character varying(100) NOT NULL,
    authors character varying(200) NOT NULL,
    publication_date character varying(50) NOT NULL,
    description text NOT NULL,
    content text NOT NULL,
    materials text
);


ALTER TABLE public.project OWNER TO cardio_user;

--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: cardio_user
--

CREATE SEQUENCE public.project_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.project_id_seq OWNER TO cardio_user;

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cardio_user
--

ALTER SEQUENCE public.project_id_seq OWNED BY public.project.id;


--
-- Name: contact id; Type: DEFAULT; Schema: public; Owner: cardio_user
--

ALTER TABLE ONLY public.contact ALTER COLUMN id SET DEFAULT nextval('public.contact_id_seq'::regclass);


--
-- Name: event id; Type: DEFAULT; Schema: public; Owner: cardio_user
--

ALTER TABLE ONLY public.event ALTER COLUMN id SET DEFAULT nextval('public.event_id_seq'::regclass);


--
-- Name: project id; Type: DEFAULT; Schema: public; Owner: cardio_user
--

ALTER TABLE ONLY public.project ALTER COLUMN id SET DEFAULT nextval('public.project_id_seq'::regclass);


--
-- Data for Name: contact; Type: TABLE DATA; Schema: public; Owner: cardio_user
--

COPY public.contact (id, name, email, phone, company, message) FROM stdin;
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: cardio_user
--

COPY public.event (id, title, date, "time", location, description) FROM stdin;
4	Конференция	15 января 2025	15:00	Москва, Россия	Присоединяйтесь к нашей ежегодной конференции по кардиогенетике!
5	Семинар	22 февраля 2025	15:00	Санкт-Петербург, Россия	Узнайте о последних методах в кардиогенетике на нашем семинаре.
6	Вебинар	10 марта 2025	15:00	Онлайн	Не пропустите наш вебинар о генетических тестах!
\.


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: cardio_user
--

COPY public.project (id, title, authors, publication_date, description, content, materials) FROM stdin;
3	Проект 1	Иванов И.И., Петров П.П.	2024-01-01	Описание проекта 1	Основной текст проекта 1	https://example.com/materials1
4	Проект 2	Сидоров С.С.	2023-06-01	Описание проекта 2	Основной текст проекта 2	https://example.com/materials2
\.


--
-- Name: contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cardio_user
--

SELECT pg_catalog.setval('public.contact_id_seq', 1, false);


--
-- Name: event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cardio_user
--

SELECT pg_catalog.setval('public.event_id_seq', 6, true);


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cardio_user
--

SELECT pg_catalog.setval('public.project_id_seq', 4, true);


--
-- Name: contact contact_pkey; Type: CONSTRAINT; Schema: public; Owner: cardio_user
--

ALTER TABLE ONLY public.contact
    ADD CONSTRAINT contact_pkey PRIMARY KEY (id);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: cardio_user
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (id);


--
-- Name: project project_pkey; Type: CONSTRAINT; Schema: public; Owner: cardio_user
--

ALTER TABLE ONLY public.project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: cardio_user
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

