UNITTEST

Struktura unittesttestów została pierwotnie zainspirowana JUnitem i ma podobny smak, co główne ramy testów jednostkowych w innych językach. Obsługuje automatyzację testów, udostępnianie kodu konfiguracji i zamykania testów, agregację testów w kolekcje oraz niezależność testów od struktury raportowania.
Aby to osiągnąć, unittestobsługuje kilka ważnych koncepcji w sposób obiektowy:
urządzenie testowe
Stanowisko testowe reprezentuje przygotowanie potrzebne do wykonania jednego lub większej liczby testów i wszelkich powiązanych działań czyszczących. Może to obejmować na przykład tworzenie tymczasowych lub proxy baz danych, katalogów lub uruchamianie procesu serwera.
przypadek testowy
Sprawdzian jest indywidualna jednostka testów. Sprawdza określoną odpowiedź na określony zestaw danych wejściowych. unittestudostępnia klasę bazową TestCase, której można użyć do tworzenia nowych przypadków testowych.
zestaw testów
Zestaw testów to zbiór przypadków testowych, zestawów testów lub obu. Służy do agregacji testów, które powinny być wykonywane razem.
biegacz testowy
Moduł uruchamiający testy to komponent, który organizuje wykonywanie testów i dostarcza wyniki użytkownikowi. Biegacz może użyć interfejsu graficznego, interfejsu tekstowego lub zwrócić specjalną wartość, aby wskazać wyniki wykonywania testów.



Podstawowy przykład 

unittestModuł udostępnia bogaty zestaw narzędzi do konstruowania i uruchamiania testów. Ta sekcja pokazuje, że niewielki podzbiór narzędzi wystarczy, aby zaspokoić potrzeby większości użytkowników.
Oto krótki skrypt do testowania trzech metod ciągów:
 

Przypadek testowy jest tworzony przez tworzenie podklas unittest.TestCase. Trzy indywidualne testy są zdefiniowane za pomocą metod, których nazwy zaczynają się od liter test. Ta konwencja nazewnictwa informuje moduł uruchamiający testy o tym, które metody reprezentują testy.
Istotą każdego testu jest wezwanie assertEqual()do sprawdzenia oczekiwanego wyniku; assertTrue()lub assertFalse() zweryfikować stan; lub assertRaises()sprawdzić, czy został zgłoszony określony wyjątek. Te metody są używane zamiast assertinstrukcji, więc biegacz testów może gromadzić wszystkie wyniki testów i sporządzać raport.
setUp()I tearDown()metody pozwalają określić instrukcje, które będą wykonywane przed i po każdej metody badania. Bardziej szczegółowo omówiono je w sekcji Organizacja kodu testu .
Ostatni blok przedstawia prosty sposób przeprowadzania testów. unittest.main() udostępnia interfejs wiersza poleceń do skryptu testowego. Po uruchomieniu z wiersza poleceń powyższy skrypt generuje dane wyjściowe, które wyglądają następująco:
 

