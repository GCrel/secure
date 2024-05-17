DROP USER seguridad CASCADE;

CREATE USER seguridad IDENTIFIED BY "StrongPassword123#" account UNLOCK ; 

GRANT UNLIMITED TABLESPACE TO seguridad;

GRANT CREATE DATABASE LINK,
	CREATE SEQUENCE,
    CREATE SESSION,
    CREATE TABLE
TO seguridad;



create table seguridad.ESTABLISHMENT(
	EST_ID NUMBER (10) NOT NULL ,
	EST_NAME VARCHAR2(90)not null,
	EST_ADDRESS VARCHAR2(90)not null,
	EST_PHONE_NUMBER VARCHAR2(30)not null,
	EST_LOCALITY VARCHAR2(30)not null,
	POLICE_CENTER_ID NUMBER(10)
);

alter table seguridad.ESTABLISHMENT add constraint "EST_PK" primary key(EST_ID);
alter table seguridad.ESTABLISHMENT add constraint "EST_FK" foreign key (POLICE_CENTER_ID) references seguridad.ESTABLISHMENT(EST_ID);


create table seguridad.EMERGENCY_CALLS (
	EMC_ID NUMBER(10)not null,
   	EMC_PHONE_NUMBER varchar2(20)not null,
	EMC_DATE  DATE not null,
	EMC_ADDRESS VARCHAR2(90) not null,
	EMC_DETAILS VARCHAR2(150)not null,
	INC_ID NUMBER(10) not null
);

alter table seguridad.EMERGENCY_CALLS add constraint "EMC_PK" primary key(EMC_ID);


create table seguridad.INCIDENTS (
	INC_ID NUMBER(10) not null,
	INC_INCIDENT_TYPE VARCHAR2(90) not NULL,
	INC_DETAILS VARCHAR2(100) not null
);

alter table seguridad.INCIDENTS add constraint "INC_PK" primary key (INC_ID);

alter table seguridad.EMERGENCY_CALLS add constraint "EMC_FK" foreign key(INC_ID) references seguridad.INCIDENTS(INC_ID);

create table seguridad.EMERG_ESTABLIS (
	EMC_ID NUMBER(10)not null,
	EST_ID NUMBER(10) not null
);

alter table seguridad.EMERG_ESTABLIS add constraint "EET_PK" primary key (EMC_ID,EST_ID);

alter table seguridad.EMERG_ESTABLIS add constraint "EET_EMC_FK" foreign key(EMC_ID) references seguridad.EMERGENCY_CALLS (EMC_ID);

alter table seguridad.EMERG_ESTABLIS add constraint "EET_EST_FK" foreign key(EST_ID) references seguridad.ESTABLISHMENT (EST_ID);

create table seguridad.EMERGEN_REPORT (
	 EMC_ID NUMBER(10) not null,
	REP_ID NUMBER(10) not null
);

create table seguridad.REPORTERS (
	REP_ID number(10) not null,
	REP_FIRST_NAME VARCHAR2(30)not null,
	REP_LAST_NAME VARCHAR2(30)not null ,
	REP_DNI VARCHAR2(20)not null,
	REP_GENDER VARCHAR2(20)not null,
	REP_AGE NUMBER(10)not null
);

alter table seguridad.REPORTERS add constraint "REP_PK" PRIMARY KEY(REP_ID);

alter table seguridad.EMERGEN_REPORT add constraint "EMR_PK" PRIMARY KEY (EMC_ID,REP_ID);

alter table seguridad.EMERGEN_REPORT add constraint "EMR_EMC_FK" FOREIGN KEY(EMC_ID) references seguridad.EMERGENCY_CALLS(EMC_ID);

alter table seguridad.EMERGEN_REPORT add constraint "EMR_REP_FK" FOREIGN KEY (REP_ID) references seguridad.REPORTERS(REP_ID);

commit;



