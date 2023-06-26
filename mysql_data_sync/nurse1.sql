/*
-- Query: select * from allpersons
LIMIT 0, 1000

-- Date: 2023-05-24 10:19
*/

use Medical_Record;

INSERT INTO `allpersons` (`personality`,`id`,`created_at`,`updated_at`,`firstname`,`surname`,`middlename`,`phone`,`_Person__nin`,`nextofkinnin`,`address`,`sex`,`dob`) VALUES ('nurses','4079e47b-3c3e-417a-bea6-e2db9c841a35','2023-05-24 03:35:07','2023-05-24 04:39:33','Rose','Gwom','Yohanna','08122420302','84930498273','87909876567','abuja nigeria','Male','1999-03-03 00:00:00');
INSERT INTO `nurses` (`occupation`,`insurance`,`allperson_id`) VALUES ('Nurse',NULL,'4079e47b-3c3e-417a-bea6-e2db9c841a35');
INSERT INTO `personauth` (`email`,`_PersonAuth__hashed_password`,`person_id`,`session_token`,`reset_token`) VALUES ('myrose@gmail.com','$argon2id$v=19$m=65536,t=3,p=4$vLbwO+lQKrAaV53J+ARQ8Q$VSl5cfQCfyAUKKXppcXUdJVuPBBH1wpwQOv9IEe1GB4','4079e47b-3c3e-417a-bea6-e2db9c841a35',NULL,NULL);
