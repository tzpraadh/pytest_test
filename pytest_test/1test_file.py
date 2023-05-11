
def setup_module(module):
    print("Setup Module!")

def teardown_module(module):
    print("Teardown Module!")

class TestClass:
    @classmethod
    def setup_class(cls):
        print("\nSetup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("\nTeardown TestClass!")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1!")
        elif method == self.test2:
            print("\nSetting up test2!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1!")
        elif method ==self.test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down unknown test!")

    def test1(self):
        print("Executing test1!")
        assert True

    def test2(self):
        print("Executing test2!")
        assert True

    def test3(self):
        print("Executing Test3!")
        assert True
        
    def test4(self):
        print("Test")
        assert True



