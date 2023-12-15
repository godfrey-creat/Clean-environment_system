#!/usr/bin/python3
"""the console"""

import cmd
from datetime import datetime
import models
from models.user import Client
from models.garbage_type import Garbage_type
from models.garbage_collection_company import Garbage_collection_company
from models.base_model import BaseModel
import shlex  # for spliting purposes except when there is double quotes
import argparse
import mysql.connector
import re

classes = {"User": Client, "Garbage_type": Garbage_type, "Garbage_collection_company": Garbage_collection_company, "BaseModel": BaseModel}

class MAZINGIRABORACommand(cmd.Cmd):
    """MAZINGIRA console"""
    prompt = '(mazingirabora)'

    def do_EOF(self, arg):
        """exits console"""
        return True

    def emptyline(self):
        """overwrites an empty line"""
        return False

    def do_quit(self, arg):
        """quits command to the program"""
        return True

    def _key_value_parser(self, args):
        """creates dictionary from list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0]
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """creates new class instance"""
        args = arg.split()
        if len(args) == 0:
            print("*class name missing*")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("*class doesn't exist*")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """ prints instances based on class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("*class name missing*")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("*no instance found*")
            else:
                print("*instance id missing*")
        else:
            print("*class doesn't exist*")

    def do_place_booking(self, args):
        """clients to place bookings for services"""
        args = shlex.split(args)
        if len(args) == 0:
            print("*client id missing*")
            return False
        client_id = args[0]
        if client_id in models.storage.all():
            client = models.storage.all()[client_id]
            location = input("Enter your location:")
            garbage_type = input("Enter the type of waste:")
            garbage_collection_company_id = input("select a garbage_collection_company(enter garbage_collection_company id):")

            #create a booking instance.
            print("Booking placed successfully!")
        else:
            print("*client not found*")

    def do_accept_booking(self, args):
        """garbage collection company to accept bookings"""
        args = shlex.split(args)
        if len(args) == 0:
            print("*garbage_collection_company id missing*")
            return False
        garbage_collection_company_id = args[0]
        if garbage_collection_company_id in models.storage.all():
            garbage_collection_company = models.storage.all()[garbage_collection_company_id]

            #Retrieve and display pending bookings
            booking_id = input("Enter the booking id to accept:")
            #Update booking status.
            print("Booking accepted Successfully!")
        else:
            print("*garbage_collection_company not found*")
    def do_update(self, args):
      """updating data set"""
      args = shlex.split(args)
      integers = ["Amount_of_waste", "pick_up_date"]
      floats = ["type_of_waste", "location"]
      if len(args) == 0:
          print("*class name missing*")
      elif args[0] in classes:
          if len(args) > 1:
              k = args[0] + "." + args[1]
              if k in models.storage.all():
                  if len(args) > 2:
                      if len(args) > 3:
                          if args[0] == "Location":
                              if args[2] in integers:
                                  try:
                                      args[3] = int[args[3]]
                                  except:
                                      args[3] = 0.0
                                  setattr(
    models.storage.all()[k], args[2], args[3])
                                  models.storage.all()[k].save()
                              else:
                                  print("*value missing*")
                      else:
                          print("*attribute missing*")
              else:
                  print("*no instance found*")
      else:
          print("*instance id missing*")



if __name__ == '__main__':
    MAZINGIRABORACommand().cmdloop()






  

                    
