from unittest import TestCase, main
from student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_without_courses = Student("Ivo")
        self.student_with_courses = Student("Georgi", {"course name": ["note"]})

    def test_correct_initialization(self):
        self.assertEqual(self.student_without_courses.name, "Ivo")
        self.assertEqual(self.student_without_courses.courses, {})
        self.assertEqual(self.student_with_courses.courses, {"course name": ["note"]})

    def test_enroll_correct_add_notes_to_existing_course(self):
        result = self.student_with_courses.enroll("course name", ["second note", "third note"])

        self.assertEqual(self.student_with_courses.courses["course name"], ["note", "second note", "third note"])
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_correct_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student_without_courses.enroll("JS", ["new course"])

        self.assertEqual(self.student_without_courses.courses, {"JS": ["new course"]})
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_correct_add_notes_to_non_existing_course_with_third_param_Y(self):
        result = self.student_without_courses.enroll("JS", ["new course"], "Y")

        self.assertEqual(self.student_without_courses.courses, {"JS": ["new course"]})
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_correct_add_non_existing_course_without_notes(self):
        result = self.student_without_courses.enroll("JS", ["new course"], "N")

        self.assertEqual(self.student_without_courses.courses, {"JS": []})
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_courses.add_notes("some course", "some note")

        self.assertEqual(self.student_without_courses.courses, {})
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_add_notes_to_existing_course(self):
        result = self.student_with_courses.add_notes("course name", "another note")

        self.assertEqual(self.student_with_courses.courses["course name"], ["note", "another note"])
        self.assertEqual(result, "Notes have been updated")

    def test_leave_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_without_courses.leave_course("some course")

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

    def test_leave_existing_course_correct(self):
        result = self.student_with_courses.leave_course("course name")

        self.assertEqual(self.student_with_courses.courses, {})
        self.assertEqual(result, "Course has been removed")


if __name__ == '__main__':
    main()
