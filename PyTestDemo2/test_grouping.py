import pytest

class TestClass:
    @pytest.mark.sanity
    def test_LoginByFacebook(self):
        print("This is login By Facebook")
        assert True==True

    @pytest.mark.regression
    def test_LoginByEmail(self):
        print("This is login By Email")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_LoginByTwitter(self):
        print("This is login By Twitter")
        assert True == True

    @pytest.mark.sanity
    def test_signupByEmail(self):
        print("This is Method signup By Email")
        assert True == True

    @pytest.mark.regression
    def test_signupByFacbook(self):
        print("This is Method signup By facebbook")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_signupByTwitter(self):
        print("This is Method signup By Twitter")
        assert True == True
