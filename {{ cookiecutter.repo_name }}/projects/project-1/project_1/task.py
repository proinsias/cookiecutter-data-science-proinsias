# + tags=["parameters"]
upstream = None
product = None
run_task = None

# Check if the task should run
if run_task:
    # Your task logic here
    with open(product, 'w') as f:
        f.write('Task executed')
else:
    print('Task is disabled')