INSERT INTO seguridad.ESTABLISHMENT (EST_ID,EST_NAME, EST_ADDRESS, EST_PHONE_NUMBER, EST_LOCALITY,POLICE_CENTER_ID)VALUES
(1,'Policía Unidad Regional II Chilecito', 'Av. Pelagio B. Luna 642','03825422404','Chilecito',NULL);

INSERT INTO seguridad.ESTABLISHMENT (EST_ID,EST_NAME, EST_ADDRESS, EST_PHONE_NUMBER, EST_LOCALITY,POLICE_CENTER_ID) VALUES
(2,'Destacamento Policial La Puntilla', 'Av. Primera Junta, La Puntilla', '03825412684', 'Chilecito',1);

INSERT INTO seguridad.ESTABLISHMENT (EST_ID,EST_NAME, EST_ADDRESS, EST_PHONE_NUMBER, EST_LOCALITY,POLICE_CENTER_ID) VALUES
(3,'Policía Accidentes Viales', 'Av. Circunvalación', '03825871249','Chilecito',1);

INSERT INTO seguridad.ESTABLISHMENT (EST_ID,EST_NAME, EST_ADDRESS, EST_PHONE_NUMBER, EST_LOCALITY,POLICE_CENTER_ID) VALUES
(4,'Comisaría del Menor y la Mujer', 'Av. Pres. Illia,Hipolito Irigoyen', '03825429692', 'Chilecito',1);

INSERT INTO seguridad.ESTABLISHMENT (EST_ID,EST_NAME, EST_ADDRESS, EST_PHONE_NUMBER, EST_LOCALITY,POLICE_CENTER_ID) VALUES
(5,'Puesto Policial Chilecito', 'RN40', '03825452010', 'Chilecito',1);

-------------------------
--–AGREGADO INCIDENTES
--—-----------------------

INSERT INTO seguridad.INCIDENTS (INC_ID,INC_INCIDENT_TYPE, INC_DETAILS ) VALUES
(1,'Delitos','Incidentes con motivación delictiva que afectan a las personas'); 

INSERT INTO seguridad.INCIDENTS (INC_ID,INC_INCIDENT_TYPE, INC_DETAILS ) VALUES
(2,'Violencia','Golpes en el cuerpo');

INSERT INTO seguridad.INCIDENTS (INC_ID,INC_INCIDENT_TYPE, INC_DETAILS ) VALUES
(3,'Accidente de seguridad vial','Cualquier accidente de seguridad vial ');

INSERT INTO seguridad.INCIDENTS (INC_ID,INC_INCIDENT_TYPE, INC_DETAILS ) VALUES
(4,'Disturbios','disturbios civiles o políticos y/o comportamientos tumultuosos');

INSERT INTO seguridad.INCIDENTS (INC_ID,INC_INCIDENT_TYPE, INC_DETAILS ) VALUES
(5,'Arma utilizada o avistada','Avistamiento de arma utilizada o en posesión de una persona');

--—---------------------------
--–AGREGADO EMERGENCY_CALLS 
--—---------------------------

INSERT INTO seguridad.EMERGENCY_CALLS (EMC_ID,EMC_PHONE_NUMBER, EMC_DATE , EMC_ADDRESS ,EMC_DETAILS ,INC_ID) VALUES 
(1,'3822340958', TO_DATE('2024-05-04 12:30:45', 'YYYY-MM-DD HH24:MI:SS'),'Catamarca 60','Robo',1); 

INSERT INTO seguridad.EMERGENCY_CALLS (EMC_ID,EMC_PHONE_NUMBER, EMC_DATE , EMC_ADDRESS ,EMC_DETAILS ,INC_ID) VALUES 
(2,'3825123940', TO_DATE('2024-05-01 16:50:15', 'YYYY-MM-DD HH24:MI:SS'),'San Martín 10, F5360','Disturbios',4); 

