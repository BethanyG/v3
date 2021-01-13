import unittest
from list_methods import *


class TestListMethods(unittest.TestCase):
    def test_add_me_to_the_queue_set_1(self):
        express_queue   = ["Tony", "Bruce"]
        normal_queue    = ["RobotGuy", "WW"]
        ticket_type     = 1
        person_name     = "RichieRich"
        expected_result = ["Tony", "Bruce", "RichieRich"]

        self.assertListEqual(add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name),
                             expected_result,
                             msg=f"Expected: {expected_result}, but {person_name} was not added to the queue correctly.")


    def test_add_me_to_the_queue_set_2(self):
        express_queue   = ["Tony", "Bruce"]
        normal_queue    = ["RobotGuy", "WW"]
        ticket_type     = 0
        person_name     = "HawkEye"
        expected_result = ["RobotGuy", "WW", "HawkEye"]

        self.assertListEqual(
            add_me_to_the_queue(express_queue,normal_queue,ticket_type, person_name),
                                expected_result,
                                msg=f"Expected: {expected_result}, but {person_name} was not "
                                    f"added to the queue correctly.")


    def test_find_his_friend_set_1(self):
        queue           =  ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"]
        friend_name     =  "Steve"
        expected_result =  1

        self.assertIs(find_his_friend(queue, friend_name), expected_result,
                      msg=f"Expected: index {expected_result}, but the index "
                          f"returned for {friend_name} is incorrect.")


    def test_find_his_friend_set_2(self):
        queue       =  ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"]
        friend_name =  "Rocket"
        expected_result = 4

        self.assertIs(find_his_friend(queue, friend_name), expected_result,
                      msg=f"Expected: index {expected_result}, but the index "
                          f"returned for {friend_name} is incorrect.")


    def test_add_person_with_his_friends_set_1(self):
        queue           = ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"]
        index           = 1
        person_name     = "Bucky"
        expected_result = ["Natasha", "Bucky", "Steve", "Tchalla", "Wanda", "Rocket"]

        self.assertListEqual(add_person_with_his_friends(queue, index, person_name), expected_result,
                             msg=f"Expected: {expected_result}, but {person_name} got "
                                 f"added in an incorrect location.")


    def test_add_person_with_his_friends_set_2(self):
        queue           = ["Natasha", "Steve", "Tchalla", "Wanda", "Rocket"]
        index           = 0
        person_name     = "Bucky"
        expected_result = ["Bucky", "Natasha", "Steve", "Tchalla", "Wanda", "Rocket"]

        self.assertListEqual(add_person_with_his_friends(queue, index, person_name),expected_result,
                             msg=f"Expected: {expected_result}, but {person_name} was added "
                                 f"to an incorrect location in line.")


    def test_remove_the_mean_person_set_1(self):
        queue           = ["Natasha", "Steve", "Eltran", "Wanda", "Eltran", "Rocket"]
        person_name     = "Eltran"
        expected_result = ["Natasha", "Steve", "Wanda", "Rocket"]

        self.assertListEqual(remove_the_mean_person(queue, person_name), expected_result,
                             msg=f"Expected: {expected_result}, but mean {person_name} was"
                                 f" not removed properly, and is still bothering people.")


    def test_remove_the_mean_person_set_2(self):
        queue           = ["Natasha", "Steve", "Eltran", "Wanda", "Eltran", "Rocket"]
        person_name     = "Eltran"
        expected_result = ["Natasha", "Steve", "Wanda", "Eltran", "Rocket"]

        self.assertListEqual(remove_the_mean_person(queue, person_name), expected_result,
                             msg=f"Expected: {expected_result}, but mean {person_name} was"
                             f" not removed properly, and is still bothering people.")


    def test_how_many_namefellows_set_1(self):
        queue           = ["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]
        person_name     = "Bucky"
        expected_result = 0

        self.assertIs(how_many_namefellows(queue,person_name), expected_result,
                      msg=f"Expected a count of {expected_result}, but the name count is incorrect."
        )

    def test_how_many_namefellows_set_2(self):
        queue           = ["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]
        person_name     = "Natasha"
        expected_result = 2

        self.assertIs(how_many_namefellows(queue, person_name), expected_result,
                      msg=f"Expected a count of {expected_result}, but the count is incorrect."
        )

    def test_remove_the_last_person(self):
        queue           = ["Natasha", "Steve", "Eltran", "Natasha", "Rocket"]
        expected_result = "Rocket"

        self.assertIs(remove_the_last_person(queue), expected_result,
                      msg=f"Expected: {expected_result} to be the person "
                          f"removed, but {expected_result} did not get removed properly.")

    def test_sorted_names(self):
        queue           =  ["Steve", "Eltran", "Natasha", "Rocket"]
        expected_result =  ['Eltran', 'Natasha', 'Rocket', 'Steve']

        self.assertListEqual(sorted_names(queue),expected_result,
                             msg=f"Expected the queue to look like {expected_result}, "
                                 f"but it didn't get properly sorted.")
