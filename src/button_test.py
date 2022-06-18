import unittest
from button import Button

class ButtonTest(unittest.TestCase):

    def test_text(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        text = "Test Text"
        bg_color = [0.1, 0.2, 0.4]
        fg_color = [0, 0, 0]
        highlight_color = [0.9, 0.8, 0.6]

        button = Button(
            center, size, bg_color,
            text, fg_color, highlight_color)

        #can we get the expected text?
        text_gotten = button.get_text()
        self.assertEqual(text_gotten, "Test Text")

        #Does the function return a copy of the text?
        text_gotten = "Oh no, this isn't the right text"
        second_text = button.get_text()
        self.assertAlmostEqual(second_text, "Test Text")
    
    def test_inside(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        text = "Test Text"
        bg_color = [0.1, 0.2, 0.4]
        fg_color = [0, 0, 0]
        highlight_color = [0.9, 0.8, 0.6]

        button = Button(
            center, size, bg_color,
            text, fg_color, highlight_color)

        #does the inside function work properly?
        left_of_button = (-0.5, 0.2)
        right_of_button = (0.75, 0.2)
        above_button = (0.1, 0.9)
        below_button = (0.1, -0.2)
        inside_button = (0.2, 0.25)

        self.assertFalse(button.inside(left_of_button))
        self.assertFalse(button.inside(right_of_button))
        self.assertFalse(button.inside(above_button))
        self.assertFalse(button.inside(below_button))
        self.assertTrue(button.inside(inside_button))
    
    """
        The following tests are not strictly necessary, but
        are included for completeness' sake.
    """

    def test_center(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        text = "Test Text"
        bg_color = [0.1, 0.2, 0.4]
        fg_color = [0, 0, 0]
        highlight_color = [0.9, 0.8, 0.6]

        button = Button(
            center, size, bg_color,
            text, fg_color, highlight_color)

        #can we get the expected center?
        center_gotten = button.get_center()
        self.assertAlmostEqual(center_gotten[0], 0.1)
        self.assertAlmostEqual(center_gotten[1], 0.2)

        #does the center's getter return a reference?
        center_gotten[1] = 0.4
        second_center = button.get_center()
        self.assertAlmostEqual(second_center[1], 0.4)

    def test_size(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        text = "Test Text"
        bg_color = [0.1, 0.2, 0.4]
        fg_color = [0, 0, 0]
        highlight_color = [0.9, 0.8, 0.6]

        button = Button(
            center, size, bg_color,
            text, fg_color, highlight_color)

        #can we get the expected size?
        size_gotten = button.get_size()
        self.assertAlmostEqual(size_gotten[0], 0.5)
        self.assertAlmostEqual(size_gotten[1], 0.3)

        #does the size's getter return a reference?
        size_gotten[1] = 0.4
        second_size = button.get_size()
        self.assertAlmostEqual(second_size[1], 0.4)

    def test_bg_color(self):

        center = [0.1, 0.2]
        size = [0.5, 0.3]
        text = "Test Text"
        bg_color = [0.1, 0.2, 0.4]
        fg_color = [0, 0, 0]
        highlight_color = [0.9, 0.8, 0.6]

        button = Button(
            center, size, bg_color,
            text, fg_color, highlight_color)

        #can we get the expected background color?
        color_gotten = button.get_bg_color()
        self.assertAlmostEqual(color_gotten[0], 0.1)
        self.assertAlmostEqual(color_gotten[1], 0.2)
        self.assertAlmostEqual(color_gotten[2], 0.4)

        #does the color's getter return a reference?
        color_gotten[1] = 0.4
        second_color = button.get_bg_color()
        self.assertAlmostEqual(second_color[1], 0.4)

if __name__ == "__main__":
    unittest.main()