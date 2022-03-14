import unittest
#import problem7_patientToDict
from problem7_patientToDict import problem7
class TestProblem7(unittest.TestCase):
    def test_happyPath(self):
        #Test if the output is correct
        expected_output={'Vaishnavi_Krishnapur': 2, 'K_v': 1, 'vaishnavi': 3, 'Krishnapur': 1}
        obj=problem7()
        self.assertEqual(obj.get_patient_visits_dict("Problem7_input.txt"),expected_output)
