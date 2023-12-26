from pymongo import MongoClient
from bson import ObjectId


def connect():
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client['project3']


def employee_lookup(first_name, last_name):
    db = connect()
    find_employee = [
        {
            '$match': {
                'firstName': first_name,
                'lastName': last_name,
            }
        }, {
            '$project': {
                '_id': 1,
                'firstName': 1,
                'lastName': 1,
                'wage': 1,
                'sessions': 1
            }
        }
    ]
    results = db["employees"].aggregate(find_employee)
    for employee in results:
        print(f"\nEmployee ID: {employee['_id']}")
        print(
            f"Full Name: {employee['firstName']} {employee['lastName']}")
        print(f"Wage: ${employee['wage']}")
        for session in employee['sessions']:
            print(f"Session Title: {session['sessionTitle']}")
            print(f"Staffs Name: {session['campName']}")
            if 'unitName' in session:
                print(f"Unit Supervising: {session['unitName']}\n")
\


def session_schedule_summary(session_id, activity_name):
    db = connect()
    schedule_summary = [
        {
            "$match": {
                "sessionId": ObjectId(session_id)
            }
        },
        {
            "$unwind": "$schedule"
        },
        {
            "$match": {
                "schedule.activityName": activity_name
            }
        },
        {
            "$project": {
                "_id": 0,
                "title": 1,
                "staffCampName": "$schedule.staffCampName",
                "unitName": "$schedule.unitName"
            }
        }
    ]
    results = db["rotations"].aggregate(schedule_summary)
    for activity in results:
        print(f"\nRotation Title: {activity['title']}")
        print(f"Staff Camp Name: {activity['staffCampName']}")
        print(f"Unit Name: {activity['unitName']}\n")


def unit_report(session_name, unit_name):
    db = connect()
    report_of_unit = [
        {
            '$match': {
                'title': session_name
            }
        }, {
            '$unwind': '$units'
        }, {
            '$lookup': {
                'from': 'rotations',
                'let': {
                    'unitId': '$units._id'
                },
                'pipeline': [
                    {
                        '$match': {
                            '$expr': {
                                '$in': [
                                    '$$unitId', '$schedule.unitId'
                                ]
                            }
                        }
                    }, {
                        '$unwind': '$schedule'
                    }
                ],
                'as': 'joinedRotations'
            }
        }, {
            '$unwind': '$joinedRotations'
        }, {
            '$unwind': '$joinedRotations.schedule'
        }, {
            '$match': {
                'units.unitName': unit_name
            }
        }, {
            '$project': {
                '_id': 0,
                'activityName': '$joinedRotations.schedule.activityName',
                'duration': {
                    '$divide': [
                        {
                            '$subtract': [
                                '$joinedRotations.endTime', '$joinedRotations.startTime'
                            ]
                        }, 60000
                    ]
                }
            }
        }, {
            '$group': {
                '_id': '$activityName',
                'totalDuration': {
                    '$sum': '$duration'
                }
            }
        }
    ]
    results = db["sessions"].aggregate(report_of_unit)
    for units in results:
        print(f"\nActvity Name: {units['_id']}")
        print(f"Duration: {units['totalDuration']} minutes\n")


def main():
    while True:
        print("\nMain Menu: ")
        print("1. Employee Lookup")
        print("2. Session Scedule Summary")
        print("3. Unit Report")
        print("4. Exit")

        pick = input("Enter your choice (1-4): ")

        if pick == '1':
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            employee_lookup(first_name, last_name)

        elif pick == '2':
            while True:
                session_id = input("Enter Session ID: ").strip()
                if ObjectId.is_valid(session_id):
                    break
                else:
                    print(
                        "Invalid Session ID. Please enter a valid 12-byte input or a 24-character hex string.")
            activity_name = input("Enter Activity Name: ").strip()
            session_schedule_summary(session_id, activity_name)

        elif pick == '3':
            unit_name = input("Enter the name of the unit: ").strip()
            session_name = input("Enter the name of the session: ").strip()
            unit_report(session_name, unit_name)

        elif pick == '4':
            print("Goodbye :)")
            break
        else:
            print("Invalid choice. Please enter a number between 1 - 4")


if __name__ == "__main__":
    main()
