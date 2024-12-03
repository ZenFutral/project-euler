
def reporter(main_function: callable, run_count: int = 10) -> None:    #type: ignore
    from time import time

    start_time: float = time()

    print(f"Executing script {run_count} times...")
    print()
    
    for count in range(1, run_count+1):
        answer: int = main_function()   #type: ignore

        avg_run_time: float = (time() - start_time) / count
        avg_run_time = round(avg_run_time, 3)

        total_run_time: float = time() - start_time
        total_run_time = round(total_run_time, 3)


        print(f"Running: {count} --- Answer: {answer} --- Average Runtime: {avg_run_time}s --- Total Runtime: {total_run_time}s", end="\r")

    print()
    print('====================================================================================')
    print(f"FINISHED --- Answer: {answer} --- Average Runtime: {avg_run_time}s --- Total Runtime: {total_run_time}s")
    print('====================================================================================')
    