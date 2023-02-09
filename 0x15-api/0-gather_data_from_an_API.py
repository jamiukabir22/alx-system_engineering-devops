#!/usr/bin/python3
""" A REST API for a given employee ID
    Return information about the employee's TODO list
"""
import requests as e
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        args = {"id": sys.argv[1]}
        user_list = e.get("https://jsonplaceholder.typicode.com/users",
                          params=args).json()
        args = {"userId": sys.argv[1]}
        todo_list = e.get("https://jsonplaceholder.typicode.com/todos",
                          params=args).json()
        t_len = 0
        t_arr = []
        for j in todo_list:
            if j.get("completed"):
                t_arr.append(j)
                t_len += 1
        print("Employee {} is done with tasks({}/{}):".format(
            user_list[0].get("name"), t_len, len(todo_list)))
        for i in t_arr:
            print("\t {}".format(i.get("title")))
