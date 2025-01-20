import pytest

class Testclass:

    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("Running method third")
    @pytest.mark.run(order=4)
    def test_methodD(self):
        print("Running method fourth")

    @pytest.mark.run(order=1)
    def test_methodA(self):
        print("Running method first")

    @pytest.mark.run(order=5)
    def test_methodE(self):
        print("Running method fifth")

    @pytest.mark.second
    def test_methodB(self):
        print("Running method second")



