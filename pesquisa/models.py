from django.db import models
from django.db.models.constraints import UniqueConstraint

linha = (
    ('1', 'CTR - CENTRO'),
    ('2', 'SUL - SUL'),
    ('3', 'DSL - DIESEL')
)

horario = (
    ('1', '05-06'),
    ('2', '06-07'),
    ('4', '07-08'),
    ('5', '08-09'),
    ('6', '09-10'),
    ('7', '10-11'),
    ('8', '11-12'),
    ('9', '12-13'),
    ('10', '13-14'),
    ('11', '14-15'),
    ('12', '15-16'),
    ('13', '16-17'),
    ('14', '17-18'),
    ('15', '18-19'),
    ('16', '19-20'),
    ('17', '20-21'),
    ('18', '21-22'),
    ('19', '22-23')
)

adesivo = (
    ('1', 'VERDE'),
    ('2', 'MARROM'),
    ('3', 'AZUL')
)


class Urna(models.Model):
    serial = models.CharField(
        max_length=255, blank=False, null=False, verbose_name="Serial")
    linha = models.CharField(
        max_length=255, verbose_name="Linha", choices=linha)
    horario = models.CharField(
        max_length=255, verbose_name="Horário", choices=horario)
    adesivo = models.CharField(
        max_length=255, verbose_name="Adesivo", choices=adesivo)

    def __str__(self):
        return self.serial

    class Meta:
        verbose_name_plural = "Urnas"
        unique_together = ('serial',)
