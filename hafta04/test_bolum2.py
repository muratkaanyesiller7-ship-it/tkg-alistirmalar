# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


# 1. Sifre gucu testleri

def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"


def test_7_karakter_sifre_zayif():
    assert sifre_gucu("abcdefg") == "zayıf"


def test_8_karakter_sifre_orta():
    assert sifre_gucu("abcdefgh") == "orta"


def test_11_karakter_sifre_orta():
    assert sifre_gucu("abcdefghijk") == "orta"


def test_12_karakter_sifre_guclu():
    assert sifre_gucu("abcdefghijkl") == "güçlü"


def test_uzun_sifre_guclu():
    assert sifre_gucu("abcdefghijklmn") == "güçlü"


def test_bos_sifre_hata_verir():
    with pytest.raises(ValueError):
        sifre_gucu("")


# 2. Otopark ucreti testleri

def test_0_dakika_ucretsiz():
    assert otopark_ucreti(0) == 0


def test_15_dakika_ucretsiz():
    assert otopark_ucreti(15) == 0


def test_16_dakika_20_tl():
    assert otopark_ucreti(16) == 20


def test_60_dakika_20_tl():
    assert otopark_ucreti(60) == 20


def test_61_dakika_40_tl():
    assert otopark_ucreti(61) == 40


def test_180_dakika_40_tl():
    assert otopark_ucreti(180) == 40


def test_181_dakika_60_tl():
    assert otopark_ucreti(181) == 60


def test_300_dakika_60_tl():
    assert otopark_ucreti(300) == 60


def test_negatif_dakika_hata_verir():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


# 3. Yuzde degisim testleri

def test_yuzde_artis():
    assert yuzde_degisim(200, 250) == 25.0


def test_yuzde_azalis():
    assert yuzde_degisim(200, 150) == -25.0


def test_degisiklik_yok():
    assert yuzde_degisim(100, 100) == 0.0


def test_yuzde_100_artis():
    assert yuzde_degisim(50, 100) == 100.0


def test_yuzde_100_azalis():
    assert yuzde_degisim(100, 0) == -100.0


def test_eski_deger_sifir_hata_verir():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)


def test_negatif_degerlerle_yuzde_degisim():
    assert yuzde_degisim(-100, -50) == -50.0