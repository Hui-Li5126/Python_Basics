"""
This is one of Airflow exercise from Udacity data engineer nanodegree program
One-stop-shop for learning Airflow fundamentals:
https://www.astronomer.io/guides
"""
import datetime
"""
datetime module's focus is on efficient attribute extraction for output formatting
and manipulation.
"""
import logging

#Api references: https://airflow.apache.org/_api/index.html
from airflow import DAG
from airflow.models import variable
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.S3_hook import S3Hook

"""
Airflow core ideas:
https://airflow.apache.org/_modules/index.html
DAGs: Directed Acyclic Graph - is a collection of all the tasks you want to run,
     organized in a way that reflects their relationships and dependencies.
Scope: DAG must appear in globals()
Operators: DAGs describe how to run a workflow. Operators determine what actually
    gets done.
       BashOperator, PythonOperator, EmailOperator, SimpleHttpOperator
       MySqlOperator, SqliteOperator, PostgresOperator, MsSqlOperator,
       OracleOperator, JdbcOperator
Sensor: Waits for a certain time, file, database row, S3 key, etc...
Tasks: Once an operator is instantiated, it is referred to as a "task".
Task instances: represents a specific run of a task and is characterized as
    the combination of a dag, a task, and a point in time. Task instances also
    have an indicative state, which could be "running", "success", "failed", etc.

Workflow
DAG: a description of the order in which work should take place
Operator: a class that acts as a template for carrying out some work
Task: a parameterized instance of an operator
Task Instance: a task that 1) has been assigned to a DAG and 2) has a state
associated with a specific run of the DAG
"""


"""
*args: variable number of arguments.
**kwargs: key word variable number of arguments. It is a dictionary.
methods on dict:
get(): returns the value of the specified key
items(): returns a list containing a tuple for each key value pair
keys(): returns a list containing the dictionary's keys
pop(): Removes the element with the specified key
popitem(): removes the last inserted key-value pair
setdefault(): returns the value of the specified key. If the key doesn't
    exist: insert the key, with the specified value
update(): Updates the dictionary with the specified key-value pairs
values(): Returns a list of all the values in the dictionary
"""
def log_details(*args, **kwargs):
    ds = kwargs['ds']
    run_id = kwargs.get('prev_ds')
    next_ds = kwargs.get('next_ds')

    logging.info(f"Execution date is {ds}")
    logging.info(f"My run id is {run_id}")
    if previous_ds:
        logging.info(f"My previous run was on {previous_ds}")
    if next_ds:
        logging.info(f"My next run will be {next_ds}")

dag = DAG(
#below three are must have?
   'lesson1.exercise5', #name
   schedule_interval = "@daily",  #default is daily?
   start_date = datetime.datetime.now() - datetime.timedelta(days=2)
)

list_task = PythonOperator(
task_id = "log_details",
python_callable = log_details,
provide_context = True, 
"""
Airflow passes in an additonal set of keyword arugments: one for each of
the jinja template variables and a templates_dict argument.
https://airflow.apache.org/macros.html

"""
dag = dag
)