INSERT INTO seguridad.EMERGENCY_CALLS (EMC_ID,EMC_PHONE_NUMBER, EMC_DATE , EMC_ADDRESS ,EMC_DETAILS ,INC_ID) VALUES 
(3,'3825783921', TO_DATE('2024-03-23 07:32:30', 'YYYY-MM-DD HH24:MI:SS'), 'RP14','Accidente', 3);

INSERT INTO seguridad.EMERGENCY_CALLS (EMC_ID,EMC_PHONE_NUMBER, EMC_DATE , EMC_ADDRESS ,EMC_DETAILS ,INC_ID) VALUES 
(4,'3825346129', TO_DATE('2023-12-10 02:14:47', 'YYYY-MM-DD HH24:MI:SS'),'Sta. Rosa, San Miguel','Accidente',3);

INSERT INTO seguridad.EMERGENCY_CALLS (EMC_ID,EMC_PHONE_NUMBER, EMC_DATE , EMC_ADDRESS ,EMC_DETAILS ,INC_ID) VALUES 
(5,'3825382792', TO_DATE('2024-03-24 20:28:58', 'YYYY-MM-DD HH24:MI:SS'),'San Francisco 320','Violencia',2);

--------------------------------
--AGREGADO EMERG_ESTABLIS
--------------------------------

INSERT INTO seguridad.EMERG_ESTABLIS (EMC_ID, EST_ID) VALUES
(1,4);

INSERT INTO seguridad.EMERG_ESTABLIS (EMC_ID, EST_ID) VALUES
(2,1);

INSERT INTO seguridad.EMERG_ESTABLIS (EMC_ID, EST_ID) VALUES
(3,3);

INSERT INTO seguridad.EMERG_ESTABLIS (EMC_ID, EST_ID) VALUES
(4,2);

INSERT INTO seguridad.EMERG_ESTABLIS (EMC_ID, EST_ID) VALUES
(5,1);

-------------------------
--AGREGADO REPORTERS
-------------------------

INSERT INTO seguridad.REPORTERS (REP_ID,REP_FIRST_NAME, REP_LAST_NAME, REP_DNI, REP_GENDER, REP_AGE) VALUES 
(1,'Lucía', 'Fernández', '35444223', 'Femenino', 28);

INSERT INTO seguridad.REPORTERS (REP_ID,REP_FIRST_NAME, REP_LAST_NAME, REP_DNI, REP_GENDER, REP_AGE) VALUES 
(2,'Sofía', 'Martínez', '30234567','Femenino', 32);

INSERT INTO seguridad.REPORTERS (REP_ID,REP_FIRST_NAME, REP_LAST_NAME, REP_DNI, REP_GENDER, REP_AGE) VALUES 
(3,'Alejandro', 'González', '25123456', 'Masculino', 45);

INSERT INTO seguridad.REPORTERS (REP_ID,REP_FIRST_NAME, REP_LAST_NAME, REP_DNI, REP_GENDER, REP_AGE) VALUES 
(4,'María', 'López', '40123456', 'Femenino', 40);

INSERT INTO seguridad.REPORTERS (REP_ID,REP_FIRST_NAME, REP_LAST_NAME, REP_DNI, REP_GENDER, REP_AGE) VALUES 
(5,'Juan', 'Rodríguez', '30123456', 'Masculino', 35);

-----------------------
--AGREGADO EMERGEN_REPORT
-------------------------

INSERT INTO seguridad.EMERGEN_REPORT (EMC_ID,REP_ID) VALUES (1,1);
INSERT INTO seguridad.EMERGEN_REPORT (EMC_ID,REP_ID) VALUES (2,2);
INSERT INTO seguridad.EMERGEN_REPORT (EMC_ID,REP_ID) VALUES (3,3);
INSERT INTO seguridad.EMERGEN_REPORT (EMC_ID,REP_ID) VALUES (4,4);
INSERT INTO seguridad.EMERGEN_REPORT (EMC_ID,REP_ID) VALUES (5,5);

commit;



