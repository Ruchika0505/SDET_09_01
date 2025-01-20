import pytest

class Testclass:
    @pytest.mark.third
    def test_methodC(self):
        print("Running method third")
    @pytest.mark.fourth
    def test_methodD(self):
        print("Running method fourth")

    @pytest.mark.first
    def test_methodA(self):
        print("Running method first")

    @pytest.mark.fifth
    def test_methodE(self):
        print("Running method fifth")

    @pytest.mark.second
    def test_methodB(self):
        print("Running method second")
