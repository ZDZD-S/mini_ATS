import csv
import os

# Utility Functions
def read_csv(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_to_csv(file_path, fieldnames, data):
    write_header = not os.path.exists(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(data)

# Core ATS Functions
def add_job(title, description):
    jobs = read_csv('jobs.csv')
    job_id = str(len(jobs) + 1)
    job = {'id': job_id, 'title': title, 'description': description}
    write_to_csv('jobs.csv', ['id', 'title', 'description'], job)

def register_candidate(name, email):
    candidates = read_csv('candidates.csv')
    candidate_id = str(len(candidates) + 1)
    candidate = {'id': candidate_id, 'name': name, 'email': email}
    write_to_csv('candidates.csv', ['id', 'name', 'email'], candidate)

def submit_application(job_id, candidate_id):
    applications = read_csv('applications.csv')
    application_id = str(len(applications) + 1)
    application = {
        'application_id': application_id,
        'job_id': job_id,
        'candidate_id': candidate_id,
        'status': 'pending'
    }
    write_to_csv('applications.csv', ['application_id', 'job_id', 'candidate_id', 'status'], application)

# User Interaction Functions
def interact_add_job():
    print("Enter job details:")
    title = input("Title: ")
    description = input("Description: ")
    add_job(title, description)
    print("Job added successfully.")

def interact_register_candidate():
    print("\nEnter candidate details:")
    name = input("Name: ")
    email = input("Email: ")
    register_candidate(name, email)
    print("Candidate registered successfully.")

def interact_submit_application():
    print("\nSubmit application:")
    job_id = input("Job ID: ")
    candidate_id = input("Candidate ID: ")
    submit_application(job_id, candidate_id)
    print("Application submitted successfully.")

def main():
    while True:
        print("\nSimple ATS")
        print("1. Add Job")
        print("2. Register Candidate")
        print("3. Submit Application")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            interact_add_job()
        elif choice == "2":
            interact_register_candidate()
        elif choice == "3":
            interact_submit_application()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == '__main__':
    main()