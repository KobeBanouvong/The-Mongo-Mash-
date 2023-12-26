# The-Mongo-Mash-
Project for CECS 323 (DATABASE FUNDAMENTALS) using MongoDB and Python

GIVEN INSTRUCTIONS:

The objects you need to create and insert:

These activities:
Archery
Swimming
Movie

These campers: Ada; Sofia; Iggy; and Rosie.

These employees: Lila Greer; Marco Valdez; Teresa Thompson; and Aisha Twist

A session titled "Harry Potter Week":

Staff: Lila Greer as "Minerva", assigned the role "Director"; Marco Valdez as "Hermes", assigned the roles "Counselor" and "Lifeguard". Teresa Thompson as "Hera", assigned the role "Counselor"; Aisha Twist as "Athena", assigned the roles of "Counselor" and "Lifeguard".

Units:
Ravenclaw: campers Ada and Sofia. Staff member is Hera.
Hufflepuff: campers Iggy and Rosie. Staff member is Hermes.

Rotations (note that these are created in the Rotations collection, and then referenced/denormalized into the Session object):
Monday Morning: schedule Archery with Ravenclaw, supervised by Minerva
Monday Afternoon: schedule Swimming with Hufflepuff, supervised by Athena.
Tuesday Morning: schedule Swimming with Ravenclaw, supervised by Athena; schedule Archery with Hufflepuff, supervised by Minerva.
Wednesday Morning: no scheduled activities
Wednesday Evening: schedule Movie with Hufflepuff, supervised by Hermes; schedule Archery with Ravenclaw, supervised by Hera.

Python application:
You must now write a Python application using PyMongo to interact with this Girl Scouts database.
Your application should begin with a Main Menu of these options:

Employee Lookup
Input the name of an employee. Retrieve that employee from the database, and print a "summary" view: their ID, full name, wage; and for each session they are working, the the title of that session, the employee's staff name for the session, and the name of the unit they are supervising, if any. (Do not print the unit name if they are not assigned to a unit.)

Session Schedule Summary
Input the ID of a session and the name of an activity.
Retrieve all scheduled activities for that specific activity at that specific session. For each scheduling of the activity, print out the title of the rotation it is scheduled during, the camp name of the staff that is supervising, and the name of the unit that is participating (if any).


Unit Report
Input the name of a unit and the name of a session. Print out a summary of that unit at the session: the name of the unit, and the number of minutes at each different activity during the session. (That is, if Unit A scheduled Archery at Monday Morning (9-11am) and Tuesday Afternoon (2-3pm), they spent 180 total minutes at Archery.)
