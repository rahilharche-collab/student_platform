import uuid
from django.db import models

WILAYA_CHOICES = [
    ('1 - Adrar', '1 - Adrar'),
    ('2 - Chlef', '2 - Chlef'),
    ('3 - Laghouat', '3 - Laghouat'),
    ('4 - Oum El Bouaghi', '4 - Oum El Bouaghi'),
    ('5 - Batna', '5 - Batna'),
    ('6 - Béjaïa', '6 - Béjaïa'),
    ('7 - Biskra', '7 - Biskra'),
    ('8 - Béchar', '8 - Béchar'),
    ('9 - Blida', '9 - Blida'),
    ('10 - Bouira', '10 - Bouira'),
    ('11 - Tamanrasset', '11 - Tamanrasset'),
    ('12 - Tébessa', '12 - Tébessa'),
    ('13 - Tlemcen', '13 - Tlemcen'),
    ('14 - Tiaret', '14 - Tiaret'),
    ('15 - Tizi Ouzou', '15 - Tizi Ouzou'),
    ('16 - Alger', '16 - Alger'),
    ('17 - Djelfa', '17 - Djelfa'),
    ('18 - Jijel', '18 - Jijel'),
    ('19 - Sétif', '19 - Sétif'),
    ('20 - Saïda', '20 - Saïda'),
    ('21 - Skikda', '21 - Skikda'),
    ('22 - Sidi Bel Abbès', '22 - Sidi Bel Abbès'),
    ('23 - Annaba', '23 - Annaba'),
    ('24 - Guelma', '24 - Guelma'),
    ('25 - Constantine', '25 - Constantine'),
    ('26 - Médéa', '26 - Médéa'),
    ('27 - Mostaganem', '27 - Mostaganem'),
    ('28 - M’Sila', '28 - M’Sila'),
    ('29 - Mascara', '29 - Mascara'),
    ('30 - Ouargla', '30 - Ouargla'),
    ('31 - Oran', '31 - Oran'),
    ('32 - El Bayadh', '32 - El Bayadh'),
    ('33 - Illizi', '33 - Illizi'),
    ('34 - Bordj Bou Arréridj', '34 - Bordj Bou Arréridj'),
    ('35 - Boumerdès', '35 - Boumerdès'),
    ('36 - El Tarf', '36 - El Tarf'),
    ('37 - Tindouf', '37 - Tindouf'),
    ('38 - Tissemsilt', '38 - Tissemsilt'),
    ('39 - El Oued', '39 - El Oued'),
    ('40 - Khenchela', '40 - Khenchela'),
    ('41 - Souk Ahras', '41 - Souk Ahras'),
    ('42 - Tipaza', '42 - Tipaza'),
    ('43 - Mila', '43 - Mila'),
    ('44 - Aïn Defla', '44 - Aïn Defla'),
    ('45 - Naâma', '45 - Naâma'),
    ('46 - Aïn Témouchent', '46 - Aïn Témouchent'),
    ('47 - Ghardaïa', '47 - Ghardaïa'),
    ('48 - Relizane', '48 - Relizane'),
    ('49 - Timimoun', '49 - Timimoun'),
    ('50 - Bordj Badji Mokhtar', '50 - Bordj Badji Mokhtar'),
    ('51 - Ouled Djellal', '51 - Ouled Djellal'),
    ('52 - Béni Abbès', '52 - Béni Abbès'),
    ('53 - In Salah', '53 - In Salah'),
    ('54 - In Guezzam', '54 - In Guezzam'),
    ('55 - Touggourt', '55 - Touggourt'),
    ('56 - Djanet', '56 - Djanet'),
    ('57 - El M’Ghair', '57 - El M’Ghair'),
    ('58 - El Menia', '58 - El Menia'),
]

class Student(models.Model):
    registration_number = models.CharField(max_length=8, unique=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    master_average = models.FloatField()
    wilaya = models.CharField(max_length=100, choices=WILAYA_CHOICES)
    agree_to_terms = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.registration_number:
            self.registration_number = str(uuid.uuid4())[:8]  # Generate 8-char code
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
