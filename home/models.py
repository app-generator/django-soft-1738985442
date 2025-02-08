# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nim = models.CharField(max_length=255, null=True, blank=True)
    nidn = models.CharField(max_length=255, null=True, blank=True)
    prodi = models.CharField(max_length=255, null=True, blank=True)
    foto = models.CharField(max_length=255, null=True, blank=True)
    nowa = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Periode(models.Model):

    #__Periode_FIELDS__
    nama = models.CharField(max_length=255, null=True, blank=True)
    tahun = models.IntegerField(null=True, blank=True)
    semester = models.CharField(max_length=255, null=True, blank=True)

    #__Periode_FIELDS__END

    class Meta:
        verbose_name        = _("Periode")
        verbose_name_plural = _("Periode")


class Prodi(models.Model):

    #__Prodi_FIELDS__
    kode = models.CharField(max_length=255, null=True, blank=True)
    nama = models.CharField(max_length=255, null=True, blank=True)

    #__Prodi_FIELDS__END

    class Meta:
        verbose_name        = _("Prodi")
        verbose_name_plural = _("Prodi")


class Matakuliah(models.Model):

    #__Matakuliah_FIELDS__
    deskripsi = models.CharField(max_length=255, null=True, blank=True)

    #__Matakuliah_FIELDS__END

    class Meta:
        verbose_name        = _("Matakuliah")
        verbose_name_plural = _("Matakuliah")


class Kelas(models.Model):

    #__Kelas_FIELDS__
    ruang = models.ForeignKey(Ruangan, on_delete=models.CASCADE)
    matakuliah = models.ForeignKey(Matakuliah, on_delete=models.CASCADE)
    dosen = models.IntegerField(null=True, blank=True)
    periode = models.ForeignKey(Periode, on_delete=models.CASCADE)
    deskripsi = models.CharField(max_length=255, null=True, blank=True)

    #__Kelas_FIELDS__END

    class Meta:
        verbose_name        = _("Kelas")
        verbose_name_plural = _("Kelas")


class Ruangan(models.Model):

    #__Ruangan_FIELDS__
    gedung = models.ForeignKey(Gedung, on_delete=models.CASCADE)

    #__Ruangan_FIELDS__END

    class Meta:
        verbose_name        = _("Ruangan")
        verbose_name_plural = _("Ruangan")


class Lokasi(models.Model):

    #__Lokasi_FIELDS__
    kode = models.CharField(max_length=255, null=True, blank=True)
    deskripsi = models.CharField(max_length=255, null=True, blank=True)

    #__Lokasi_FIELDS__END

    class Meta:
        verbose_name        = _("Lokasi")
        verbose_name_plural = _("Lokasi")


class Gedung(models.Model):

    #__Gedung_FIELDS__
    deskripsi = models.CharField(max_length=255, null=True, blank=True)
    lokasi = models.ForeignKey(lokasi, on_delete=models.CASCADE)

    #__Gedung_FIELDS__END

    class Meta:
        verbose_name        = _("Gedung")
        verbose_name_plural = _("Gedung")


class Jadwalpertemuan(models.Model):

    #__Jadwalpertemuan_FIELDS__
    tanggal = models.DateTimeField(blank=True, null=True, default=timezone.now)
    jam = models.CharField(max_length=255, null=True, blank=True)
    materi = models.CharField(max_length=255, null=True, blank=True)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)

    #__Jadwalpertemuan_FIELDS__END

    class Meta:
        verbose_name        = _("Jadwalpertemuan")
        verbose_name_plural = _("Jadwalpertemuan")


class Presensi(models.Model):

    #__Presensi_FIELDS__
    mahasiswa = models.IntegerField(null=True, blank=True)
    pertemuan = models.ForeignKey(JadwalPertemuan, on_delete=models.CASCADE)
    tanggal = models.DateTimeField(blank=True, null=True, default=timezone.now)
    jam = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    ip = models.CharField(max_length=255, null=True, blank=True)
    agen = models.CharField(max_length=255, null=True, blank=True)

    #__Presensi_FIELDS__END

    class Meta:
        verbose_name        = _("Presensi")
        verbose_name_plural = _("Presensi")



#__MODELS__END
