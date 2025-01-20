import pytest

class TestClass:
    @pytest.fixture()  # decorator-- annotation in TestNG
    def setup(self):
        print("Launching browser")
        yield
        print("Closing browser")


    def test_login(self,setup):
        print("This is Login Method")
    def test_search(self,setup):
        print("This is Search Method")
    def test_AdvancedSearch(self,setup):
        print("This is Advanced Search Method")

