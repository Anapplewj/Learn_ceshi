import time
import unittest
from Pra0720 import testbaidu1
from Pra0720 import testbaidu2


def createsuit():
    # suite=unittest.TestSuite()
    # suite.addTest(testbaidu1.Baidu1("test_hao"))
    # suite.addTest(testbaidu1.Baidu1("test_baidusearch"))
    #
    # time.sleep(3)
    # suite.addTest(testbaidu2.Baidu2("test_hao"))
    # suite.addTest(testbaidu2.Baidu2("test_baidusearch"))

    # makesuit

    # suite=unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(testbaidu1.Baidu1))
    # suite.addTest(unittest.makeSuite(testbaidu2.Baidu2))
    # return suite

    # TestLoader

    # suite1 = unittest.TestLoader.loadTestsFromTestCase(testbaidu1.Baidu1)
    # suite2 = unittest.TestLoader.loadTestsFromTestCase(testbaidu2.Baidu2)
    # suite3 = unittest.TestSuite([suite1, suite2])
    # return suite3

    # discover
    discover=unittest.defaultTestLoader.discover("../pra0720", pattern="testbaidu*.py", top_level_dir=None)
    print(discover)
    return discover

if __name__=='__main__':
    suite=createsuit()
    runner=unittest.TextTestRunner(verbosity=1)
    runner.run(suite)