BEGIN;


CREATE TABLE IF NOT EXISTS public.carreras
(
    cod_carrera serial NOT NULL,
    nombre_carrera character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT carreras_pkey PRIMARY KEY (cod_carrera)
);

CREATE TABLE IF NOT EXISTS public.carreras_personas
(
    id_carr_pers serial NOT NULL,
    id_persona integer NOT NULL,
    cod_carrera integer NOT NULL,
    CONSTRAINT carreras_personas_pkey PRIMARY KEY (id_carr_pers)
);

CREATE TABLE IF NOT EXISTS public.materias
(
    cod_materia serial NOT NULL,
    nombre_materia character varying(50) COLLATE pg_catalog."default" NOT NULL,
    cod_carrera integer NOT NULL,
    CONSTRAINT materias_pkey PRIMARY KEY (cod_materia)
);

CREATE TABLE IF NOT EXISTS public.personas
(
    id_persona serial NOT NULL,
    nombre_persona character varying(50) COLLATE pg_catalog."default" NOT NULL,
    apellido_persona character varying(50) COLLATE pg_catalog."default" NOT NULL,
    email_persona character varying(50) COLLATE pg_catalog."default" NOT NULL,
    active boolean,
    CONSTRAINT personas_pkey PRIMARY KEY (id_persona)
);

ALTER TABLE IF EXISTS public.carreras_personas
    ADD CONSTRAINT fk_carreras_personas_carreras FOREIGN KEY (cod_carrera)
    REFERENCES public.carreras (cod_carrera) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.carreras_personas
    ADD CONSTRAINT fk_carreras_personas_personas FOREIGN KEY (id_persona)
    REFERENCES public.personas (id_persona) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.materias
    ADD CONSTRAINT fk_materias_carreras FOREIGN KEY (cod_carrera)
    REFERENCES public.carreras (cod_carrera) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


INSERT INTO public.carreras (nombre_carrera) VALUES 
('Ingeniería en Sistemas'),
('Arquitectura'),
('Programación');

INSERT INTO public.materias (nombre_materia, cod_carrera) VALUES 
('DSI', 1),
('Análisis Matemático 2', 1),
('Estructuras I', 2),
('Estructuras II', 2),
('Estructuras III', 2),
('Bases de Datos 1', 3),
('Laboratorio de Computación 1', 3),
('Matemática', 3),
('Legislación', 3);


END;