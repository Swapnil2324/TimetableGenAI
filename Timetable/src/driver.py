import json

from tabulate import tabulate
from os import sys, path

from utils import print_data, print_population_schedules, print_schedule_as_table

POPULATION_SIZE           = 9
MUTATION_RATE             = 0.1
CROSSOVER_RATE            = 0.9
TOURNAMENT_SELECTION_SIZE = 3
NUMB_OF_ELITE_SCHEDULES   = 1

def run(data_dict):
  global SCHEDULE_NUMBER, CLASS_NO

  from data import Data
  from genetic_algorithm import GeneticAlgorithm
  from population import Population

  generation_number = 0
  data = Data(data_dict)

  _genetic_algorithm = GeneticAlgorithm(data=data)
  _population = Population(size=POPULATION_SIZE, data=data).sort_by_fitness()

  print_data(data=data)

  print_population_schedules(population=_population, generation_number=generation_number)
  print_schedule_as_table(data=data, schedule=_population.schedules[0], generation=generation_number)

  while _population.schedules[0].fitness != 1.0:
    generation_number += 1
    _population = _genetic_algorithm.evolve(population=_population).sort_by_fitness()

    print_population_schedules(population=_population, generation_number=generation_number)
    print_schedule_as_table(data=data, schedule=_population.schedules[0], generation=generation_number)

if __name__ == '__main__' and __package__ is None:
    if len(sys.argv) != 2:
          print("Usage: python driver.py <data_json>")
          sys.exit(1)

    data_json = sys.argv[1]
    data_dict = json.loads(data_json)

 
    run(data_dict)






















    # data_dict={
    # "num_rooms": "2",
    # "room_1_number": "CS101",
    # "room_1_capacity": "20",
    # "room_2_number": "CS202",
    # "room_2_capacity": "30",
    # "num_instructors": "2",
    # "instructor_1_id": "123",
    # "instructor_1_name": "Prof. Kumar",
    # "instructor_2_id": "456",
    # "instructor_2_name": "Ms. Lee",
    # "num_courses": "3",
    # "course_1_number": "CSE431",
    # "course_1_name": "Algorithm",
    # "course_1_max_students": "25",
    # "course_1_num_instructors": "2",
    # "course_1_instructor_1_id": "123",
    # "course_1_instructor_2_id": "456",
    # "course_2_number": "CSE311",
    # "course_2_name": "Dsat struc",
    # "course_2_max_students": "30",
    # "course_2_num_instructors": "1",
    # "course_2_instructor_1_id": "123",
    # "course_3_number": "CSE220",
    # "course_3_name": "DM",
    # "course_3_max_students": "30",
    # "course_3_num_instructors": "1",
    # "course_3_instructor_1_id": "123",
    # "num_departments": "1",
    # "department_name": "CSEDep",
    # "courses_in_department": "3",
    # "dept_course_1": "CSE431",
    # "dept_course_2": "CSE311",
    # "dept_course_3": "CSE220",
    # "num_meeting_times": "2",
    # "meeting_time_1_id": "1",
    # "meeting_time_1": "TTH 10:00 - 11:00",
    # "meeting_time_2_id": "2",
    # "meeting_time_2": "MWF 13:00 - 14:00"
    # }
   