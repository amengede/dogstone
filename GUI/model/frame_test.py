import unittest
from frame import Frame

class FrameTest(unittest.TestCase):

    def test_center(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        color = [0.1, 0.2, 0.4]

        frame = Frame(center, size, color)

        #can we get the expected center?
        center_gotten = frame.get_center()
        self.assertAlmostEqual(center_gotten[0], 0.1)
        self.assertAlmostEqual(center_gotten[1], 0.2)

        #does the center's getter return a reference?
        center_gotten[1] = 0.4
        second_center = frame.get_center()
        self.assertAlmostEqual(second_center[1], 0.4)
    
    """
        The following tests are not strictly necessary, but
        are included for completeness' sake.
    """

    def test_size(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        color = [0.1, 0.2, 0.4]

        frame = Frame(center, size, color)

        #can we get the expected size?
        size_gotten = frame.get_size()
        self.assertAlmostEqual(size_gotten[0], 0.5)
        self.assertAlmostEqual(size_gotten[1], 0.3)

        #does the size's getter return a reference?
        size_gotten[1] = 0.4
        second_size = frame.get_size()
        self.assertAlmostEqual(second_size[1], 0.4)

    def test_bg_color(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        color = [0.1, 0.2, 0.4]

        frame = Frame(center, size, color)

        #can we get the expected background color?
        color_gotten = frame.get_bg_color()
        self.assertAlmostEqual(color_gotten[0], 0.1)
        self.assertAlmostEqual(color_gotten[1], 0.2)
        self.assertAlmostEqual(color_gotten[2], 0.4)

        #does the color's getter return a reference?
        color_gotten[1] = 0.4
        second_color = frame.get_bg_color()
        self.assertAlmostEqual(second_color[1], 0.4)

if __name__ == "__main__":
    unittest.main()