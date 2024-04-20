from domain import (
    Class,
    Course,
    Department,
    Instructor,
    MeetingTime,
    Room,
)

class Data(object):
    def __init__(self, data_dict):
        self.rooms = self.initialize_rooms(data_dict)
        self.instructors = self.initialize_instructors(data_dict)
        self.courses = self.initialize_courses(data_dict)
        self.depts = self.initialize_departments(data_dict)
        self.meeting_times = self.initialize_meeting_times(data_dict)
        self.meeting_time_ids = [mt.id for mt in self.meeting_times if mt.id]
        self.number_of_classes = sum([len(dept.courses) for dept in self.depts])

    def initialize_rooms(self, data_dict):
        num_rooms = int(data_dict["num_rooms"])
        rooms = []
        for i in range(1, num_rooms + 1):
            room_number = data_dict.get(f"room_{i}_number")
            seating_capacity = int(data_dict.get(f"room_{i}_capacity", 0))  # Default to 0 if capacity is missing
            room = Room(number=room_number, seating_capacity=seating_capacity)
            rooms.append(room)
        return rooms



    def initialize_instructors(self, data_dict):
        num_instructors = int(data_dict["num_instructors"])
        instructors = []
        for i in range(1, num_instructors + 1):
            instructor_id = data_dict[f"instructor_{i}_id"]
            instructor_name = data_dict[f"instructor_{i}_name"]
            instructor = Instructor(id=instructor_id, name=instructor_name)
            instructors.append(instructor)
        return instructors

    def initialize_courses(self, data_dict):
        num_courses = int(data_dict["num_courses"])
        courses = []
        for i in range(1, num_courses + 1):
            course_number = data_dict[f"course_{i}_number"]
            course_name = data_dict[f"course_{i}_name"]
            max_students = int(data_dict[f"course_{i}_max_students"])
            num_instructors = int(data_dict[f"course_{i}_num_instructors"])

            instructor_ids = [data_dict.get(f"course_{i}_instructor_{j}_id", None) for j in range(1, num_instructors + 1)]
            instructor_ids = [id_ for id_ in instructor_ids if id_ is not None]
            instructors = [inst for inst in self.instructors if inst.id in instructor_ids]
            course = Course(number=course_number, name=course_name, max_number_of_students=max_students, instructors=instructors)
            courses.append(course)
        return courses


    def initialize_departments(self, data_dict):
        num_departments = int(data_dict["num_departments"])
        departments = []
        for i in range(1, num_departments + 1):
            dept_name = data_dict["department_name"]
            courses = [course for course in self.courses if course.number in [data_dict[f"dept_course_{j}"] for j in range(1, int(data_dict["courses_in_department"]) + 1)]]
            department = Department(name=dept_name, courses=courses)
            departments.append(department)
        return departments


    def initialize_meeting_times(self, data_dict):
        meeting_times = []
        try:
            num_meeting_times = int(data_dict["num_meeting_times"])
        except KeyError:
            raise KeyError("Key 'num_meeting_times' not found in data_dict")
        except ValueError:
            raise ValueError("Value for 'num_meeting_times' must be an integer")

        for i in range(1, num_meeting_times + 1):
            meeting_time_id = data_dict.get(f"meeting_time_{i}_id", None)  # Provide default value if key is missing
            meeting_time_str = data_dict.get(f"meeting_time_{i}", "")  # Provide default value if key is missing
            meeting_time = MeetingTime(id=meeting_time_id, time=meeting_time_str)
            meeting_times.append(meeting_time)

        return meeting_times
