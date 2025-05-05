{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ebf48257-5c4a-435e-920a-e9ec885a0307",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Employee Management System\n",
      "1. Add Employee\n",
      "2. View All Employees\n",
      "3. Search for Employee\n",
      "4. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice (1-4):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using the Employee Management System.\n"
     ]
    }
   ],
   "source": [
    "employees = {\n",
    "    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}\n",
    "}\n",
    "\n",
    "def display_menu():\n",
    "    print(\"\\nEmployee Management System\")\n",
    "    print(\"1. Add Employee\")\n",
    "    print(\"2. View All Employees\")\n",
    "    print(\"3. Search for Employee\")\n",
    "    print(\"4. Exit\")\n",
    "\n",
    "def add_employee():\n",
    "    try:\n",
    "        emp_id = int(input(\"Enter Employee ID: \"))\n",
    "        if emp_id in employees:\n",
    "            print(\"Employee ID already exists. Please enter a unique ID.\")\n",
    "            return\n",
    "\n",
    "        name = input(\"Enter Employee Name: \")\n",
    "        age = int(input(\"Enter Employee Age: \"))\n",
    "        department = input(\"Enter Employee Department: \")\n",
    "        salary = float(input(\"Enter Employee Salary: \"))\n",
    "\n",
    "        employees[emp_id] = {\n",
    "            'name': name,\n",
    "            'age': age,\n",
    "            'department': department,\n",
    "            'salary': salary\n",
    "        }\n",
    "        print(\"Employee added successfully.\")\n",
    "\n",
    "    except ValueError:\n",
    "        print(\"Invalid input. Please enter the correct data types.\")\n",
    "\n",
    "def view_employees():\n",
    "    if not employees:\n",
    "        print(\"No employees available.\")\n",
    "        return\n",
    "\n",
    "    print(\"\\n{:<10} {:<15} {:<5} {:<15} {:<10}\".format(\"Emp ID\", \"Name\", \"Age\", \"Department\", \"Salary\"))\n",
    "    print(\"-\" * 60)\n",
    "    for emp_id, info in employees.items():\n",
    "        print(\"{:<10} {:<15} {:<5} {:<15} {:<10.2f}\".format(\n",
    "            emp_id, info['name'], info['age'], info['department'], info['salary']\n",
    "        ))\n",
    "\n",
    "def search_employee():\n",
    "    try:\n",
    "        emp_id = int(input(\"Enter Employee ID to search: \"))\n",
    "        if emp_id in employees:\n",
    "            emp = employees[emp_id]\n",
    "            print(f\"\\nDetails of Employee ID {emp_id}:\")\n",
    "            print(f\"Name      : {emp['name']}\")\n",
    "            print(f\"Age       : {emp['age']}\")\n",
    "            print(f\"Department: {emp['department']}\")\n",
    "            print(f\"Salary    : {emp['salary']}\")\n",
    "        else:\n",
    "            print(\"Employee not found.\")\n",
    "    except ValueError:\n",
    "        print(\"Invalid input. Please enter a valid Employee ID.\")\n",
    "\n",
    "def main_menu():\n",
    "    choice = 0\n",
    "    while choice != 4:\n",
    "        display_menu()\n",
    "        try:\n",
    "            choice = int(input(\"Enter your choice (1-4): \"))\n",
    "            if choice == 1:\n",
    "                add_employee()\n",
    "            elif choice == 2:\n",
    "                view_employees()\n",
    "            elif choice == 3:\n",
    "                search_employee()\n",
    "            elif choice == 4:\n",
    "                print(\"Thank you for using the Employee Management System.\")\n",
    "            else:\n",
    "                print(\"Invalid choice. Please select between 1 and 4.\")\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a number.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main_menu()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94350ff3-0397-45ae-8f3e-c403633b8bd3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
