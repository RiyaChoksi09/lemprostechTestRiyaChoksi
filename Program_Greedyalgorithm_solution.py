def schedule_jobs(jobs):
    jobs.sort(key=lambda x: x[1])     ## Sort jobs by  deadlines in ascending order
    n = 3     #lenght of jobs
    # To keep track of the latest available slot
    slots = [False] * n  # False means slot is free, True means slot is occupied
    job_order = [-1] * n  # To store the job order of completion
    completed_jobs = 0

  # we can give priority to deadline who are deadly first in decending order and then give to an for loop and check this for given jobs with it's deadline and by this in decending order we will get our output 
