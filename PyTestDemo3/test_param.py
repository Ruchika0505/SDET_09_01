import pytest

class TestClass:
    @pytest.mark.parametrize("num1,num2",[(10,10),(3,5),(4,4),(8,3)])
    def test_calculate(self,num1,num2):
        assert num1==num2
        