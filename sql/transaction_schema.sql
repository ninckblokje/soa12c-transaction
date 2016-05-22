CREATE USER transaction IDENTIFIED BY Beheer_01;
  ALTER USER transaction QUOTA UNLIMITED ON system;
  GRANT
CREATE SEQUENCE TO transaction;
  GRANT
CREATE SESSION TO transaction;
  GRANT
  CREATE TABLE TO transaction;