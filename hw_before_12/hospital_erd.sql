CREATE TABLE "appointment"(
    "appointment-id" SERIAL NOT NULL PRIMARY KEY,
    "appointment-date" DATE NOT NULL,
    "appointment-time" TIME(0) WITHOUT TIME ZONE NOT NULL,
    "doctor-id" INTEGER NOT NULL,
    "patient-id" INTEGER NOT NULL,
    "appointment-description" TEXT NULL,
    "next-visit" DATE NULL
);

CREATE TABLE "bed"(
    "bed-id" SERIAL NOT NULL PRIMARY KEY,
    "bed-name" VARCHAR(120) NOT NULL,
    "bed-type" VARCHAR(120) NULL,
    "room-id" INTEGER NOT NULL
);

CREATE TABLE "person"(
    "person-id" SERIAL NOT NULL PRIMARY KEY,
    "person-firstname" VARCHAR(120) NOT NULL,
    "person-lastname" VARCHAR(120) NOT NULL,
    "person-address" VARCHAR(255) NOT NULL,
    "person-insured-code" INTEGER NULL,
    "person-national-code" CHAR(10) NOT NULL UNIQUE,
    "gender" BOOLEAN NOT NULL
);
ALTER TABLE
    "person" ADD CONSTRAINT "person_person_national_code_unique" UNIQUE("person-national-code");
CREATE TABLE "hospital-doctor"(
    "doctor-id" INTEGER NOT NULL,
    "hospital-id" INTEGER NOT NULL,
    "start-cooperation" DATE NOT NULL,
    "finish-cooperation" DATE NULL
    UNIQUE TO 
);
ALTER TABLE
    "hospital-doctor" ADD PRIMARY KEY("doctor-id","hospital-id");

alter table add column id 

CREATE TABLE "phone-number"(
    "phone-number-id" SERIAL NOT NULL PRIMARY KEY,
    "phone-number" INTEGER NOT NULL ,
    "person-id" INTEGER NOT NULL
);

CREATE TABLE "hospital"(
    "hospital-id" SERIAL NOT NULL PRIMARY KEY,
    "hospital-name" VARCHAR(120) NOT NULL,
    "hospital-address" VARCHAR(200) NOT NULL
);

CREATE TABLE "medicine"(
    "medicine-id" SERIAL NOT NULL PRIMARY KEY,
    "appointment-id" INTEGER NOT NULL,
    "medicine-name" VARCHAR(100) NOT NULL
);

CREATE TABLE "patient"(
    "patient-id" SERIAL NOT NULL PRIMARY KEY,
    "patient-hospitalization-date-start" DATE NOT NULL,
    "patient-hospitalization-date-finish" DATE NOT NULL,
    "patient-hospitalization-reason" TEXT NOT NULL,
    "patient-hospitalization-bill" DECIMAL(8, 2) NOT NULL,
    "person-id" INTEGER NOT NULL,
    "bed-id" INTEGER NOT NULL
);


CREATE TABLE "room"(
    "room-id" SERIAL NOT NULL PRIMARY KEY,
    "room-name" VARCHAR(100) NOT NULL,
    "room-type" VARCHAR(100) NOT NULL,
    "hospital-id" INTEGER NOT NULL
);

CREATE TABLE "bill"(
    "bill-id" SERIAL NOT NULL PRIMARY KEY,
    "bill-payment-date" DATE NOT NULL,
    "bill-amount" DECIMAL(8, 2) NOT NULL,
    "patient-id" INTEGER NOT NULL,
    "bill-description" TEXT NOT NULL
);

CREATE TABLE "doctor"(
    "doctor-id" SERIAL NOT NULL PRIMARY KEY,
    "doctor-specialist" VARCHAR(120) NOT NULL,
    "person-id" INTEGER NOT NULL,
    "doctor-medical-system-code" BIGINT NOT NULL
);


ALTER TABLE
    "doctor" ADD CONSTRAINT "doctor_person_id_unique" UNIQUE("person-id");
ALTER TABLE
    "bed" ADD CONSTRAINT "bed_room_id_foreign" FOREIGN KEY("room-id") REFERENCES "room"("room-id");
ALTER TABLE
    "bill" ADD CONSTRAINT "bill_patient_id_foreign" FOREIGN KEY("patient-id") REFERENCES "patient"("patient-id");
ALTER TABLE
    "medicine" ADD CONSTRAINT "medicine_appointment_id_foreign" FOREIGN KEY("appointment-id") REFERENCES "appointment"("appointment-id");
ALTER TABLE
    "patient" ADD CONSTRAINT "patient_person_id_foreign" FOREIGN KEY("person-id") REFERENCES "person"("person-id");
ALTER TABLE
    "patient" ADD CONSTRAINT "patient_bed_id_foreign" FOREIGN KEY("bed-id") REFERENCES "bed"("bed-id");
ALTER TABLE
    "phone-number" ADD CONSTRAINT "phone_number_person_id_foreign" FOREIGN KEY("person-id") REFERENCES "person"("person-id");
ALTER TABLE
    "appointment" ADD CONSTRAINT "appointment_patient_id_foreign" FOREIGN KEY("patient-id") REFERENCES "patient"("patient-id");
ALTER TABLE
    "hospital" ADD CONSTRAINT "hospital_hospital_id_foreign" FOREIGN KEY("hospital-id") REFERENCES "hospital-doctor"("hospital-id");
ALTER TABLE
    "room" ADD CONSTRAINT "room_hospital_id_foreign" FOREIGN KEY("hospital-id") REFERENCES "hospital"("hospital-id");
ALTER TABLE
    "doctor" ADD CONSTRAINT "doctor_person_id_foreign" FOREIGN KEY("person-id") REFERENCES "person"("person-id");
ALTER TABLE
    "doctor" ADD CONSTRAINT "doctor_doctor_id_foreign" FOREIGN KEY("doctor-id") REFERENCES "hospital-doctor"("doctor-id");

alter table patient drop column "patient-hospitalization-bill" ;